# Worklog Schema Specification

Worklogs track the history of work on issues for AI context preservation, structured handoffs between agents, and lessons learned extraction.

## Purpose

1. **AI Context Preservation**: New sessions load `_state.json` for instant context
2. **Structured Handoffs**: Clear agent-to-agent handoff with context
3. **Lessons Database**: Queryable learnings across all projects
4. **Resume After Interruption**: Know exactly where work stopped

## Directory Structure

```
ideas/[project]/issues/###-slug/
├── TASK.md              # Issue definition
├── PLAN.md              # Phase breakdown
└── worklog/
    ├── _state.json      # Current state (quick context load)
    ├── 001-*.json       # Entry files (chronological)
    ├── 002-*.json
    └── ...
```

### File Naming Convention

Entry files: `{sequence}-{type}-{slug}.json`

Examples:
- `001-phase-nextjs-init.json`
- `002-phase-convex-setup.json`
- `003-handoff-code-review.json`
- `004-manual-dark-mode-fix.json`
- `005-decision-auth-provider.json`

Types:
- `phase` - Work on a PLAN.md phase
- `handoff` - Transfer between agents
- `manual` - Human work outside /implement
- `decision` - Architecture/design decision
- `research` - Research findings
- `blocker` - Documenting a blocker
- `resolution` - Resolving a blocker

---

## Schema: `_state.json`

Quick-load file for new AI sessions. Updated after every entry.

```json
{
  "$schema": "worklog-state-v1",
  "issue_id": "YB-2",
  "issue_type": "TASK",
  "issue_title": "Initialize Next.js 16 project",

  "status": "in_progress",
  "current_phase": "3",
  "current_agent": "code-reviewer",
  "branch": "feature/YB-2-nextjs-init",

  "summary": "Next.js 16 + Convex init complete, awaiting code review",

  "progress": {
    "phases_total": 5,
    "phases_complete": 5,
    "quality_gates_passed": ["typescript", "tests"],
    "quality_gates_pending": ["code-review", "security"]
  },

  "blockers": [],

  "key_decisions": [
    "Using Clerk for auth (faster than custom)",
    "Tailwind 3.4.x (v4 has breaking changes)"
  ],

  "key_files": [
    "src/app/page.tsx",
    "convex/schema.ts",
    "src/lib/auth.ts"
  ],

  "last_entry": "003-handoff-code-review.json",
  "last_updated": "2025-11-03T16:24:00Z",
  "entries_count": 3
}
```

### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `$schema` | string | yes | Schema version for validation |
| `issue_id` | string | yes | Issue identifier (e.g., "YB-2") |
| `issue_type` | enum | yes | `TASK`, `BUG`, or `SPIKE` |
| `issue_title` | string | yes | Human-readable title |
| `status` | enum | yes | `open`, `in_progress`, `blocked`, `review`, `complete` |
| `current_phase` | string | no | Current PLAN.md phase (e.g., "3", "2.1") |
| `current_agent` | string | no | Agent currently responsible |
| `branch` | string | no | Git branch name |
| `summary` | string | yes | 1-2 sentence current state summary |
| `progress` | object | yes | Phase and quality gate progress |
| `blockers` | array | yes | Active blockers (can be empty) |
| `key_decisions` | array | yes | Important decisions for context |
| `key_files` | array | yes | Most relevant files touched |
| `last_entry` | string | yes | Filename of most recent entry |
| `last_updated` | datetime | yes | ISO 8601 timestamp |
| `entries_count` | integer | yes | Total entry count |

---

## Schema: Entry Files

Each entry captures a discrete unit of work.

**REQUIRED**: Every entry MUST include an `author` field identifying who performed the work. This is critical for:
- Understanding which agent/human performed each phase
- Tracking handoffs between agents
- Debugging issues in the workflow
- Attributing decisions and learnings

