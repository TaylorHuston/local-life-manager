# Skills Catalog

This directory contains 49 skills (slash commands) that extend Claude Code's capabilities for life management, project development, learning, and content processing.

## Quick Reference

| Skill | Description |
|-------|-------------|
| `/brief` | Create or update project brief through interactive discovery |
| `/critique` | Challenge idea assumptions with skeptical VC-style evaluation |
| `/validate-idea` | Validate idea/project structure and readiness for next phase |
| `/validate-space` | Validate project space structure, boilerplate docs, and consistency |
| `/spec` | Manage protocol/standard specifications that define what a system must do |
| `/research` | Deep research on a topic with persistent documentation |
| `/issue` | Create standalone work items (TASK, BUG, or SPIKE) with AI-assisted type detection |
| `/plan` | Create PLAN.md file with phase-based breakdown for issues |
| `/adr` | Create Architecture Decision Records through interactive conversation |
| `/ui-design` | Create HTML UI mockups stored in ideas/[project]/docs/ui-designs/ |
| `/implement` | Execute plan phases, writing code in spaces/ while tracking in ideas/ |
| `/advise` | Interactive conversational guidance - you implement with step-by-step advice |
| `/teach` | Deep pedagogical guidance - learn technology by doing with Socratic teaching |
| `/troubleshoot` | Systematic debugging with 5-step loop |
| `/worklog` | Add timestamped work log entries to track progress and decisions |
| `/quality` | Comprehensive code quality assessment |
| `/security-audit` | Comprehensive security audit using multiple agents |
| `/validate-spec` | Validate spec completeness and implementation compliance |
| `/commit` | Create git commits with conventional message format |
| `/complete` | Complete task: validate, document, review, commit, and merge |
| `/sanity-check` | Step back, reflect on current work, validate direction |
| `/project-status` | Enhanced project status dashboard with intelligent context analysis |
| `/projects-quick` | Quick overview of all projects (lightweight, Haiku-powered) |
| `/whats-next` | Quick prioritization of what to work on |
| `/good-morning` | Morning routine check-in |
| `/daily-review` | Complete daily journal review |
| `/daily-journal` | Daily journal management (parent skill) |
| `/quick-journal` | Quick update to today's journal without full review |
| `/weekly-review` | Weekly review and planning session |
| `/learning-system` | Structured learning and spaced repetition system (parent skill) |
| `/start-session` | Start a new learning session on a topic |
| `/end-session` | End the current learning session |
| `/log-session` | Log entries to the current learning session |
| `/review-session` | Retrieval practice session to test retention |
| `/flashcards` | Generate spaced repetition flashcards from notes or topics |
| `/study-notes` | Create comprehensive study notes on a topic |
| `/youtube-catchup` | Fetch and summarize latest videos from priority YouTube channels |
| `/video-summarize` | Summarize a single YouTube video and create a note |
| `/rss-catchup` | Fetch and summarize latest articles from RSS feeds |
| `/synthesize` | Synthesize information across multiple sources into structured documents |
| `/docs` | Documentation health check and maintenance |
| `/readmes` | Check all READMEs for accuracy and consistency |
| `/process-inbox` | Process notes in inbox folder |
| `/refresh` | Silently refresh AI context by reading project configuration |
| `/spaces-sync` | Sync spaces/ directory with Projects Index |
| `/improve-processes` | Reflect on session and suggest improvements to tooling |
| `/life-planning` | Cross-repo life and project planning |

---

## 1. Project Foundation

Skills for starting and validating project ideas.

### `/brief`
**Create or update project brief through interactive discovery**

Interactive conversation to define project vision, problem, audience, and scope.

```bash
/brief                           # Interactive discovery for current or new project
/brief --project coordinatr      # Brief for specific project
/brief --review                  # Analyze existing brief (no edits)
/brief --force                   # Start from scratch
```

**Use when:** Starting any new idea, revisiting after time away, or when vision feels unclear.

### `/critique`
**Challenge idea assumptions with skeptical VC-style evaluation**

Skeptical evaluation focusing on market, technical, and business viability.

