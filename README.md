# python-behave-examples

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![behave 1.3.3](https://img.shields.io/badge/behave-1.3.3-brightgreen.svg)](https://github.com/behave/behave)

A complete, self-contained [Behave](https://behave.readthedocs.io/) example suite
for Python (behave 1.3.x) — and a showcase for the whole `behave-*` library
ecosystem. It exercises every major Gherkin and Behave feature against small
in-memory domain objects and a real Flask REST API started in a background
thread — no external services needed.

## What's inside

| Feature file | Demonstrates |
|---|---|
| `features/calculator/calculator.feature` | `Background`, `Scenario Outline` with multiple `Examples` tables, tags |
| `features/string_utils/string_utils.feature` | Gherkin v6 `Rule` blocks, `Example` keyword, `Background` inside a Rule |
| `features/shopping_cart/shopping_cart.feature` | Data tables, DocStrings (`"""`), Scenario Outline with an embedded table |
| `features/async/async_steps.feature` | Async step definitions (`async def`, native behave 1.3.x support) |
| `features/api/users_api.feature` | REST API testing with `requests` against a live Flask server, pagination, CRUD |
| `features/api/csv_examples.feature` | Dynamic `Examples` loaded from an external CSV via **behave-data** |
| `features/libraries/kit.feature` | **behave-kit**: soft assertions, `env()`, `get_path`, `wait_until`, `@parameter_type`, `@scoped`, class-based steps |
| `features/libraries/tables.feature` | **behave-tables**: `wrap()`, `as_dicts`, `as_models`, `find_row`, `select`, `sort`, `to_csv`/`to_json` |
| `features/libraries/data.feature` | **behave-data**: typed table columns (`age:int`, `active:bool`, `created:date`), null resolution |
| `features/libraries/comments.feature` | **behave-comments**: `# @key value` metadata, `"""json` doc strings, comment-declared lifecycle hooks |
| `features/libraries/steplib.feature` | **behave-steplib**: ready-made API/data/IO/CLI steps — zero step code in this repo |
| `features/libraries/priority.feature` | **behave-priority**: `@priority(N)` ordering, `@critical`, execution report |
| `features/libraries/retry.feature` | **behave-retry**: `@flaky` tag filtering, `@retry:N` override, flakiness stats |
| `features/libraries/model.feature` | **behave-model**: `load_project()` meta-analysis of this very suite |

### Behave capabilities showcased

- **Gherkin v6 grammar**: `Rule`, `Example`, `Background` at feature and rule level
- **Scenario Outline** with multiple `Examples` tables
- **Data tables** (step-level) and **DocStrings**
- **Tags** (`@smoke`, `@negative`, `@unit`, `@integration`, `@api`, `@math`,
  `@docstring`, `@csv`) with tag-expression filtering (`default_tags = not @wip`
  in `behave.ini`)
- **Async steps** (`async def` step functions)
- **Custom type converters** (`register_type`, behave-kit `@parameter_type`)
- **Full lifecycle hooks**: `before_all` / `after_all`, `before_feature` / `after_feature`,
  `before_rule` / `after_rule`, `before_scenario` / `after_scenario`,
  `before_step` / `after_step`
- **`context.add_cleanup`** for stack-based teardown
- **In-memory Flask SUT** started in a background thread (no external services needed)
- **12 report formatters** wired in `behave.ini`: console, HTML, JSON, Markdown,
  Cucumber JSON, step catalogs, trace, CSV/XLSX, TXT/DOCX/PDF

## The behave-* ecosystem

Every library in the ecosystem is exercised either by a feature file, by
`features/environment.py` (hook wiring), or by configuration in this repo.

### Runtime libraries — wired in `features/environment.py`

| Library | What it adds | Example |
|---|---|---|
| [behave-kit](https://github.com/MathiasPaulenko/behave-kit) | `setup()`/`teardown()` wiring, env profiles (`behave.toml`), soft assertions, fixtures, step suggestions, context dump on failure | `features/libraries/kit.feature` |
| [behave-data](https://github.com/MathiasPaulenko/behave-data) | `setup_data()` + hooks: typed tables, `@load_examples:<source>` dynamic Examples, declarative tags | `features/libraries/data.feature`, `features/api/csv_examples.feature` |
| [behave-steplib](https://github.com/MathiasPaulenko/behave-steplib) | `autoload()` of pre-built steps — `categories=["api","data","io","cli"]`, `backends={"api": "requests"}` | `features/libraries/steplib.feature` |
| [behave-retry](https://github.com/MathiasPaulenko/behave-retry) | `setup_retry(max_retries=2, retry_tags=["@flaky"])` + `after_scenario_hook` + `retry_report()` | `features/libraries/retry.feature` |
| [behave-priority](https://github.com/MathiasPaulenko/behave-priority) | `setup_priority(order=True, report=True)` + hooks: priority ordering and execution report | `features/libraries/priority.feature` |
| [behave-comments](https://github.com/MathiasPaulenko/behave-comments) | `setup_lifecycle_hooks_from_path()` + `run_*` hooks + `inject_metadata()` + `@with_parsed_text` | `features/libraries/comments.feature` |

### Utility libraries — used in step code

| Library | API used | Example |
|---|---|---|
| [behave-tables](https://github.com/MathiasPaulenko/behave-tables) | `wrap(context.table)` — query/transform/export | `features/steps/tables_steps.py` |
| [behave-model](https://github.com/MathiasPaulenko/behave-model) | `load_project()`, `find_scenarios`, `Validator` | `features/steps/model_steps.py` |

### Execution & debugging tools — CLI/config examples

| Library | Usage |
|---|---|
| [behave-runner](https://github.com/MathiasPaulenko/behave-runner) | `behave-runner run / list / select / watch / lint / format / doctor`. Profiles in `[tool.behave-runner]` (`pyproject.toml`): `smoke`, `unit`, `integration` |
| [behave-pool](https://github.com/MathiasPaulenko/behave-pool) | Parallel runner registered as `[behave.runners] parallel` in `behave.ini` — `behave --runner=parallel`, `behave-pool --parallel 4`, `pool.*` userdata keys. **Note:** this suite binds port 5000 in `before_all`, so parallel workers conflict — the config is illustrative |
| [behave-trace](https://github.com/MathiasPaulenko/behave-trace) | `behave-trace` formatter writes `reports/trace.json`; `trace_log()` attaches failures. View: `behave-trace show reports/trace.json` |

### Quality & scaffolding tools — CLI/config examples

| Library | Usage |
|---|---|
| [behave-doctor](https://github.com/MathiasPaulenko/behave-doctor) | `behave-doctor scan .`, `behave-doctor impact . --changed-files <file>`. Configured in `[tool.behave-doctor]` |
| [behave-lint](https://github.com/MathiasPaulenko/behave-lint) | `behave-lint features/`, `--fix`, `--output sarif`. Configured in `[tool.behave-lint]` — `BC004` ignored because the suite deliberately uses functional tags (`@priority(N)`, `@retry:N`, `@load_examples:x`) |
| [behave-format](https://github.com/MathiasPaulenko/behave-format) | `behave-format features/` (already applied), `--check` for CI. Configured in `[tool.behave-format]` |
| [behave-gen](https://github.com/MathiasPaulenko/behave-gen) | `behave-gen init`, `add feature`, `add steps`, `from-openapi`, `migrate`, `stats` |

### Report formatters — registered in `[behave.formatters]`

| Alias | Library | Output |
|---|---|---|
| `modern` | behave-modern-html-report | `reports/behave_modern_html_report.html` — `bmr.*` userdata options |
| `steps` | behave-modern-html-report | `reports/steps_catalog.html` |
| `cucumber-json` | behave-modern-json-report | `reports/cucumber.json` |
| `modern-md` | behave-modern-md-report | `reports/behave_modern_md_report.md` |
| `behave-trace` | behave-trace | `reports/trace.json` (viewable with `behave-trace show`) |
| `csv-modern` / `xlsx-modern` / `ods-modern` | behave-modern-sheets-report | `reports/report.csv` / `.xlsx` (+ ODS registered) — `report_*` userdata options |
| `behave-modern-txt` / `behave-modern-docx` / `behave-modern-pdf` | behave-modern-file-report | `reports/report.txt` / `.docx` / `.pdf` — `bmfr.*` userdata options |

Console formatters from **behave-modern-console-report** (`modern-console`,
`modern-console-live`, `progress`, `log`, `ci`, `minimal`) can be selected with
`-f`, e.g. `behave -f modern-console`.

## Project structure

```text
python-behave-examples/
├── behave.ini                      # Behave config: formatters, outfiles, runners, userdata
├── behave_data.yml                 # behave-data: null markers, load_base_dir, data_sources
├── behave.toml                     # behave-kit: env profiles ([env.default]/[env.test])
├── pyproject.toml                  # Tool config: behave-runner/doctor/lint/format
├── requirements.txt                # Python dependencies
├── README.md
├── reports/                        # Generated reports (gitignored, recreated on run)
└── features/
    ├── environment.py              # Lifecycle hooks + wiring of all runtime libraries
    │
    ├── support/                    # Shared support code (SUT + domain models)
    │   ├── __init__.py
    │   ├── app.py                  # Flask SUT (in-memory REST API)
    │   ├── domain.py               # Calculator, StringUtils, ShoppingCart, async helpers
    │   └── data/
    │       └── users.csv           # CSV data file for @load_examples
    │
    ├── calculator/                 # Domain: calculator
    ├── string_utils/               # Domain: string utilities (Gherkin v6 Rules)
    ├── shopping_cart/              # Domain: shopping cart
    ├── async/                      # Domain: async steps
    ├── api/                        # Domain: REST API + dynamic CSV examples
    │   ├── users_api.feature
    │   └── csv_examples.feature
    ├── libraries/                  # behave-* ecosystem library demos
    │   ├── kit.feature             # behave-kit
    │   ├── tables.feature          # behave-tables
    │   ├── data.feature            # behave-data
    │   ├── comments.feature        # behave-comments
    │   ├── steplib.feature         # behave-steplib (no step code needed)
    │   ├── priority.feature        # behave-priority
    │   ├── retry.feature           # behave-retry
    │   └── model.feature           # behave-model
    │
    └── steps/                      # Step definitions (auto-discovered by behave)
        ├── common_steps.py         # Shared steps + register_type
        ├── calculator_steps.py
        ├── string_utils_steps.py
        ├── shopping_cart_steps.py
        ├── async_steps.py
        ├── api_steps.py
        ├── kit_steps.py            # behave-kit demos
        ├── tables_steps.py         # behave-tables demos
        ├── data_steps.py           # behave-data demos
        ├── comments_steps.py       # behave-comments demos
        ├── retry_steps.py          # behave-retry demos
        └── model_steps.py          # behave-model demos
```

## Setup

Requires Python 3.11+.

```bash
pip install -r requirements.txt
```

## Running tests

```bash
# Run everything — reports are auto-generated in reports/ via behave.ini
behave

# Run only smoke tests
behave --tags=@smoke

# Run only the ecosystem library demos
behave features/libraries/

# Tag expression: smoke tests that are not negative
behave --tags="@smoke and not @negative"

# Run a single feature file
behave features/calculator/calculator.feature

# Via the unified CLI (profiles are defined in pyproject.toml)
behave-runner run
behave-runner run --profile smoke
behave-runner list

# Quality tools
behave-doctor scan .
behave-lint features/
behave-format --check features/

# Parallel execution (requires the SUT caveat below — illustrative config)
behave --runner=parallel

# Open the trace viewer
behave-trace show reports/trace.json
```

## Configuration files

| File | Consumed by | Purpose |
|---|---|---|
| `behave.ini` | behave + all formatters | `format`/`outfiles`, `[behave.formatters]` aliases, `[behave.runners]`, `[behave.userdata]` (`bmr.*`, `bmfr.*`, `report_*`, `pool.*`) |
| `behave_data.yml` | behave-data | `null_markers`, `load_base_dir`, `data_sources` for `@load_examples` |
| `behave.toml` | behave-kit | `[env.*]` profiles loaded by `setup(context, env=...)` |
| `pyproject.toml` | runner/doctor/lint/format | `[tool.behave-runner]` profiles, `[tool.behave-doctor]`, `[tool.behave-lint]`, `[tool.behave-format]` |

## Known issues and caveats

- **The Flask SUT starts on every run.** `before_all` starts the server on
  port 5000 even when only unit-tagged features are selected, and the run fails
  entirely if the port is already in use.
- **`behave --runner=parallel` conflicts with the SUT.** Each behave-pool
  worker runs its own `before_all`, so all of them try to bind port 5000.
  To run the suite in parallel, start the server externally or use a
  per-worker port.
- **`behave-doctor` reports expected diagnostics** on this suite: it flags
  `BD302` (undefined step) for steplib steps and behave-kit class-based steps
  because both are registered at runtime — doctor's AST scan cannot see them.
  It also flags the lifecycle-flag steps (`BD301`) that are invoked through
  behave-comments hooks.
- **`behave-data` dynamic Examples need a non-empty table.** The `Examples:`
  block must declare headers plus at least one row; the injected rows replace
  it. An empty `Examples:` block is skipped by the loader (and crashes
  `behave-model`'s parser — upstream issue).
- **Empty `Examples:` blocks crash `behave-model`** (`table=None` is not
  handled by its adapter) — keep a placeholder row in the table.
- **The flaky retry demo intentionally logs a failed first attempt.** The
  final result is a pass; the retry report in `after_all` counts it as
  retried.

## Contributing

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

Please note that this project follows a
[Code of Conduct](CODE_OF_CONDUCT.md).

## License

Distributed under the MIT License — see [LICENSE](LICENSE) for details.
