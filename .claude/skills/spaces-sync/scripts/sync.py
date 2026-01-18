#!/usr/bin/env python3
"""
Spaces Sync Tool

Synchronizes the spaces/ directory with the Projects Index in CLAUDE.md.
Validates bidirectionally: index → filesystem and filesystem → index.

Usage:
    python sync.py --check              # Report status only (default)
    python sync.py --pull               # Pull behind branches
    python sync.py --push               # Push ahead branches
    python sync.py --clone              # Clone missing repos
    python sync.py --suggest-additions  # Show repos not in index
    python sync.py --json               # Output as JSON
"""

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field, asdict
from enum import Enum
from pathlib import Path
from typing import Optional


class BranchStatus(Enum):
    UP_TO_DATE = "up_to_date"
    AHEAD = "ahead"
    BEHIND = "behind"
    DIVERGED = "diverged"
    LOCAL_ONLY = "local_only"
    DIRTY = "dirty"
    ERROR = "error"


class RepoStatus(Enum):
    OK = "ok"
    MISSING = "missing"
    NOT_GIT = "not_git"
    REMOTE_MISMATCH = "remote_mismatch"
    REMOTE_ONLY = "remote_only"
    NOT_IN_INDEX = "not_in_index"


@dataclass
class BranchInfo:
    name: str
    status: BranchStatus
    ahead: int = 0
    behind: int = 0
    dirty_files: int = 0
    message: str = ""


@dataclass
class RepoInfo:
    name: str
    status: RepoStatus
    path: Optional[str] = None
    remote: Optional[str] = None
    expected_remote: Optional[str] = None
    branches: list = field(default_factory=list)
    message: str = ""
    index_status: str = "unknown"


@dataclass
class SyncReport:
    repos: list = field(default_factory=list)
    not_in_index: list = field(default_factory=list)
    summary: dict = field(default_factory=dict)


def find_repo_root() -> Path:
    """Find the ideas repo root by looking for CLAUDE.md"""
    current = Path(__file__).resolve()
    for parent in [current] + list(current.parents):
        if (parent / "CLAUDE.md").exists():
            return parent
    # Fallback to environment or current directory
    if "IDEAS_ROOT" in os.environ:
        return Path(os.environ["IDEAS_ROOT"])
    raise FileNotFoundError("Could not find CLAUDE.md - run from ideas repo")


def parse_projects_index(claude_md_path: Path) -> list[dict]:
    """Parse the YAML projects index from CLAUDE.md"""
    content = claude_md_path.read_text()

    # Extract YAML block between markers
    match = re.search(
        r'<!-- SPACES_INDEX_START -->\s*```yaml\s*(.*?)\s*```\s*<!-- SPACES_INDEX_END -->',
        content,
        re.DOTALL
    )

    if not match:
        raise ValueError("Could not find SPACES_INDEX in CLAUDE.md")

    yaml_content = match.group(1)

    # Simple YAML parsing (avoiding external dependency)
    projects = []
    current_project = {}

    for line in yaml_content.split('\n'):
        line = line.rstrip()

        # Skip comments and empty lines
        if not line or line.strip().startswith('#'):
            continue

        # New project starts with "- name:"
        if re.match(r'\s*-\s*name:', line):
            if current_project:
                projects.append(current_project)
            name_match = re.match(r'\s*-\s*name:\s*(.+)', line)
            current_project = {"name": name_match.group(1).strip()}
        elif current_project and ':' in line:
            # Parse key: value
            key_match = re.match(r'\s+(\w+):\s*(.+)?', line)
            if key_match:
                key = key_match.group(1)
                value = key_match.group(2).strip() if key_match.group(2) else ""
                current_project[key] = value

    if current_project:
        projects.append(current_project)

    return projects


def run_git(repo_path: Path, *args) -> tuple[int, str, str]:
    """Run a git command and return (returncode, stdout, stderr)"""
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_path)] + list(args),
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except subprocess.TimeoutExpired:
        return 1, "", "Command timed out"
    except Exception as e:
        return 1, "", str(e)


def get_repo_remote(repo_path: Path) -> Optional[str]:
    """Get the origin remote URL"""
    code, stdout, _ = run_git(repo_path, "remote", "get-url", "origin")
    return stdout if code == 0 else None


