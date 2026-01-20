# [Project Name] - AI Instructions

## Project Overview

[Brief description of what this project does and its core value proposition]

**Core value proposition:**
- [Key benefit 1]
- [Key benefit 2]
- [Key benefit 3]

## Tech Stack

| Layer | Choice |
|-------|--------|
| Backend | [Framework/Language] |
| Database | [Database + hosting] |
| ORM/Query | [ORM or query library] |
| Frontend | [Framework or approach] |
| Auth | [Auth provider] |
| Hosting | [Platform] |
| [Other key services] | [Details] |

**See ADRs for architecture decisions**: `docs/adrs/`

## Repository Structure

```
[project-root]/
├── docs/
│   ├── adrs/                   # Architecture Decision Records
│   ├── architecture-overview.md  # System design (update as built)
│   └── data-model.md           # Entity schemas (update as built)
├── src/ (or app/)              # Source code
│   ├── [models/]               # Data models
│   ├── [routes/ or api/]       # HTTP endpoints
│   ├── [services/]             # Business logic
│   ├── [components/]           # UI components (if applicable)
│   └── [lib/]                  # Utilities
├── tests/                      # Test files
└── [other directories]
```

**Planning docs in meta-repo**: `ideas/[project]/`

## Development Setup

### Prerequisites
- [Language/runtime version]
- [Database installation]
- [Other requirements]

### Local Development
```bash
# Clone and install
git clone [repo-url]
cd [project]
[install command]  # e.g., npm install, pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your local values

# Run migrations (if applicable)
[migration command]

# Start dev server
[run command]  # e.g., npm run dev, flask run
```

## Development Guidelines

### Code Style
- [Style guide - e.g., PEP 8, Airbnb, etc.]
- [Linting tool and config]
- [Formatting tool - e.g., Prettier, Black]

### Database
- [Model location]
- [Migration approach]
- [Common patterns - e.g., timestamps, soft deletes]

### API Design
- [REST/GraphQL/tRPC approach]
- [Endpoint structure]
- [Error handling patterns]
- [Validation approach]

### Frontend Patterns
- [Component structure]
- [State management approach]
- [Styling approach]
- [Key libraries and when to use them]

### Auth Integration
- [How auth works]
- [Where auth logic lives]
- [Session management]

### [Other Key Integration]
- [How integration works]
- [Where code lives]
- [Common patterns]

## Data Model

Core entities (see `docs/data-model.md` for full schemas):

**[Entity Category 1]:**
- **EntityName** - [Brief description, key fields]
- **EntityName** - [Brief description, key fields]

**[Entity Category 2]:**
- **EntityName** - [Brief description, key fields]
- **EntityName** - [Brief description, key fields]

### Data Model Notes
- [Important relationships]
- [Denormalization decisions]
- [Indexing strategies]
- [Any special patterns]

## Common Tasks

### Adding a new entity
1. [Step 1]
2. [Step 2]
3. [Step 3]
4. Update `docs/data-model.md`

### Adding a new API endpoint
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Adding a new page/component
1. [Step 1]
2. [Step 2]
3. [Step 3]

### [Other common task]
1. [Step 1]
2. [Step 2]

## Testing Strategy

- [Test framework]
- [Test file location]
- [Coverage requirements]
- [How to run tests]

**See ADR-### for full testing strategy**

## Deployment

- [Hosting platform]
- [Deployment trigger - e.g., push to main]
- [Environment variables setup]
- [Migration handling]

**See ADR-### for deployment strategy**

## Workflow Overrides

**This project overrides workspace defaults**:

### Branching Strategy
<!-- If different from workspace GitFlow:
- Use [trunk-based / GitHub Flow / custom]
- Branch naming: [pattern]
- PR requirements: [requirements]
-->
Uses workspace default (GitFlow: main + develop + feature/###-slug)

### Commit Message Format
<!-- If different from workspace default:
- Format: [your format]
- Example: [example]
-->
Uses workspace default (Conventional Commits with Claude co-author)

### Testing Requirements
<!-- If different from workspace default:
- Coverage threshold: [percentage]
- Required test types: [unit/integration/e2e]
- CI enforcement: [rules]
-->
Uses workspace default (80% coverage, enforced in CI)

### Documentation Standards
<!-- If different from workspace default:
- ADR format: [custom format]
- Code comments: [style]
- API docs: [approach]
-->
Uses workspace default

**NOTE**: Project overrides take precedence over workspace defaults in root CLAUDE.md.

## AI Agent Notes

When implementing features:
1. **Read this file first** for project-specific context AND overrides
2. **Check ADRs** (`docs/adrs/`) for architecture decisions
3. **Follow existing patterns** - grep codebase for similar implementations
4. **Update docs** - Keep `data-model.md` and `architecture-overview.md` current
5. **Reference specs** - Planning docs live in `ideas/[project]/`

**Project-specific constraints:**
- [Constraint 1 - e.g., "No Docker, use venv"]
- [Constraint 2 - e.g., "HTMX over React"]
- [Constraint 3 - e.g., "Test coverage must stay above 80%"]

**Precedence for conflicting guidance:**
1. This file (project overrides)
2. Root CLAUDE.md (workspace defaults)
3. ADRs (architecture decisions)
