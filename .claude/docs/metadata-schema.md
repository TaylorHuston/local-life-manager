# Metadata Schema Documentation

All markdown files in the ideas repository should include YAML frontmatter for tracking, automation, and AI agent context.

## Purpose of Metadata

Metadata enables:
- **Dashboard generation**: Summary views of all ideas and their status
- **Staleness detection**: Identify documents that need updates
- **AI context**: Quick understanding without reading full documents
- **Validation tracking**: Monitor progress from hypothesis to validated
- **Cross-referencing**: Link related ideas and documents
- **Automated tooling**: Build scripts and agents that understand project state

## Common Fields (All Documents)

These fields should appear in ALL documents:

### `idea`
**Type**: String
**Required**: Yes
**Example**: `"Coordinatr"` or `"YourBench"`
**Purpose**: Links document to parent idea, must be consistent across all files in an idea

### `document`
**Type**: String (controlled vocabulary)
**Required**: Yes
**Values**:
- `"readme"` - README.md overview
- `"project-brief"` - Main project brief
- `"critique"` - Idea Critic output
- `"elevator-pitch"` - Pitch document
- `"competitive-analysis"` - Market research
- `"pricing-strategy"` - Pricing document
- `"technical-architecture"` - Tech architecture
- `"go-to-market"` - Launch strategy
- `"spec"` - Protocol specification (lives in spaces/)
- `"support-doc"` - Misc docs/ files
- `"note"` - Notes/ files
- `"notes-index"` - Notes overview
- `"docs-index"` - Docs overview

### `created`
**Type**: Date (YYYY-MM-DD)
**Required**: Yes
**Example**: `"2025-01-15"`
**Purpose**: Track when document was first created

### `updated`
**Type**: Date (YYYY-MM-DD)
**Required**: Yes
**Example**: `"2025-01-20"`
**Purpose**: Track last modification, helps identify stale documents

## README.md Metadata

```yaml
---
idea: "ProjectName"
status: "concept" | "active-planning" | "pre-mvp" | "mvp-in-progress" | "shelved" | "graduated"
stage: "brainstorm" | "validation" | "planning" | "building" | "launched"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
confidence: 1-10
priority: "high" | "medium" | "low"
tags: ["tag1", "tag2"]
related_ideas: ["idea-name-1", "idea-name-2"]
---
```

### `status`
**Type**: Enum
**Values**:
- `concept` - Initial idea capture
- `active-planning` - Detailed planning in progress
- `pre-mvp` - Ready to build, planning complete
- `mvp-in-progress` - Actively building MVP
- `shelved` - Decided not to pursue (for now)
- `graduated` - Moved to its own repository

### `stage`
**Type**: Enum
**Values**:
- `brainstorm` - Rough thinking
- `validation` - Testing assumptions
- `planning` - Detailed planning
- `building` - Implementation
- `launched` - Live and active

### `confidence`
**Type**: Integer (1-10)
**Example**: `7`
**Purpose**: How confident are you this is a good idea?

### `priority`
**Type**: Enum
**Values**: `high`, `medium`, `low`
**Purpose**: Relative priority among your ideas

### `tags`
**Type**: Array of strings
**Example**: `["b2b", "saas", "ai", "developer-tools"]`
**Purpose**: Categorization for filtering and search

### `related_ideas`
**Type**: Array of strings
**Example**: `["coordinatr", "techvetted"]`
**Purpose**: Cross-reference related or competing ideas

## project-brief.md Metadata

```yaml
---
idea: "ProjectName"
document: "project-brief"
version: "1.0"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
completeness: 0-100
validation_status: "hypothesis" | "researched" | "user-tested" | "validated"
next_review: "YYYY-MM-DD"
---
```

### `version`
**Type**: String (semantic versioning)
**Example**: `"1.0"`, `"2.1"`
**Purpose**: Track major pivots or revisions

### `completeness`
**Type**: Integer (0-100)
**Example**: `75`
**Purpose**: Percentage of sections filled out

### `validation_status`
**Type**: Enum
**Values**:
- `hypothesis` - Unvalidated assumptions
- `researched` - Desktop research done
- `user-tested` - Validated with target users
- `validated` - Proven with real usage/payment

### `next_review`
**Type**: Date (YYYY-MM-DD)
**Example**: `"2025-03-01"`
**Purpose**: When to revisit assumptions

## critique.md Metadata

```yaml
---
idea: "ProjectName"
document: "critique"
critique_date: "YYYY-MM-DD"
critic_version: "1.0"
brief_version: "1.0"
severity_score: 1-10
addressed: false
---
```