def get_branch_status(repo_path: Path, branch: str) -> BranchInfo:
    """Get status of a specific branch"""
    info = BranchInfo(name=branch, status=BranchStatus.UP_TO_DATE)

    # Check if this is the current branch and if it's dirty
    code, current_branch, _ = run_git(repo_path, "branch", "--show-current")
    if code == 0 and current_branch == branch:
        code, status_output, _ = run_git(repo_path, "status", "--porcelain")
        if code == 0 and status_output:
            info.dirty_files = len(status_output.split('\n'))
            info.status = BranchStatus.DIRTY
            info.message = f"{info.dirty_files} uncommitted files"
            return info

    # Check upstream tracking
    code, upstream, _ = run_git(repo_path, "rev-parse", "--abbrev-ref", f"{branch}@{{upstream}}")
    if code != 0:
        info.status = BranchStatus.LOCAL_ONLY
        info.message = "No remote tracking branch"
        return info

    # Get ahead/behind counts
    code, ahead_str, _ = run_git(repo_path, "rev-list", "--count", f"{upstream}..{branch}")
    code2, behind_str, _ = run_git(repo_path, "rev-list", "--count", f"{branch}..{upstream}")

    if code == 0 and code2 == 0:
        info.ahead = int(ahead_str) if ahead_str.isdigit() else 0
        info.behind = int(behind_str) if behind_str.isdigit() else 0

        if info.ahead > 0 and info.behind > 0:
            info.status = BranchStatus.DIVERGED
            info.message = f"{info.ahead} ahead, {info.behind} behind"
        elif info.ahead > 0:
            info.status = BranchStatus.AHEAD
            info.message = f"{info.ahead} commits to push"
        elif info.behind > 0:
            info.status = BranchStatus.BEHIND
            info.message = f"{info.behind} commits to pull"
        else:
            info.status = BranchStatus.UP_TO_DATE
            info.message = "Up to date"

    return info


def check_repo(repo_path: Path, expected_remote: Optional[str] = None,
               index_status: str = "unknown") -> RepoInfo:
    """Check status of a single repository"""
    name = repo_path.name
    info = RepoInfo(name=name, status=RepoStatus.OK, path=str(repo_path),
                    index_status=index_status)

    if not repo_path.exists():
        info.status = RepoStatus.MISSING
        info.message = "Directory does not exist"
        info.expected_remote = expected_remote
        return info

    git_dir = repo_path / ".git"
    if not git_dir.exists():
        info.status = RepoStatus.NOT_GIT
        info.message = "Not a git repository"
        return info

    # Get actual remote
    info.remote = get_repo_remote(repo_path)
    info.expected_remote = expected_remote

    # Check remote matches if expected
    if expected_remote and info.remote:
        # Normalize URLs for comparison (remove .git suffix, trailing slashes)
        def normalize_url(url):
            url = url.rstrip('/')
            if url.endswith('.git'):
                url = url[:-4]
            # Convert SSH to HTTPS for comparison
            if url.startswith('git@github.com:'):
                url = 'https://github.com/' + url[15:]
            return url.lower()

        if normalize_url(info.remote) != normalize_url(expected_remote):
            info.status = RepoStatus.REMOTE_MISMATCH
            info.message = f"Remote mismatch: expected {expected_remote}, got {info.remote}"
            return info

    # Fetch to get latest remote info
    run_git(repo_path, "fetch", "--all", "--quiet")

    # Get all local branches
    code, branches_output, _ = run_git(repo_path, "branch", "--format=%(refname:short)")
    if code == 0 and branches_output:
        for branch in branches_output.split('\n'):
            branch = branch.strip()
            if branch:
                branch_info = get_branch_status(repo_path, branch)
                info.branches.append(branch_info)

    return info


def scan_spaces_directory(spaces_path: Path) -> list[Path]:
    """Find all git repositories in spaces/"""
    repos = []
    if not spaces_path.exists():
        return repos

    for item in spaces_path.iterdir():
        if item.is_dir():
            if (item / ".git").exists():
                repos.append(item)
            else:
                # Check for nested repos (like yourbench-legacy/)
                for nested in item.iterdir():
                    if nested.is_dir() and (nested / ".git").exists():
                        repos.append(nested)

    return repos


def pull_branch(repo_path: Path, branch: str) -> bool:
    """Pull a branch (fast-forward only)"""
    # Checkout branch first if not current
    code, current, _ = run_git(repo_path, "branch", "--show-current")
    if current != branch:
        code, _, err = run_git(repo_path, "checkout", branch)
        if code != 0:
            return False

    code, _, err = run_git(repo_path, "pull", "--ff-only")
    return code == 0


def push_branch(repo_path: Path, branch: str) -> bool:
    """Push a branch"""
    code, _, err = run_git(repo_path, "push", "origin", branch)
    return code == 0


def push_new_branch(repo_path: Path, branch: str) -> bool:
    """Push a new branch with upstream tracking"""
    code, _, err = run_git(repo_path, "push", "-u", "origin", branch)
    return code == 0


def clone_repo(spaces_path: Path, name: str, remote: str, branch: str) -> bool:
    """Clone a repository"""
    target = spaces_path / name
    try:
        result = subprocess.run(
            ["git", "clone", "-b", branch, remote, str(target)],
            capture_output=True,
            text=True,
            timeout=120
        )
        return result.returncode == 0
    except Exception:
        return False


