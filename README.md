# 

A framework for AI-assisted life and project management using Claude Code. This is still fairly bespoke to my workflows and things, but should be a starting point for you to tweak for yourself.

## What This Is

A structured approach to:
- **Project planning** with briefs, specs, and issue tracking
- **Personal knowledge management** with daily journals and learning systems
- **AI-powered workflows** via 49 custom Claude Code skills
- **Multi-project coordination** with shared standards and templates

## Prerequisites

- [Claude Code](https://claude.ai/code) CLI installed
- [Obsidian](https://obsidian.md/) for personal knowledge management
- Git

## Directory Structure

```
life-framework/
├── .claude/
│   ├── skills/              # 49 custom Claude Code skills
│   ├── agents/              # 26 specialized agent definitions
│   ├── docs/                # System documentation
│   ├── memories/            # Persistent AI context about you (create this)
│   └── learning-sessions/   # Learning progress tracking (create this)
├── my-vault/                # Your Obsidian vault (clone/create here)
├── ideas/                   # Project planning (private strategy docs)
│   └── [project]/
│       ├── README.md
│       ├── project-brief.md
│       ├── specs/
│       ├── issues/
│       └── notes/
├── spaces/                  # Code repositories (each has own git)
│   └── [project]/
├── shared/
│   ├── templates/           # Project and doc templates
│   └── docs/                # Cross-project standards
├── CLAUDE.md                # AI instructions (customize this)
└── CHANGELOG.md
```

## Setup

### 1. Clone and Initialize

```bash
git clone https://github.com/YOU/life-framework.git
cd life-framework

# Create personal directories
mkdir -p .claude/memories .claude/learning-sessions
```

### 2. Set Up Your Obsidian Vault

Clone or create your Obsidian vault in the root:

```bash
# Option A: Clone existing vault
git clone https://github.com/YOU/my-vault.git my-vault

# Option B: Create new vault
mkdir my-vault
# Then open it in Obsidian to initialize
```

**Recommended vault structure:**
```
my-vault/
├── 01 Inbox/           # Capture location
├── 02 Calendar/        # Daily notes (YYYY-MM-DD.md)
├── 03 Tags/            # Tag index pages
├── 04 Personal/        # Personal notes
├── 05 Projects/        # Project notes
├── 06 Knowledge Base/  # Accumulated knowledge
└── 09 System/          # Templates
```

### 3. Create Your Context

Create `.claude/memories/about-me.md`:

```markdown
# About Me

## Profile
- **Name:** Your Name
- **Role:** What you do
- **Focus:** Current priorities

## Communication Preferences
- Style preferences
- What to avoid

## Key Accounts
- GitHub: https://github.com/you
- Other relevant links
```

Initialize the memories index:

```bash
echo '[]' > .claude/memories/index.json
```

### 4. Customize CLAUDE.md

Edit `CLAUDE.md` to:
- Update the overview with your context
- Add your projects to the Projects Index
- Adjust paths if your vault has different structure
- Add any personal preferences

### 5. Configure Personal Skills

These skills need your data:

**RSS Feeds** (`.claude/skills/rss-catchup/references/feeds.json`):
```json
{
  "feeds": [
    {"name": "Blog Name", "url": "https://example.com/feed.xml", "category": "tech"}
  ]
}
```

**YouTube Channels** (`.claude/skills/youtube-catchup/references/channels.json`):
```json
{
  "channels": [
    {"name": "Channel", "channel_id": "UC...", "priority": "high"}
  ]
}
```

## Usage

### Starting a Session

```bash
cd life-framework
claude
```

Then use skills like:
- `/good-morning` - Morning routine and planning
- `/daily-journal` - Update your daily note
- `/whats-next` - Prioritize what to work on

### Project Workflow

1. **Start an idea**: `/brief` - Interactive project brief creation
2. **Validate**: `/critique` - Skeptical evaluation
3. **Specify**: `/spec` - Write feature specifications
4. **Track work**: `/issue` - Create trackable work items
5. **Implement**: `/implement` - Execute with guidance
6. **Ship**: `/commit` - Quality commits

### Learning Workflow

1. **Start session**: `/start-session [topic]`
2. **Log progress**: `/log-session`
3. **Create cards**: `/flashcards`
4. **Review**: `/review-session`
5. **End**: `/end-session`

### Daily Workflow

| Time | Skill | Purpose |
|------|-------|---------|
| Morning | `/good-morning` | Review yesterday, plan today |
| During day | `/quick-journal` | Log activities |
| End of day | `/daily-review` | Fill in journal sections |
| Weekly | `/weekly-review` | Review week, plan next |

## Skills Reference

### Project Skills
| Skill | Purpose |
|-------|---------|
| `/brief` | Create project briefs through discovery |
| `/critique` | VC-style skeptical evaluation |
| `/spec` | Write feature specifications |
| `/issue` | Create work items (TASK/BUG/SPIKE) |
| `/plan` | Break issues into phases |
| `/implement` | Execute implementation plans |
| `/advise` | Get guidance without AI writing code |
| `/teach` | Deep learning with Socratic method |
| `/commit` | Create quality commits |
| `/complete` | Finalize and merge work |

### Quality Skills
| Skill | Purpose |
|-------|---------|
| `/quality` | Code quality assessment |
| `/security-audit` | Security review |
| `/validate-spec` | Check spec completeness |
| `/troubleshoot` | Systematic debugging |
| `/sanity-check` | Step back and validate direction |

### Personal Skills
| Skill | Purpose |
|-------|---------|
| `/daily-journal` | Manage daily entries |
| `/daily-review` | End of day journal completion |
| `/good-morning` | Morning routine |
| `/weekly-review` | Weekly planning |
| `/life-planning` | Cross-project prioritization |
| `/whats-next` | Quick prioritization |

### Learning Skills
| Skill | Purpose |
|-------|---------|
| `/learning-system` | Structured learning |
| `/start-session` | Begin learning session |
| `/end-session` | Complete session with summary |
| `/flashcards` | Generate spaced repetition cards |
| `/study-notes` | Create comprehensive notes |
| `/review-session` | Test retention |

### Content Skills
| Skill | Purpose |
|-------|---------|
| `/rss-catchup` | Summarize RSS feeds |
| `/youtube-catchup` | Summarize YouTube videos |
| `/video-summarize` | Summarize single video |
| `/synthesize` | Research synthesis |
| `/research` | Deep research with docs |

## Philosophy

### Planning vs Code
- `ideas/` contains strategy: briefs, specs, issues (private)
- `spaces/` contains code: each project is its own repo
- ADRs live with code, not in planning docs

### Memory is Persistent
Claude learns your preferences over time via `.claude/memories/`. The AI will proactively capture:
- Preferences you express
- Corrections you make
- Workflow insights
- Project decisions

### Skills are Workflows
Skills aren't just prompts—they're structured multi-step processes with:
- Clear triggers and entry points
- Reference materials
- Output formats
- Integration with your vault and repos

## Maintenance

- Update `CLAUDE.md` Projects Index when adding/archiving projects
- Review and prune `.claude/memories/` periodically
- Keep your vault's daily notes current
- Update skill configs as your feeds/channels change

## License

MIT
