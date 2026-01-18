# /init-space

Initialize a new code repository in `spaces/` with standard structure.

## Public vs Private Split

**spaces/ is PUBLIC** (pushed to GitHub). Only include:
- README.md, CLAUDE.md
- docs/adrs/ (technical decisions)
- Code documentation

**ideas/ is PRIVATE** (meta-repo only). Keep there:
- project-brief.md, specs/, issues/
- critiques, competitive analysis
- Pricing, strategy docs

See CLAUDE.md "Public vs Private Documentation" for full policy.

## Usage

```bash
/init-space coordinatr              # Initialize existing idea
/init-space new-project --type next # Initialize new project
/init-space myapp --type python     # Python project
```

## Supported Project Types

| Type | Command | Creates |
|------|---------|---------|
| `next` | `create-next-app` | Next.js with App Router, TypeScript, Tailwind |
| `python` | `uv init` or manual | Python with pyproject.toml |
| `empty` | manual | Just standard structure |

## Standard Structure (All Projects)

Every space MUST have:

```
spaces/[project]/
├── CLAUDE.md              # Project-specific AI instructions
├── README.md              # Project overview
├── CHANGELOG.md           # Release history
└── docs/
    ├── README.md          # Docs index
    ├── architecture.md    # System overview
    └── adrs/
        └── README.md      # ADR index + template
```

## Execution Flow

### 1. Validate Project

```bash
# Check if idea exists (optional but recommended)
ls ideas/[project]/project-brief.md

# Check space doesn't already exist
ls spaces/[project]/
```

### 2. Create Project

**Next.js:**
```bash
cd spaces
npx create-next-app@latest [project] \
  --typescript --tailwind --eslint --app \
  --import-alias="@/*" --use-pnpm --yes
```

**Python:**
```bash
cd spaces
mkdir [project] && cd [project]
uv init  # or: python -m venv .venv && touch pyproject.toml
```

**Empty:**
```bash
mkdir -p spaces/[project]
```

### 3. Create Standard Structure

```bash
mkdir -p docs/adrs
```

Create these files:

**CHANGELOG.md:**
```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project setup
```

**CLAUDE.md:**
```markdown
# [Project Name]

Project-specific instructions for AI assistants.

## Overview

[Brief description from project-brief.md if exists]

## Development

```bash
pnpm dev        # Start dev server
pnpm test       # Run tests
pnpm build      # Production build
```

## Key Files

| File | Purpose |
|------|---------|
| `src/app/` | Next.js app routes |
| `convex/` | Backend functions |

## Conventions

- [Project-specific conventions]

## Related Documentation

- [Project Brief](../../ideas/[project]/project-brief.md)
- [Specs](../../ideas/[project]/specs/)
```

**docs/README.md:**
```markdown
# Documentation

Technical documentation for [project].

## Contents

| File/Directory | Purpose |
|----------------|---------|
| `architecture.md` | System overview |
| `adrs/` | Architecture Decision Records |

## Planning Documentation

Planning docs live in the meta-repo at `ideas/[project]/`.
```

**docs/architecture.md:**
```markdown
# Architecture Overview

## System Diagram

[TODO: Add system diagram]

## Components

| Component | Purpose |
|-----------|---------|
| `src/app/` | Next.js routes |
| `convex/` | Backend functions |

## Data Flow

[TODO: Document data flow]

## External Services

| Service | Purpose |
|---------|---------|
| Convex | Database + backend |
| Clerk | Authentication |
| Vercel | Hosting |

## Related

- [ADRs](adrs/) - Architecture decisions
- [Project Brief](../../../ideas/[project]/project-brief.md) - Vision and requirements
```

**docs/adrs/README.md:**
```markdown
# Architecture Decision Records

ADRs document significant technical decisions made during implementation.

## Index

| ADR | Title | Status |
|-----|-------|--------|
| - | (none yet) | - |

## Template

\```markdown
# ADR-###: Title

**Status**: Proposed | Accepted | Deprecated | Superseded
**Date**: YYYY-MM-DD

## Context
Why is this decision needed?

## Decision
What did we decide?

## Consequences
What are the trade-offs?
\```
```

### 4. Initialize Git (if not exists)

```bash
git init
```

### 5. Stage Files (DO NOT COMMIT)

```bash
git add .
git status
```

**CRITICAL**: Do NOT commit. Show user the staged files and remind them:

```
Files staged and ready. When you're ready to commit, run:
/commit [project]
```

## Safety Rules

1. **NEVER commit automatically** - only stage files
2. **NEVER overwrite existing space** - error if directory exists
3. **Always create standard structure** - even for framework scaffolds

## Post-Init Checklist

Display to user after init:

```markdown
## Space Initialized: [project]

### Created
- [ ] Project scaffolded
- [ ] CLAUDE.md created
- [ ] README.md created
- [ ] CHANGELOG.md created
- [ ] docs/architecture.md created
- [ ] docs/adrs/ structure created
- [ ] Git initialized
- [ ] Files staged (not committed)

### Next Steps
1. Review staged files: `git status`
2. Commit when ready: `/commit [project]`
3. Add to Projects Index in CLAUDE.md (if not already)
4. Set up remote: `git remote add origin [url]`
```

## Error Handling

| Error | Resolution |
|-------|------------|
| Space already exists | Error: "Space already exists at spaces/[project]/" |
| No idea exists | Warning: "No planning docs at ideas/[project]/. Continue anyway?" |
| Scaffold fails | Clean up partial directory, show error |

## Integration with Projects Index

After successful init, remind user to add to CLAUDE.md Projects Index if not present:

```yaml
- name: [project]
  planning: ideas/[project]/
  code: spaces/[project]/
  remote: [to be added]
  branch: main
  status: active
```