```bash
/critique                        # Critique current project
/critique --project coordinatr   # Specific project
/critique --focus market         # Market validation focus
/critique --focus technical      # Technical feasibility focus
/critique --focus business       # Business model focus
```

**Use when:** Before significant time investment to validate the idea is worth pursuing.

### `/validate-idea`
**Validate idea/project structure, documentation completeness, and readiness**

Checks documentation structure and phase readiness without edits.

```bash
/validate-idea coordinatr        # Validate specific idea
/validate-idea yourbench         # Check another project
```

**Use when:** Checking if project documentation is complete before next phase.

### `/validate-space`
**Validate project space structure, boilerplate docs, and consistency with ideas/**

Checks spaces/[project]/ for required files, version consistency, and cross-references with ideas/.

```bash
/validate-space leaf-nextjs-convex   # Validate specific space
/validate-space coordinatr           # Another project
```

**Use when:** After scaffolding, before implementation, after dependency upgrades, monthly maintenance.

---

## 2. Project Planning

Skills for defining what to build and how.

### `/spec`
**Manage protocol/standard specifications that define what a system must do**

Import external specs (LEAF, OAuth, etc.) or create self-authored protocol specs. Specs live with code in `spaces/[project]/docs/specs/`.

```bash
/spec                            # Show current project's spec status
/spec --import <url>             # Import external spec (GitHub, raw URL)
/spec --init                     # Create new protocol spec for project
/spec --sync                     # Sync imported spec with upstream
/spec --section <name>           # Show specific section of spec
```

**Use when:** Defining requirements before implementation, importing external standards.

### `/research`
**Deep research on a topic, creating persistent documentation**

Creates comprehensive research documents (20-30+ sources → 3-5 pages). Uses research-specialist agent with Context7 and WebSearch.

```bash
/research "authentication patterns for multi-tenant SaaS"
/research "Jira vs Linear competitive analysis"
/research "WebSocket vs SSE trade-offs"
```

**Output:** `ideas/[project]/notes/research/`, `shared/docs/research/`, or `resources/research/`

**Use when:** Technology decisions, competitive analysis, complex topics requiring deep investigation.

### `/issue`
**Create standalone work items (TASK, BUG, or SPIKE) with AI-assisted type detection**

Auto-detects type from description. Links to spec sections via `implements:` field.

```bash
/issue                                    # Start conversation
/issue "Implement authentication"         # AI detects: TASK
/issue "Compare GraphQL vs REST"          # AI detects: SPIKE
/issue "Broken link in project-brief"     # AI detects: BUG
/issue --project coordinatr               # Create for specific project
```

**Creates:** `ideas/[project]/issues/###-name/TASK.md` (or BUG.md, SPIKE.md)

**Use when:** Need to track work that needs doing, exploration needed, or something broken.

### `/plan`
**Create PLAN.md file with phase-based breakdown for issues**

Breaks work into logical phases with checkpoints. Validates library documentation with Context7.

```bash
/plan 001                        # Create plan for issue 001
/plan 001 --project coordinatr   # Explicit project
/plan SPIKE-003                  # Plan for a spike
/plan 003 --second-opinion       # Get peer review from Gemini CLI
```

**Creates:** `ideas/[project]/issues/###-name/PLAN.md`

**Use when:** After creating an issue, to break down work into executable phases.

### `/adr`
**Create Architecture Decision Records through interactive conversation**

Documents technology choices, architecture patterns, third-party selections. Lives with code.

```bash
/adr                                      # Start conversation
/adr "database selection for coordinatr"  # Provide topic
```

**Creates:** `spaces/[project]/docs/project/adrs/NNNN-title.md`

**Use when:** Making technology/framework selections, architecture patterns, third-party service decisions.

### `/ui-design`
**Create HTML UI mockups stored in ideas/[project]/docs/ui-designs/**

Creates self-contained HTML prototypes. Can generate multiple variants in parallel.

```bash
/ui-design yourbench "login screen"
/ui-design yourbench "dashboard" --variants 3
/ui-design coordinatr "project list" --tech shadcn
/ui-design yourbench list                  # Show existing designs
```

**Use when:** Designing interfaces before implementation, exploring UI variations.

---

## 3. Project Implementation

Skills for building and debugging.

### `/implement`
**Execute plan phases, writing code in spaces/ while tracking in ideas/**

Agent coordination based on phase type (frontend, backend, database, tests). Creates worklog entries.

```bash
/implement yourbench YB-2 1.1     # Execute phase 1.1 of issue YB-2
/implement yourbench YB-2 --next  # Auto-find next uncompleted phase
/implement yourbench --next       # Auto-detect issue + next phase
/implement coordinatr 003 --full  # Execute all remaining phases
```

**Use when:** Ready to write code from a plan.

### `/advise`
**Interactive conversational guidance - you implement with step-by-step advice**

Explains what to do, answers questions, checks your work. Medium-paced, task-focused.

```bash
/advise 001              # Guide through issue 001
/advise yourbench 001    # Explicit project
/advise 001 --phase 2.1  # Start at specific phase
```

**Use when:** Know the stack, need guidance on THIS task, want to maintain control.

### `/teach`
**Deep pedagogical guidance - learn technology by doing with Socratic teaching**

Line-by-line explanations with WHY not just HOW. Frequent comprehension checks.

```bash
/teach 001              # Learn through issue 001
/teach yourbench 001    # Explicit project
/teach 001 --phase 2.1  # Start at specific phase
```

**Comparison:**
| Aspect | /implement | /advise | /teach |
|--------|------------|---------|--------|
| Who codes | AI | You | You |
| Speed | Fast | Medium | Slower |
| Depth | Task completion | Task guidance | Conceptual learning |

**Use when:** Learning new framework, want to understand deeply WHY not just HOW.

### `/troubleshoot`
**Systematic debugging with 5-step loop**

Research → Hypothesize → Implement → Test → Document. One hypothesis at a time. Liberal debug logging.

```bash
/troubleshoot yourbench "tests failing after auth changes"
/troubleshoot yourbench 001       # Debug in context of issue
/troubleshoot coordinatr          # General debugging session
```

**Use when:** Encountering bugs, test failures, or unexpected behavior.

### `/worklog`
**Add timestamped work log entries to track progress and decisions**

JSON-based entries with types: manual, decision, gotcha, handoff, phase, blocker.

```bash
/worklog yourbench YB-2 "Added login button"
/worklog yourbench YB-2 --decision "Using Clerk for auth"
/worklog yourbench YB-2 --gotcha "Token refresh needs cleanup"
/worklog coordinatr 003 --handoff code-reviewer "Ready for review"
/worklog yourbench YB-2 --state              # Show current state
```

**Use when:** Documenting work, decisions, gotchas, agent handoffs.

---

## 4. Project Quality & Completion

Skills for ensuring quality and finishing work.

### `/quality`
**Comprehensive code quality assessment in spaces/[project]/**

Multi-agent analysis (code, security, performance, testing). Scoring system.

```bash
/quality yourbench                  # Full assessment
/quality yourbench --focus security # Security-focused
/quality coordinatr --focus testing # Test coverage focus
```

**Use when:** Before commits, merges, or releases to ensure consistent quality.

### `/security-audit`
**Comprehensive security audit of codebase using multiple agents**

5 agents run in parallel (Auth, Input, Crypto, Config, Dependencies). OWASP Top 10 coverage.

```bash
/security-audit yourbench           # Full security review
/security-audit coordinatr          # Audit specific project
```

**Use when:** Before production deployments, after major features, monthly reviews.

### `/validate-spec`
**Validate spec completeness and implementation compliance**

Pre-implementation: checks structure, scenarios, metrics. Post-implementation: verifies test coverage, metrics.

```bash
/validate-spec SPEC-001              # Auto-detect mode
/validate-spec SPEC-001 --pre        # Pre-implementation validation
/validate-spec SPEC-001 --post       # Post-implementation compliance
```

**Use when:** Before approval or before completion to verify spec compliance.

### `/commit`
**Create git commits in spaces/[project]/ with conventional message format**

Auto-detects changes. Runs quality checks unless `--no-verify`. Conventional commit format.

```bash
/commit yourbench                     # Interactive commit
/commit yourbench "feat: add auth"    # Direct with message
/commit coordinatr --amend            # Amend last commit (safety checks)
/commit yourbench "fix: typo" --no-verify  # Skip hooks
```

**Use when:** Saving progress with quality checks and proper commit messages.

### `/complete`
**Complete task: validate, document, review, commit, and merge to develop**

Validates PLAN completion and spec compliance. Updates all documentation. Runs code review + security audit.

```bash
/complete careerbrain 002         # Complete specific issue
/complete careerbrain             # Complete current/active issue
```

**Use when:** All implementation is done and ready to finalize.

---

## 5. Development Workflows

Skills for staying on track during work.

### `/sanity-check`
**Step back, reflect on current work, validate direction and alignment**

Uses sequential thinking to reflect. Checks alignment with vision, brief, critique. Categorizes findings.

```bash
/sanity-check                        # Reflect on current work
/sanity-check --project coordinatr   # Focus on specific project
```

**Use when:** Complexity increasing, feeling uncertain, before major decisions, something feels off.

### `/project-status`
**Enhanced project status dashboard with intelligent context analysis**

Scans ideas/, docs/specs/, issues/. Analyzes dependencies and blockers. Shows branch status.

```bash
/project-status                       # Overview of all projects
/project-status --project coordinatr  # Focus on one project
/project-status --detailed            # Comprehensive analysis
```

**Use when:** Session start context, weekly reviews, seeing what needs attention.

### `/projects-quick`
**Quick overview of all projects (lightweight, Haiku-powered)**

Reads project index and README files. Quick stats on open issues.

```bash
/projects-quick  # Show status of all projects
```

**Triggers on:** "project status", "show projects", "what projects"

### `/whats-next`
**Quick prioritization of what to work on**

Checks learning reviews, today's highlight, project status. Prioritization framework.

```bash
/whats-next  # Get quick recommendation
```

**Triggers on:** "what's next", "what should I do", "prioritize", "what now"

---

## 6. Daily & Weekly Routines

Skills for daily and weekly rhythms.

### `/good-morning`
**Morning routine check-in**

Checks yesterday's journal, sets up today, shows learning reviews due.

```bash
/good-morning  # Morning check-in
```

**Triggers on:** "good morning", "morning", "start my day"

### `/daily-review`
**Complete daily journal review**

Fills in journal sections (Work, Personal, Study). Pulls GitHub commits. Reviews highlight.

```bash
/daily-review  # Evening review
```

**Triggers on:** "daily review", "end of day", "journal review"

### `/daily-journal`
**Daily journal management (parent skill)**

Entry point for all daily journal workflows.

| Subcommand | Purpose |
|------------|---------|
| `/good-morning` | Morning check-in |
| `/daily-review` | Evening review |
| `/quick-journal [entry]` | Quick update |

### `/quick-journal`
**Quick update to today's journal without full review**

Adds bullet point to appropriate section.

```bash
/quick-journal "finished AWS EFS module"
```

**Triggers on:** "log this", "add to journal", "I just did"

### `/weekly-review`
**Weekly review and planning session**

Reviews past week (journal, GitHub, learning). Plans next week with daily highlights.

```bash
/weekly-review  # Weekly review and planning
```

**Triggers on:** "weekly review", "plan my week", "Sunday planning"

---

## 7. Learning System

Skills for structured learning and knowledge retention.

### `/learning-system`
**Structured learning and spaced repetition system (parent skill)**

Entry point for all learning workflows.

| Subcommand | Purpose |
|------------|---------|
| `/start-session [topic]` | Begin teaching session |
| `/end-session` | End current session |
| `/log-session` | Log entries mid-session |
| `/review-session [topic]` | Retrieval practice (test retention) |
| `/flashcards [file/topic]` | Generate flashcards |
| `/study-notes [topic]` | Create comprehensive notes |

### `/start-session`
**Start a new learning session on a topic**

Checks for topics due for review. Retrieval warm-up if topic covered before.

```bash
/start-session "AWS EFS"
/start-session /path/to/notes.md
```

**Triggers on:** "teach me", "let's learn", "start session", "study [topic]"

### `/end-session`
**End the current learning session**

Generates summary. Updates learning plan. Adjusts proficiency levels.

```bash
/end-session
```

**Triggers on:** "end session", "done learning", "finish studying"

### `/log-session`
**Log entries to the current learning session**

Saves progress mid-session. Captures concepts, corrections, elaborations.

```bash
/log-session
```

**Triggers on:** "log this", "save progress"

### `/review-session`
**Retrieval practice session to test retention on a topic**

Tests what you remember (NOT teaching). Logs confidence vs accuracy.

```bash
/review-session "AWS EFS"
```

**Triggers on:** "quiz me", "test my knowledge", "what do I remember"

### `/flashcards`
**Generate spaced repetition flashcards from notes or topics**

Supports multiple formats (::, :::, ;;, cloze deletions). For Obsidian Spaced Repetition plugin.

```bash
/flashcards /path/to/notes.md
/flashcards "AWS EFS concepts"
```

**Triggers on:** "flashcards", "make cards", "spaced repetition"

### `/study-notes`
**Create comprehensive study notes on a topic**

Well-structured with tables, callouts, examples. Related links to existing notes.

```bash
/study-notes "AWS EFS" "my-vault/06 Knowledge Base/AWS/"
```

**Triggers on:** "study notes", "create notes", "document [topic]"

---

## 8. Content Processing

Skills for consuming and synthesizing content.

### `/youtube-catchup`
**Fetch and summarize latest videos from priority YouTube channels**

Uses coordinator + Haiku subagents pattern. Processes 4-6 videos in parallel.

```bash
/youtube-catchup  # Process new videos from configured channels
```

**Config:** `.claude/skills/youtube-catchup/references/channels.json`

**Triggers on:** "youtube catchup", "video catchup", "check youtube"

### `/video-summarize`
**Summarize a single YouTube video and create a note**

Fetches metadata and transcript. Creates summary note with tags.

```bash
/video-summarize https://www.youtube.com/watch?v=abc123
/video-summarize abc123 "Tech Talks"
```

**Triggers on:** "summarize this video", "video summary", YouTube URLs

### `/rss-catchup`
**Fetch and summarize latest articles from RSS feeds**

Processes feeds since last run. Creates article notes with bullet summaries.

```bash
/rss-catchup  # Process new articles from feeds
```

**Config:** `.claude/skills/rss-catchup/references/feeds.json`

**Triggers on:** "rss catchup", "blog catchup", "check feeds"

### `/synthesize`
**Synthesize information across multiple sources into structured documents**

Coordinator + Haiku extractors for parallel processing (6-10 sources per batch). Auto-discovers related sources.

```bash
/synthesize adhd                      # Continue processing
/synthesize list                      # Show all syntheses
/synthesize new "ADHD Medications"    # Create new
/synthesize add adhd path/to/note.md  # Add sources
/synthesize update adhd               # Scan for new sources
```

**Output:** `my-vault/06 Knowledge Base/Synthesis/[Topic]/`

**Triggers on:** "synthesize", "synthesis", "research [topic]"

---

## 9. Documentation & Maintenance

Skills for keeping documentation healthy.

### `/docs`
**Documentation health check and maintenance across all ideas**

Health scoring by project. Validates links. Finds stale documents.

```bash
/docs --health                   # Overall health report
/docs --validate                 # Check broken links
/docs --stale                    # Find outdated docs
/docs --sync                     # Sync CLAUDE.md with project state
/docs --project coordinatr       # Focus on specific project
```

**Use when:** Periodic maintenance, finding gaps, keeping docs accurate.

### `/readmes`
**Check all READMEs for accuracy and consistency across the meta-repo**

Reviews all README.md files in ideas/. Checks status, dates, links, structure.

```bash
/readmes    # Review and update all READMEs
```

**Use when:** After major updates, monthly maintenance.

### `/process-inbox`
**Process notes in inbox folder**

Helps organize captured notes. Suggests destinations based on content.

```bash
/process-inbox  # Process my-vault inbox
```

**Triggers on:** "process inbox", "organize notes", "inbox zero"

---

## 10. System Utilities

Skills for system management and meta-work.

### `/refresh`
**Silently refresh AI context by reading project configuration**

Reads core configuration (CLAUDE.md, about-me.md). Gets recent git activity. Silent operation.

```bash
/refresh  # Silent context reload
```

**Use when:** Starting new conversation, after context loss, before major tasks.

### `/spaces-sync`
**Sync spaces/ directory with Projects Index**

Checks status of all repos and branches. Safe operations (no force push).

```bash
/spaces-sync              # Check status
/spaces-sync --pull       # Pull updates
/spaces-sync --push       # Push local commits
/spaces-sync --clone      # Clone missing repos
```

### `/improve-processes`
**Reflect on session and suggest improvements to tooling**

Analyzes conversation for friction points. Suggests improvements.

```bash
/improve-processes                    # Reflect on session
/improve-processes --focus agents     # Focus on agent improvements
/improve-processes --focus workflows  # Focus on workflow improvements
```

### `/life-planning`
**Cross-repo life and project planning**

Unified view across personal (my-vault), projects (ideas/), and learning.

```bash
/life-planning  # Overview and planning
```

**Triggers on:** "plan my week", "what should I work on", "prioritize"

---

## Workflow Examples

### New Project Flow
```
/brief → /critique → /research → /spec → /issue → /plan → /implement → /commit → /complete
```

### Learning Flow
```
/start-session → [teach conversationally] → /log-session → /end-session
Later: /review-session → /flashcards
```

### Daily Flow
```
Morning: /good-morning
Evening: /daily-review
Weekly: /weekly-review
```

### Content Processing Flow
```
/youtube-catchup → [creates notes] → /synthesize add → /synthesize [topic]
/rss-catchup → [creates notes] → /synthesize add → /synthesize [topic]
```

### Quality Assurance Flow
```
/implement → /troubleshoot (if needed) → /quality → /security-audit → /commit → /complete
```

---

## Architecture Patterns

### Coordinator + Subagent Pattern
Some skills use parallel subagents for efficiency:

- **/synthesize**: Haiku extractors process 6-10 sources in parallel
- **/youtube-catchup**: Haiku summarizers handle 4-6 videos in parallel
- **/implement**: Specialist agents for different phase types
- **/quality**: Multiple agents analyze different dimensions