### `critique_date`
**Type**: Date
**Purpose**: When critique was generated

### `critic_version`
**Type**: String
**Purpose**: Version of Idea Critic agent used

### `brief_version`
**Type**: String
**Purpose**: Which version of project-brief was critiqued (to detect staleness)

### `severity_score`
**Type**: Integer (1-10)
**Purpose**: How harsh were the criticisms?

### `addressed`
**Type**: Boolean
**Purpose**: Have we addressed the critique points?

## competitive-analysis.md Metadata

```yaml
---
idea: "ProjectName"
document: "competitive-analysis"
research_date: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
competitors_analyzed: 5
market_maturity: "nascent" | "growing" | "mature" | "declining"
needs_refresh_by: "YYYY-MM-DD"
---
```

### `research_date`
**Type**: Date
**Purpose**: When initial research was conducted

### `competitors_analyzed`
**Type**: Integer
**Purpose**: How many competitors were analyzed

### `market_maturity`
**Type**: Enum
**Values**: `nascent`, `growing`, `mature`, `declining`
**Purpose**: Market lifecycle stage

### `needs_refresh_by`
**Type**: Date
**Purpose**: Markets change - when to re-research

## Protocol Spec Metadata

Protocol specs live in `spaces/[project]/docs/specs/` alongside code.

### docs/specs/README.md

```yaml
---
project: "ProjectName"
document: "spec"
version: "1.0.0"
source: "self-authored" | "https://github.com/..."
last_synced: "YYYY-MM-DD"  # if imported
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
---
```

### `version`
**Type**: String (semantic versioning)
**Example**: `"1.0.0"`
**Purpose**: Track spec evolution (patch: clarifications, minor: new features, major: breaking changes)

### `source`
**Type**: String
**Values**: `"self-authored"` or URL to upstream spec
**Purpose**: Track origin for syncing

## Notes Metadata

```yaml
---
idea: "ProjectName"
document: "note"
note_type: "brainstorm" | "pivot" | "research" | "meeting" | "decision"
date: "YYYY-MM-DD"
obsolete: false
---
```

### `note_type`
**Type**: Enum
**Values**: `brainstorm`, `pivot`, `research`, `meeting`, `decision`
**Purpose**: Categorize note type

### `obsolete`
**Type**: Boolean
**Purpose**: Mark old notes without deleting history

## Optional Strategic Files Metadata

### pricing-strategy.md

```yaml
---
idea: "ProjectName"
document: "pricing-strategy"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
pricing_model: "subscription" | "usage-based" | "freemium" | "one-time" | "hybrid"
validated: false
---
```

### technical-architecture.md

```yaml
---
idea: "ProjectName"
document: "technical-architecture"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
architecture_status: "proposed" | "validated" | "implemented"
tech_stack_decided: false
---
```

### go-to-market.md

```yaml
---
idea: "ProjectName"
document: "go-to-market"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
launch_date: "YYYY-MM-DD"
strategy_validated: false
---
```

## Validation Rules

### Required Fields by Document Type

**All documents**:
- `idea`
- `document`
- `created`

**README.md**:
- Also requires: `status`, `updated`

**project-brief.md**:
- Also requires: `version`, `updated`

### Controlled Vocabularies

Always use exact enum values (case-sensitive) for:
- `status`
- `stage`
- `priority`
- `validation_status`
- `market_maturity`
- `note_type`

### Date Format

Always use ISO 8601 format: `YYYY-MM-DD`
- ✅ `"2025-01-15"`
- ❌ `"01/15/2025"`
- ❌ `"15-Jan-2025"`

## Future Tooling Possibilities

With standardized metadata, we can build:

1. **Dashboard generator**: `/project-status` shows all ideas and status
2. **Staleness checker**: `/docs --stale` finds outdated docs
3. **Validation tracker**: `/validate-idea` checks documentation completeness
4. **Critique tracker**: `/critique` generates and tracks critiques

Most of these are now implemented as skills.

## Best Practices

1. **Keep metadata updated**: When you edit a file, update the `updated` field
2. **Be honest with confidence**: Low confidence is valuable information
3. **Use tags consistently**: Establish a tag vocabulary and stick to it
4. **Review next_review dates**: Set realistic review cadences
5. **Mark obsolete, don't delete**: Keep history by marking `obsolete: true`
6. **Version on pivots**: Increment `version` when fundamentally changing direction
