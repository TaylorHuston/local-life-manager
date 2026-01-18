# Minimal Idea Template Usage Guide

## Purpose

This is the **quick-capture template** for brainstorming new ideas without overhead.

Use this when:
- You have a rough idea and want to capture it quickly
- You're not ready for detailed planning yet
- You want to explore multiple ideas without commitment

## Quick Start

```bash
cp -r shared/templates/idea-minimal ideas/your-idea-name
cd ideas/your-idea-name
```

Then fill in `README.md` and `project-brief.md`. Search for `TODO:` to find placeholders.

## What's Included

### README.md
Lightweight overview with:
- One-sentence description
- Problem/solution/audience summary
- Simple status checklist
- Next steps

### project-brief.md
Minimal brief with just the essentials:
- The problem
- The solution
- Target audience
- Core MVP features
- Basic business model
- Open questions

## Metadata

Both files include minimal YAML frontmatter:

```yaml
---
idea: "ProjectName"
status: "concept"
created: "2025-01-15"
updated: "2025-01-15"
---
```

This allows tracking even at the concept stage.

## Workflow

1. **Copy the template** and rename
2. **Fill in README.md** (5 minutes)
3. **Fill in project-brief.md** (15-30 minutes)
4. **Let it simmer** - Come back in a few days
5. **Decide**: Build it, shelve it, or expand to full template

## Expanding to Full Template

When ready for deeper planning:

```bash
# From your idea directory
cp shared/templates/idea/* .

# Or selectively copy specific files
cp shared/templates/idea/competitive-analysis.md .
cp shared/templates/idea/elevator-pitch.md .
```

You can also copy entire subdirectories:

```bash
cp -r shared/templates/idea/features .
cp -r shared/templates/idea/notes .
```

## Tips

- **Don't overthink it**: This template is designed for speed
- **One idea per day**: Capture ideas as they come
- **Review weekly**: Look at all minimal ideas, decide which to pursue
- **Graduate or shelve**: Move to full template or mark as shelved
- **Keep it light**: Resist the urge to add more structure prematurely