Provides ~3x throughput improvement for batch operations.

### Agent Specialization
Skills invoke specialized agents based on task type:

- **research-specialist**: Deep research with 20-30+ sources
- **brief-strategist**: Interactive project discovery
- **idea-critic**: Skeptical VC-style evaluation
- **ui-ux-designer**: Interface mockup generation
- **frontend-specialist**, **backend-specialist**, **database-specialist**: Domain implementation
- **code-reviewer**, **security-auditor**, **test-engineer**: Quality assurance

---

## Skill File Structure

Each skill has its own directory:
```
skills/
├── skill-name/
│   ├── SKILL.md           # Skill definition (required)
│   └── references/        # Supporting docs (optional)
│       └── schema.md
```

### SKILL.md Frontmatter

```yaml
---
name: skill-name
description: "One-line description"
model: claude-opus-4-5-20251101   # or claude-sonnet-4-20250514, claude-haiku-4-5-20251001
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
argument-hint: [optional arguments]
---
```

---

## Best Practices

1. **Start with /brief** for new projects before diving into implementation
2. **Run /critique** before significant time investment to validate ideas
3. **Use /spec** to define requirements before creating tasks
4. **Link issues to specs** via `implements:` field for traceability
5. **Document as you go** with /worklog entries
6. **Run quality checks** (/quality, /security-audit) before completion
7. **Complete properly** with /complete to update all documentation
8. **Review regularly** - /daily-review, /weekly-review for reflection
9. **Learn actively** - /start-session with retrieval warm-ups
10. **Synthesize knowledge** - use /synthesize for deep understanding of topics

---

## Configuration Files

Skills read from several configuration files:

| File | Purpose |
|------|---------|
| `.claude/skills/[skill]/SKILL.md` | Skill definitions |
| `.claude/skills/[skill]/references/` | Skill-specific configuration |
| `.claude/learning-sessions/learning-plan.json` | Learning system state |
| `.claude/skills/youtube-catchup/references/channels.json` | YouTube channels |
| `.claude/skills/rss-catchup/references/feeds.json` | RSS feeds |
| `.claude/skills/synthesize/references/queues/` | Synthesis queues |
