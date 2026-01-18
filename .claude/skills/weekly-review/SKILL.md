---
name: weekly-review
description: Weekly review and planning session. Use at end of week or weekend to review progress, plan next week, and set priorities. Triggers on "weekly review", "plan my week", "what did I do this week", "Sunday planning".
model: claude-opus-4-5-20251101
allowed-tools: Read, Write, Edit, Glob, Bash(gh:*)
---

Run a weekly review and planning session.

## Part 1: Review Last Week

### Journal Review
1. Read journal entries from past 7 days (`my-vault/02 Calendar/`)
2. Summarize:
   - **Did**: Personal highlights
   - **Worked On**: Technical accomplishments
   - **Studied**: Learning progress

### GitHub Activity
```bash
gh search commits --author=TaylorHuston --committer-date=>YYYY-MM-DD
```
Summarize commits by repo/project.

### Learning Progress
1. Read `.claude/learning-sessions/learning-plan.json`
2. Check sessions completed this week
3. Note topics covered and proficiency changes

### Project Progress
1. Scan `ideas/ideas/*/issues/` for completed work
2. Check any WORKLOG.md updates
3. Note project status changes

## Part 2: Current State

Present a brief status:
- **Job Search**: Any interviews, applications, responses?
- **Learning**: Reviews due, next in queue
- **Projects**: What's active, what's blocked?
- **Personal**: Health, social, any concerns?

## Part 3: Plan Next Week

Ask Taylor:
1. "Any interviews or job search priorities this week?"
2. "What's the one thing that would make this week a success?"
3. "Any personal commitments to work around?"

Then suggest:
- **Daily highlights** for each day
- **Learning sessions** to schedule
- **Project work** if time permits

## Part 4: Update Files

1. Update `.claude/memories/about-taylor.md` with any new context
2. Add memories for significant learnings
3. Optionally create tomorrow's journal entry with highlight

Keep it conversational - don't dump everything at once.
