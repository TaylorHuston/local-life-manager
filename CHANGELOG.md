# Changelog

All notable changes to the Life Framework will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [0.2.0] - 2026-01-20

### Added
- `/debrief` skill - End-of-session reflection for extracting memories and suggesting updates to about-me.md and CLAUDE.md
- `/git-sync` skill - Renamed from spaces-sync for clarity

### Changed
- `/refresh` now reads about-taylor.md (profile) and last 3 days of memories for better context loading
- `/good-morning` updated to use vault template at `my-vault/09 System/Templates/Daily Template.md`
- `/youtube-catchup` and `/rss-catchup` now deduplicate by checking for existing URLs before creating notes
- Content capture skills now write to `07 Knowledge Base/Capture/` (was 06)

### Fixed
- Catchup skills no longer create duplicate notes when run multiple times

### Removed
- `/spaces-sync` (renamed to `/git-sync`)

---

## [0.1.0] - 2026-01-18

### Added
- Initial framework release
- 49 custom Claude Code skills
- 26 specialized agent definitions
- Project planning templates (ideas/)
- Code workspace structure (spaces/)
- Example project scaffolding

### Changed

### Fixed

### Removed
