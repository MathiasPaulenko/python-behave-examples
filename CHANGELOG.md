# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- Examples for the full `behave-*` ecosystem (21 libraries):
  `features/libraries/` demos for behave-kit, behave-data, behave-tables,
  behave-comments, behave-steplib, behave-priority, behave-retry and
  behave-model, wired together in `features/environment.py`.
- Dynamic `Examples` loaded from CSV via behave-data's
  `@load_examples:users_csv` tag (replaces the previous no-op approach).
- `behave.ini`: trace, sheets (CSV/XLSX/ODS) and file (TXT/DOCX/PDF)
  report formatters, behave-pool parallel runner alias, report userdata
  options.
- `behave_data.yml` (behave-data config), `behave.toml` (behave-kit env
  profiles), `pyproject.toml` (behave-runner/doctor/lint/format config).
- Community standards: LICENSE (MIT), CODE_OF_CONDUCT.md, CONTRIBUTING.md,
  SECURITY.md, SUPPORT.md, issue templates, PR template, CODEOWNERS,
  dependabot config, this CHANGELOG.
- `.gitignore` covering reports, caches, venvs, IDE and OS artifacts.

### Fixed

- Hook counters (`context.run_stats`) — attributes assigned inside a
  scenario layer were discarded; a shared dict now survives layer pops.
- `behave-data` dynamic Examples marked `table.modified` so scenario
  outlines rebuild after row injection.

### Changed

- Removed the `junit` formatter — behave 1.3 no longer ships it.
- Applied `behave-format` across all feature files.
