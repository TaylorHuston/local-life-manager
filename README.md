# Local Life Manager

LLM. Get it? Because it uses an LLM to help manage your life?... I'll see myself out now.

A framework for AI-assisted life and project management using Claude Code. This is still very bespoke to my workflows, Obsidian vault layout, Obsidian plugins, etc, so you probably can't just clone it and start using it right away, but it should be enough of a starting point for you to tweak for yourself.

See: [I'm Letting Claude Manage My Life (Sort Of)](https://taylorhuston.me/2026/01/13/Claude-Life-Management.html) and [Local Life Management (LLM? Get It?)](https://taylorhuston.me/2026/01/21/Local-Life-Management.html)

## What This Is

A structured approach to:
- **Project planning** with briefs, specs, and issue tracking
- **Personal knowledge management** with daily journals and learning systems
- **AI-powered workflows** via 50 custom Claude Code skills
- **Multi-project coordination** with shared standards and templates

## Prerequisites

- [Claude Code](https://claude.ai/code) CLI installed
- [Obsidian](https://obsidian.md/) for personal knowledge management
- Git

## What Can It Do?

### Spec Driven Development
- Contains an updated version of the skills and workflows from my [Claude Code SDD Plugin](https://github.com/TaylorHuston/ai-toolkit).
- Skills to create detailed specs, plans, tasks and then implement those plans in a structured way.
- Also includes a "/teach" mode where the LLM will walk you through building the spec yourself, great for a truly personalized tutorial.

### Personal Tutor
- The LLM can create study sessions for you, tracking what topics you've already worked on.
- Help you study any topic you want, taking in your previous study sessions and existing notes into account.

### Summarize YouTube Channels and RSS Feeds
- Constantly find yourself drowning in all of the different things you feel like you need to watch and read to stay on top of things?
- The LLM can track a list of YouTube channels you want to follow, download the transcripts, and create summaries for each of them in your vault.
- The LLM can track a list of RSS feeds you want to follow, read the latest entries and create summaries for each article in your vaut.
- Then you can read these summaries and determine which ones are actually worth your time to go watch or read.

### Journal, Daily Review, Weekly Review
- Commands to help you keep track of your daily journal.
- Have it help you with your daily review each evening.
- Have it help you plan your day each morning.
- Have it help you reflect on the previous week and set goals for the upcoming week every Sunday.

_Note that a lot of this could still be considered a beta at best, this is definitely a work in progress. Skills and workflows are changing frequently, these instructions might not always be up to date, but you should be able to ask Claude itself what it can do in this project._

## Directory Structure

```
local-life-manager/
├── .claude/
│   ├── skills/              # 50 custom Claude Code skills
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
git clone https://github.com/TaylorHuston/local-life-manager.git
cd local-life-manager

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
├── 01 Inbox/           # Capture location for new notes
├── 02 Calendar/        # Daily notes (YYYY-MM-DD.md), weekly reviews (YYYY-Www.md)
├── 03 TaskNotes/       # Tasks (each task = note with #task tag)
├── 04 Tags/            # Tag index pages with Dataview queries
├── 05 Personal/        # Personal notes, decisions, career, health
├── 06 Projects/        # Active projects
├── 07 Knowledge Base/  # Courses, videos, tech notes
├── 08 AI Research/     # AI/ML research, experiments, agent patterns
└── 09 System/          # Templates, Classes, assets
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
cd local-life-manager
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

## Limitations and Future Plans

- It's entirely reliant on my workflows and Obsidian setup, I'd like to generalize it more.
- It's entirely based on Claude Code, I'd like to generalize it to work better with any LLM, including local ones, possible folding in my [Local Ollama Chatbot experiment](https://github.com/TaylorHuston/ollama-chat).
- The YouTube and RSS catchup skills both just store their state in a giant JSON file, which probably won't scale.
- As the size of the vault grows I might look into adding a RAG to help the LLM search through it easier.

## License

MIT
