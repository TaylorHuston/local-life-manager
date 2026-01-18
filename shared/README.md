# Shared Resources

Cross-project standards, templates, and documentation.

## Structure

```
shared/
├── docs/           # Cross-project standards and guides
├── templates/
│   ├── pm/         # Issue templates (TASK, BUG, SPIKE, PLAN, WORKLOG, SPEC)
│   ├── docs/       # Documentation templates (API, architecture, etc.)
│   └── idea-minimal/  # New project scaffolding
```

## docs/

Standards that apply across all projects:

- **branching-strategy.md** - Git workflow and branch naming
- **development-loop.md** - How to work on issues
- **style-guide.md** - Code style standards
- **tech-stack-decisions.md** - Common technology choices
- **pricing-philosophy.md** - Pricing approach for products

## templates/

### pm/ - Project Management

Issue and planning templates:

| Template | Purpose |
|----------|---------|
| `TASK-template.md` | Feature implementation work |
| `BUG-template.md` | Bug fixes |
| `SPIKE-template.md` | Research/exploration |
| `PLAN-template.md` | Phase breakdown for issues |
| `WORKLOG-template.md` | Progress tracking |
| `SPEC-template.md` | Protocol specification |

### docs/ - Documentation

Templates for project documentation in `spaces/[project]/docs/`:

- API overview
- Architecture overview
- Data model
- Deployment
- Security
- Testing overview
- UI guide

### idea-minimal/ - New Project

Minimal scaffolding for new project ideas:

```bash
cp -r shared/templates/idea-minimal ideas/my-new-project
```

Creates:
- `README.md` - Project status overview
- `project-brief.md` - Vision, problem, solution
