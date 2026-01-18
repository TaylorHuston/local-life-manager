---
name: refresh
description: "Silently refresh AI context by reading project configuration and guidelines. Use when starting a new conversation, after context loss, or before major tasks."
model: claude-haiku-4-5-20251001
allowed-tools: Read, Glob
---

# /refresh

Silently reload project context by reading critical configuration files.

## Usage

```bash
/refresh    # Silent context reload
```

## Execution Steps

### 1. Read Core Configuration

```bash
Read: CLAUDE.md
Read: about-me.md
```

**Error if CLAUDE.md missing**: "CLAUDE.md not found"

### 2. Read Shared Documentation

```bash
Glob: shared/docs/**/*.md
# Read each found file
```

Skip silently if not found.

### 3. Read Resource Documentation

```bash
Glob: resources/**/*.md
# Read key research and style guides
```

Skip silently if not found.

### 4. Get Recent Activity

```bash
Bash: git log -3 --format="%h - %s"
```

Skip if git unavailable.

### 5. Output

```
Context refreshed
```

**Silent operation**: Do NOT summarize files, list what was read, or explain context.

## What Gets Loaded

| Category | Files |
|----------|-------|
| Core | CLAUDE.md, about-me.md |
| Shared | shared/docs/**/*.md |
| Resources | resources/**/*.md |
| Git | Last 3 commits |

## Error Handling

| Situation | Action |
|-----------|--------|
| CLAUDE.md missing | Error message |
| Other files missing | Skip silently |
| Git unavailable | Skip git, continue |

## When to Use

- Starting a new conversation
- After long break in session
- Before major planning work
- When context feels stale

**Not for**: Mid-task validation (use /sanity-check), project-specific context (read files directly)