```json
{
  "$schema": "worklog-entry-v1",
  "id": "YB-2-003",
  "sequence": 3,
  "timestamp": "2025-11-03T16:24:00Z",

  "type": "handoff",
  "phase": "post-implementation",
  "author": {
    "agent": "project-manager",
    "human": null
  },

  "summary": "All 5 phases complete, passing to code-reviewer for validation",

  "work": {
    "description": "Completed full implementation of Next.js 16 project initialization...",
    "files_changed": [
      {
        "path": "src/app/page.tsx",
        "action": "created",
        "purpose": "Hello World page with Convex integration"
      },
      {
        "path": "convex/schema.ts",
        "action": "created",
        "purpose": "Database schema definition"
      }
    ],
    "commits": [
      {
        "sha": "abc1234",
        "message": "feat(YB-2): initialize Next.js 16 with TypeScript"
      }
    ],
    "tests": {
      "ran": true,
      "passing": 12,
      "failing": 0,
      "skipped": 0
    },
    "quality_scores": {
      "typescript": "pass",
      "build": "pass"
    }
  },

  "handoff": {
    "from": "project-manager",
    "to": "code-reviewer",
    "context": "Full implementation complete. All 5 phases done. Need comprehensive code review before merge.",
    "expectations": [
      "Review all configuration files",
      "Verify TypeScript strict mode",
      "Check for security issues",
      "Validate build passes"
    ],
    "artifacts": [
      "src/app/",
      "convex/",
      "package.json",
      "tsconfig.json"
    ]
  },

  "learnings": {
    "decisions": [
      {
        "what": "Used manual installation instead of create-next-app",
        "why": "Directory was not empty",
        "alternatives": ["Delete and recreate directory"],
        "reversible": true,
        "tags": ["next.js", "setup", "tooling"]
      }
    ],
    "gotchas": [
      {
        "issue": "Tailwind v4 breaks PostCSS configuration",
        "symptom": "Build fails with PostCSS plugin error",
        "solution": "Downgrade to Tailwind 3.4.x",
        "prevention": "Check Tailwind version compatibility before upgrading",
        "tags": ["tailwind", "postcss", "config", "breaking-change"]
      }
    ],
    "lessons": [
      {
        "insight": "Always run production build before requesting code review",
        "context": "Dev server can pass while production build fails",
        "applies_to": ["all-projects"],
        "tags": ["workflow", "quality", "code-review"]
      }
    ],
    "patterns": [
      {
        "name": "ConvexProvider wrapper pattern",
        "description": "Create client component wrapper for Convex context",
        "example_file": "src/app/ConvexClientProvider.tsx",
        "reusable": true,
        "tags": ["convex", "react", "context"]
      }
    ]
  },

  "next_steps": [
    "Code reviewer: Run comprehensive quality check",
    "Code reviewer: Verify all quality gates pass",
    "After approval: Create PR to develop branch"
  ],

  "blockers": []
}
```

### Entry Types

| Type | Use Case | Required Fields |
|------|----------|-----------------|
| `phase` | PLAN.md phase completion | `work`, `phase` |
| `handoff` | Agent-to-agent transfer | `handoff.from`, `handoff.to`, `handoff.context` |
| `manual` | Human work outside /implement | `work.description`, `author.human` |
| `decision` | Architecture/design decision | `learnings.decisions` (at least one) |
| `research` | Research findings | `work.description`, `learnings` |
| `blocker` | Documenting impediment | `blockers` (at least one) |
| `resolution` | Resolving blocker | `work.description`, reference to blocker |

### Author Object

```json
{
  "agent": "frontend-specialist",  // or null if human
  "human": null                     // or username if human
}
```

At least one must be non-null.

### Work Object

```json
{
  "description": "Detailed description of work done...",
  "approach": "Optional: how the work was approached",
  "files_changed": [...],
  "commits": [...],
  "tests": {...},
  "quality_scores": {...},
  "time_spent_minutes": 45  // optional
}
```

### Files Changed

```json
{
  "path": "src/app/page.tsx",
  "action": "created",      // created, modified, deleted, renamed
  "purpose": "Brief description of why",
  "old_path": null          // for renames only
}
```

### Handoff Object

Required when `type: "handoff"`:

