# python-behave-examples

Repository with examples of use of the **Behave** library in Python.

This project is a **complete, self-contained Behave automation suite** that
demonstrates every major Gherkin / Behave feature using **behave 1.3.x**
(latest release: `1.3.3`).

## What's inside

| Feature file | Demonstrates |
|---|---|
| `features/calculator.feature` | **Background**, **Scenario Outline** with multiple `Examples` tables, tags |
| `features/string_utils.feature` | **Gherkin v6 `Rule`** blocks, `Example` keyword, `Background` inside a Rule |
| `features/shopping_cart.feature` | **Data tables**, **DocStrings** (`"""`), Scenario Outline with tables |
| `features/async_steps.feature` | **Async step definitions** (behave 1.3.x native support) |
| `features/api/users_api.feature` | **REST API testing** with `requests` against a real Flask server, data tables, pagination, Scenario Outline |
| `features/api/csv_examples.feature` | **External CSV** file as `Examples` source |

### Behave capabilities showcased

- **Gherkin v6 grammar**: `Rule`, `Example`, `Background` (including inside Rules)
- **Scenario Outline** with multiple `Examples` tables
- **Data tables** (step-level) and **DocStrings**
- **Tags** (`@smoke`, `@negative`, `@api`, `@unit`, `@integration`, `@wip`) and tag filtering
- **Async steps** (`async def` step functions)
- **Custom type converters** (`register_type`)
- **Environment hooks**: `before_all` / `after_all`, `before_feature` / `after_feature`,
  `before_rule` / `after_rule`, `before_scenario` / `after_scenario`,
  `before_step` / `after_step`
- **`context.add_cleanup`** for stack-based teardown
- **External CSV** Examples tables
- **In-memory Flask SUT** started in a background thread (no external services needed)
- **Multiple report formats**: pretty, JSON, JUnit XML, HTML, Markdown, Cucumber JSON,
  step catalogs — all via configurable formatters in `behave.ini`

## Project structure

```text
python-behave-examples/
├── behave.ini                      # Behave configuration (formats, outfiles, junit)
├── requirements.txt                # Python dependencies
├── README.md
├── reports/                        # Generated reports (created on run)
│   ├── pretty.txt                  # Behave built-in pretty formatter
│   ├── results.json                # Behave built-in JSON formatter
│   ├── behave_modern_html_report.html  # Modern HTML report (behave-modern-html-report)
│   ├── step_catalog.html           # HTML step catalog
│   ├── results_rjson.json          # Modern JSON report (behave-modern-json-report)
│   ├── results_cucumber.json       # Cucumber JSON format (CI-compatible)
│   ├── results_markdown.md         # Markdown report (behave-modern-md-report)
│   ├── step_catalog.md             # Markdown step catalog
│   └── junit/                      # JUnit XML reports (one file per feature)
└── features/
    ├── environment.py              # Lifecycle hooks (before_all, before_rule, ...)
    │
    ├── support/                    # Shared support code (SUT + domain models)
    │   ├── __init__.py
    │   ├── app.py                  # Flask SUT (in-memory REST API)
    │   ├── domain.py               # Calculator, StringUtils, ShoppingCart, async helpers
    │   └── data/
    │       └── users.csv           # External Examples data (CSV)
    │
    ├── calculator/                 # Domain: calculator
    │   └── calculator.feature      # Background + Scenario Outline
    │
    ├── string_utils/               # Domain: string utilities
    │   └── string_utils.feature    # Gherkin v6 Rule blocks
    │
    ├── shopping_cart/              # Domain: shopping cart
    │   └── shopping_cart.feature   # Data tables + DocStrings
    │
    ├── async/                      # Domain: async steps
    │   └── async_steps.feature     # async def step definitions
    │
    ├── api/                        # Domain: REST API
    │   ├── users_api.feature       # CRUD testing with requests
    │   └── csv_examples.feature    # External CSV Examples
    │
    └── steps/                      # Step definitions (auto-discovered by behave)
        ├── common_steps.py         # Shared steps + register_type
        ├── calculator_steps.py
        ├── string_utils_steps.py
        ├── shopping_cart_steps.py
        ├── async_steps.py
        └── api_steps.py
```

## Setup

```bash
pip install -r requirements.txt
```

## Running tests

```bash
# Run everything — reports are auto-generated in reports/ via behave.ini
# (pretty.txt, results.json, junit/*.xml)
behave

# Run only smoke tests
behave --tags=@smoke

# Run only API integration tests
behave --tags=@api

# Tag expression: smoke tests that are not negative
behave --tags="@smoke and not @negative"

# Run a single feature file
behave features/calculator/calculator.feature
```

### Report configuration

All outputs are configured in `behave.ini` using the `format` and `outfiles`
multi-line keys (paired by position). Custom formatters are registered in the
`[behave.formatters]` section.

#### File formatters (paired with outfiles)

| Formatter name | Library | Output file | Description |
|---|---|---|---|
| `pretty` | behave (built-in) | `reports/pretty.txt` | Human-readable colored output |
| `json` | behave (built-in) | `reports/results.json` | Behave JSON summary |
| `modern` | behave-modern-html-report | `reports/behave_modern_html_report.html` | Modern interactive HTML report |
| `steps` | behave-modern-html-report | `reports/step_catalog.html` | HTML step catalog (all registered steps) |
| `rjson` | behave-modern-json-report | `reports/results_rjson.json` | Enhanced JSON with metadata (project, branch, build) |
| `cucumber` | behave-modern-json-report | `reports/results_cucumber.json` | Cucumber-compatible JSON (CI tools like Jenkins) |
| `markdown` | behave-modern-md-report | `reports/results_markdown.md` | Markdown report for documentation/GitHub |
| `stepcatalog` | behave-modern-md-report | `reports/step_catalog.md` | Markdown step catalog |
| _(junit)_ | behave (built-in) | `reports/junit/*.xml` | JUnit XML — enabled via `junit = true` |

#### Console formatters (default_format)

The console output is controlled by `default_format` in `behave.ini`.
Available console formatters (registered in `[behave.formatters]`):

| Formatter name | Library | Description |
|---|---|---|
| `minimal` | behave-modern-console-report | Compact one-line-per-scenario output |
| `progress` | behave-modern-console-report | Progress bar with percentage |
| `modern` | behave-modern-console-report | Modern colored output with timestamps |
| `modern-live` | behave-modern-console-report | Live-updating modern output |
| `log` | behave-modern-console-report | Structured log format with timestamps |
| `ci` | behave-modern-console-report | CI-optimized output |
| `pretty` | behave (built-in) | Default behave pretty output |

To switch the console format, change `default_format` in `behave.ini`:

```ini
default_format = progress
```

#### Adding a new report library

1. Install the package: `pip install <package>`
2. Register the formatter in `[behave.formatters]`:
   ```ini
   [behave.formatters]
   myformat = my_package.formatter:MyFormatter
   ```
3. Add it to the `format` / `outfiles` lists:
   ```ini
   format = pretty
       json
       myformat
   outfiles = reports/pretty.txt
       reports/results.json
       reports/my_report.html
   ```

## Requirements

- Python 3.10+
- behave 1.3.3
- Flask, requests, PyHamcrest, jsonschema
- behave-modern-html-report 2.2.1
- behave-modern-json-report 1.1.0
- behave-modern-md-report 1.2.0
- behave-modern-console-report 1.0.1