def generate_report(repo_root: Path, do_pull: bool = False, do_push: bool = False,
                   do_clone: bool = False) -> SyncReport:
    """Generate a full sync report"""
    report = SyncReport()
    spaces_path = repo_root / "spaces"
    claude_md_path = repo_root / "CLAUDE.md"

    # Parse index
    projects = parse_projects_index(claude_md_path)

    # Track which paths we've seen from the index
    indexed_paths = set()

    # Check each project in the index
    for project in projects:
        name = project.get("name", "unknown")
        code_path = project.get("code", "")
        remote = project.get("remote", "")
        branch = project.get("branch", "main")
        status = project.get("status", "unknown")

        # Skip remote-only entries
        if status == "remote-only":
            report.repos.append(RepoInfo(
                name=name,
                status=RepoStatus.REMOTE_ONLY,
                expected_remote=remote,
                index_status=status,
                message="Tracked remotely, not cloned locally"
            ))
            continue

        # Skip entries without code path
        if not code_path:
            continue

        repo_path = repo_root / code_path.rstrip('/')
        indexed_paths.add(repo_path.resolve())

        info = check_repo(repo_path, remote, status)

        # Handle missing repos
        if info.status == RepoStatus.MISSING and do_clone and remote:
            print(f"Cloning {name}...")
            if clone_repo(spaces_path, name, remote, branch):
                info = check_repo(repo_path, remote, status)
                info.message = "Cloned successfully"

        # Handle branch operations
        if info.status == RepoStatus.OK:
            for branch_info in info.branches:
                if branch_info.status == BranchStatus.BEHIND and do_pull:
                    print(f"Pulling {name}/{branch_info.name}...")
                    if pull_branch(repo_path, branch_info.name):
                        branch_info.status = BranchStatus.UP_TO_DATE
                        branch_info.message = f"Pulled {branch_info.behind} commits"
                        branch_info.behind = 0

                elif branch_info.status == BranchStatus.AHEAD and do_push:
                    print(f"Pushing {name}/{branch_info.name}...")
                    if push_branch(repo_path, branch_info.name):
                        branch_info.status = BranchStatus.UP_TO_DATE
                        branch_info.message = f"Pushed {branch_info.ahead} commits"
                        branch_info.ahead = 0

                elif branch_info.status == BranchStatus.LOCAL_ONLY and do_push:
                    print(f"Pushing new branch {name}/{branch_info.name}...")
                    if push_new_branch(repo_path, branch_info.name):
                        branch_info.status = BranchStatus.UP_TO_DATE
                        branch_info.message = "Pushed new branch"

        report.repos.append(info)

    # Find repos not in index
    actual_repos = scan_spaces_directory(spaces_path)
    for repo_path in actual_repos:
        if repo_path.resolve() not in indexed_paths:
            remote = get_repo_remote(repo_path)
            report.not_in_index.append({
                "name": repo_path.name,
                "path": str(repo_path.relative_to(repo_root)),
                "remote": remote
            })

    # Generate summary
    report.summary = {
        "total_indexed": len([r for r in report.repos if r.status != RepoStatus.REMOTE_ONLY]),
        "remote_only": len([r for r in report.repos if r.status == RepoStatus.REMOTE_ONLY]),
        "ok": len([r for r in report.repos if r.status == RepoStatus.OK]),
        "missing": len([r for r in report.repos if r.status == RepoStatus.MISSING]),
        "not_in_index": len(report.not_in_index),
        "branches_ahead": sum(
            len([b for b in r.branches if b.status == BranchStatus.AHEAD])
            for r in report.repos
        ),
        "branches_behind": sum(
            len([b for b in r.branches if b.status == BranchStatus.BEHIND])
            for r in report.repos
        ),
        "branches_dirty": sum(
            len([b for b in r.branches if b.status == BranchStatus.DIRTY])
            for r in report.repos
        ),
        "branches_diverged": sum(
            len([b for b in r.branches if b.status == BranchStatus.DIVERGED])
            for r in report.repos
        ),
        "branches_local_only": sum(
            len([b for b in r.branches if b.status == BranchStatus.LOCAL_ONLY])
            for r in report.repos
        ),
    }

    return report


def format_status_symbol(status: BranchStatus) -> str:
    """Get symbol for branch status"""
    symbols = {
        BranchStatus.UP_TO_DATE: "✓",
        BranchStatus.AHEAD: "↑",
        BranchStatus.BEHIND: "↓",
        BranchStatus.DIVERGED: "↕",
        BranchStatus.LOCAL_ONLY: "+",
        BranchStatus.DIRTY: "!",
        BranchStatus.ERROR: "✗",
    }
    return symbols.get(status, "?")


