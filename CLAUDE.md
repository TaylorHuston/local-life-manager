# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a life management hub - a unified repo for personal knowledge, project planning, and AI-assisted life management.

## Directory Structure

```
life-hub/
├── .claude/                    # AI configuration
│   ├── skills/                 # Custom skills (project + personal workflows)
│   ├── memories/               # Persistent context (create this)
│   ├── learning-sessions/      # Learning progress tracking (create this)
│   ├── agents/                 # Agent definitions
│   └── docs/                   # Skill system documentation
├── my-vault/                # Your PKM vault (optional)
├── ideas/[project]/            # Project planning (briefs, issues)
├── spaces/[project]/           # Code repos with specs & ADRs (gitignored)
└── shared/                     # Cross-project standards and templates
```

| Directory | Purpose | Git Status |
|-----------|---------|------------|
| `.claude/` | Skills, memories, learning sessions | Tracked |
| `my-vault/` | PKM vault | Separate repo or gitignored |
| `ideas/` | Project planning (briefs, issues) | Tracked |
| `spaces/` | Code repos (includes specs, ADRs) | Gitignored (each has own repo) |
| `shared/` | Cross-project standards | Tracked |

## Getting Started

1. **Create your memories directory**: `mkdir -p .claude/memories`
2. **Create about-me file**: `.claude/memories/about-me.md` with your context
3. **Create memories index**: `.claude/memories/index.json` (empty array to start)
4. **Configure personal skills**: Update RSS feeds, YouTube channels, etc.

## Claude Data

- **About You**: `.claude/memories/about-me.md` - Summary of who you are
- **Memories**: `.claude/memories/` - JSON entries of important things learned
- **Learning Sessions**: `.claude/learning-sessions/` - Learning progress tracking
- **Skills**: `.claude/skills/` - Custom skills for project and personal workflows

---

## Project Structure

### Planning (`ideas/`)

```
ideas/[project]/
├── README.md                # Status overview
├── project-brief.md         # Vision, problem, audience (private)
├── issues/###-name/         # Work items
│   ├── TASK.md|BUG.md|SPIKE.md
│   ├── PLAN.md              # Phase breakdown
│   └── WORKLOG.md           # Progress tracking
└── notes/                   # Scratchpad
```

### Code (`spaces/`)

```
spaces/[project]/
├── docs/
│   ├── specs/               # Protocol spec (source of truth)
│   └── adrs/                # Architecture decisions
└── src/                     # Implementation
```

**Why specs live with code:** Specs are the contract the code fulfills. Changes to spec and code can be atomic commits.

### Required Files (Every Project)

| File | Purpose | Requirements |
|------|---------|--------------|
| **README.md** | Status overview, quick links | YAML frontmatter (status, created, updated) |
| **project-brief.md** | Vision, problem, solution | Complete sections: Vision, Problem, Solution, Audience, Scope |

---

## Skill System

Skills organized by purpose:

**Project Workflow:**
- Foundation: `/brief`, `/validate-idea`, `/critique`
- Planning: `/spec`, `/adr`, `/research`, `/ui-design`
- Implementation: `/implement`, `/advise`, `/teach`
- Quality: `/quality`, `/security-audit`, `/validate-spec`, `/troubleshoot`
- Completion: `/commit`, `/complete`

**Personal/Learning:**
- Daily: `/daily-journal`, `/daily-review`, `/good-morning`, `/weekly-review`
- Learning: `/learning-system`, `/start-session`, `/flashcards`, `/study-notes`
- Content: `/youtube-catchup`, `/rss-catchup`, `/synthesize`
- Planning: `/life-planning`, `/whats-next`, `/projects-quick`

See `.claude/skills/README.md` for full catalog.

---

## Projects Index

<!-- PROJECTS_INDEX_START -->
```yaml
# Status values: active, on-hold, maintained, archived, experiment
projects:
  # Add your projects here
  # - name: my-project
  #   planning: ideas/my-project/
  #   code: spaces/my-project/
  #   remote: https://github.com/you/my-project
  #   status: active
```
<!-- PROJECTS_INDEX_END -->

---

## Core Rules

1. **Planning vs Code**: Briefs, issues, plans → `ideas/`. Specs, ADRs, code → `spaces/`.
2. **Specs & ADRs live with code**: They're the technical contract, versioned with the codebase.
3. **Precedence**: Project `spaces/[project]/CLAUDE.md` overrides this file.
4. **spaces/ is gitignored**: Each project there has its own git repo.
5. **Never commit unless explicitly asked** or it's part of a prescribed workflow.

---

## Customization

### Personal Skills to Configure

These skills have placeholder configs you should customize:

- **`/rss-catchup`**: Add your RSS feeds to `.claude/skills/rss-catchup/references/feeds.json`
- **`/youtube-catchup`**: Add your channels to `.claude/skills/youtube-catchup/references/channels.json`
- **`/daily-journal`**: Update paths in the skill to match your vault location

### About You

Create `.claude/memories/about-me.md` with sections like:
- Profile (name, role, expertise)
- Communication preferences
- Current focus/goals
- Key accounts and links

---

## Maintenance

- Update `.claude/memories/about-me.md` as preferences change
- Update project READMEs when status changes
- Keep Projects Index current