```json
{
  "from": "project-manager",
  "to": "code-reviewer",
  "context": "What the receiving agent needs to know",
  "expectations": ["What the receiving agent should do"],
  "artifacts": ["Key files/directories to focus on"],
  "warnings": ["Any gotchas or things to watch for"]
}
```

### Learnings Object

All fields optional but encouraged:

```json
{
  "decisions": [{
    "what": "What was decided",
    "why": "Rationale",
    "alternatives": ["Other options considered"],
    "reversible": true,
    "tags": ["category", "technology"]
  }],
  "gotchas": [{
    "issue": "What went wrong",
    "symptom": "How it manifested",
    "solution": "How it was fixed",
    "prevention": "How to avoid in future",
    "tags": ["category"]
  }],
  "lessons": [{
    "insight": "What was learned",
    "context": "When this applies",
    "applies_to": ["project-name", "all-projects"],
    "tags": ["category"]
  }],
  "patterns": [{
    "name": "Pattern name",
    "description": "What it does",
    "example_file": "path/to/example",
    "reusable": true,
    "tags": ["category"]
  }]
}
```

### Blocker Object

```json
{
  "id": "blocker-001",
  "type": "technical",        // technical, dependency, decision, external
  "description": "What's blocking progress",
  "impact": "What can't proceed",
  "needs": "What's needed to unblock",
  "owner": "Who can resolve this",
  "created": "2025-11-03T16:00:00Z",
  "resolved": null,           // timestamp when resolved
  "resolution": null          // how it was resolved
}
```

---

## Tag Taxonomy

Consistent tags enable cross-project queries.

### Technology Tags
`next.js`, `react`, `convex`, `typescript`, `tailwind`, `clerk`, `prisma`, `postgresql`, `redis`

### Domain Tags
`auth`, `database`, `api`, `frontend`, `backend`, `testing`, `deployment`, `config`, `security`

### Workflow Tags
`setup`, `refactoring`, `optimization`, `debugging`, `documentation`, `code-review`

### Issue Tags
`breaking-change`, `regression`, `performance`, `compatibility`, `tooling`

### Scope Tags
`all-projects`, `[project-name]`

---

## Querying Worklogs

### Find all gotchas for a technology
```bash
grep -r '"tags":.*"tailwind"' ideas/*/issues/*/worklog/*.json
```

### Find all handoffs to code-reviewer
```bash
grep -r '"to": "code-reviewer"' ideas/*/issues/*/worklog/*.json
```

### Find all lessons that apply to all projects
```bash
grep -r '"applies_to":.*"all-projects"' ideas/*/issues/*/worklog/*.json
```

### Get current state of all in-progress issues
```bash
find ideas/*/issues/*/worklog/_state.json -exec grep -l '"status": "in_progress"' {} \;
```

---

## Lessons Extraction

Periodic extraction to build institutional knowledge:

```
resources/lessons-learned/
├── by-tag/
│   ├── auth.json           # All auth-related learnings
│   ├── testing.json
│   └── next.js.json
├── gotchas.json            # All gotchas, searchable
├── patterns.json           # Reusable patterns
└── index.json              # Summary and stats
```

### Extracted Lesson Format

```json
{
  "id": "lesson-2025-001",
  "source": {
    "project": "yourbench",
    "issue": "YB-2",
    "entry": "003-handoff-code-review.json"
  },
  "type": "gotcha",
  "content": {
    "issue": "Tailwind v4 breaks PostCSS configuration",
    "solution": "Downgrade to Tailwind 3.4.x"
  },
  "tags": ["tailwind", "postcss", "breaking-change"],
  "extracted": "2025-11-03",
  "referenced_count": 0
}
```

---

## Migration from Markdown

Existing WORKLOG.md files can be converted:

1. Parse markdown entries (split on `## YYYY-MM-DD`)
2. Extract structured data (files, tests, decisions)
3. Infer type from content (phase, manual, decision)
4. Generate JSON entries
5. Create `_state.json` from latest entry
6. Archive original as `WORKLOG.md.bak`

The `/worklog --migrate` flag will handle this.

---

## Version History

- **v1** (2025-01): Initial JSON schema