def format_report(report: SyncReport) -> str:
    """Format report as human-readable text"""
    lines = []
    lines.append("=" * 60)
    lines.append("SPACES SYNC REPORT")
    lines.append("=" * 60)
    lines.append("")

    # Group repos by status
    ok_repos = [r for r in report.repos if r.status == RepoStatus.OK]
    problem_repos = [r for r in report.repos if r.status not in (RepoStatus.OK, RepoStatus.REMOTE_ONLY)]
    remote_only = [r for r in report.repos if r.status == RepoStatus.REMOTE_ONLY]

    # Show problem repos first
    if problem_repos:
        lines.append("## Issues")
        lines.append("")
        for repo in problem_repos:
            lines.append(f"  {repo.name}")
            lines.append(f"    Status: {repo.status.value}")
            lines.append(f"    {repo.message}")
            if repo.expected_remote:
                lines.append(f"    Remote: {repo.expected_remote}")
            lines.append("")

    # Show OK repos with branch details
    if ok_repos:
        lines.append("## Repositories")
        lines.append("")
        for repo in ok_repos:
            branch_count = len(repo.branches)
            branch_summary = f"({branch_count} branch{'es' if branch_count != 1 else ''})"
            lines.append(f"  {repo.name} {branch_summary}")
            for branch in repo.branches:
                symbol = format_status_symbol(branch.status)
                msg = f" - {branch.message}" if branch.message else ""
                lines.append(f"    {symbol} {branch.name}{msg}")
            lines.append("")

    # Show not in index
    if report.not_in_index:
        lines.append("## Not in Index")
        lines.append("")
        for item in report.not_in_index:
            lines.append(f"  ? {item['name']}")
            lines.append(f"    Path: {item['path']}")
            if item['remote']:
                lines.append(f"    Remote: {item['remote']}")
            lines.append("")

    # Summary
    lines.append("-" * 60)
    lines.append("SUMMARY")
    lines.append("-" * 60)
    s = report.summary
    lines.append(f"  Indexed repos:    {s['total_indexed']} ({s['ok']} ok, {s['missing']} missing)")
    lines.append(f"  Remote-only:      {s['remote_only']}")
    lines.append(f"  Not in index:     {s['not_in_index']}")
    lines.append("")
    lines.append(f"  Branches ahead:   {s['branches_ahead']}")
    lines.append(f"  Branches behind:  {s['branches_behind']}")
    lines.append(f"  Branches dirty:   {s['branches_dirty']}")
    lines.append(f"  Branches diverged:{s['branches_diverged']}")
    lines.append(f"  Local-only:       {s['branches_local_only']}")
    lines.append("")

    return "\n".join(lines)


def serialize_report(report: SyncReport) -> dict:
    """Convert report to JSON-serializable dict"""
    def serialize_enum(obj):
        if isinstance(obj, Enum):
            return obj.value
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

    result = {
        "repos": [],
        "not_in_index": report.not_in_index,
        "summary": report.summary
    }

    for repo in report.repos:
        repo_dict = {
            "name": repo.name,
            "status": repo.status.value,
            "path": repo.path,
            "remote": repo.remote,
            "expected_remote": repo.expected_remote,
            "message": repo.message,
            "index_status": repo.index_status,
            "branches": []
        }
        for branch in repo.branches:
            repo_dict["branches"].append({
                "name": branch.name,
                "status": branch.status.value,
                "ahead": branch.ahead,
                "behind": branch.behind,
                "dirty_files": branch.dirty_files,
                "message": branch.message
            })
        result["repos"].append(repo_dict)

    return result


def main():
    parser = argparse.ArgumentParser(description="Sync spaces/ with Projects Index")
    parser.add_argument("--check", action="store_true", help="Check status only (default)")
    parser.add_argument("--pull", action="store_true", help="Pull behind branches")
    parser.add_argument("--push", action="store_true", help="Push ahead/local-only branches")
    parser.add_argument("--clone", action="store_true", help="Clone missing repos")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--suggest-additions", action="store_true",
                       help="Show YAML for repos not in index")

    args = parser.parse_args()

    try:
        repo_root = find_repo_root()
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    report = generate_report(
        repo_root,
        do_pull=args.pull,
        do_push=args.push,
        do_clone=args.clone
    )

    if args.json:
        print(json.dumps(serialize_report(report), indent=2))
    elif args.suggest_additions:
        if report.not_in_index:
            print("# Add to CLAUDE.md Projects Index:\n")
            for item in report.not_in_index:
                print(f"  - name: {item['name']}")
                print(f"    code: {item['path']}/")
                if item['remote']:
                    print(f"    remote: {item['remote']}")
                print(f"    branch: main")
                print(f"    status: active  # or: on-hold, archived, experiment")
                print()
        else:
            print("All repos are in the index.")
    else:
        print(format_report(report))


if __name__ == "__main__":
    main()
