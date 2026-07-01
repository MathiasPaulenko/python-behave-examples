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
- **JUnit** and **JSON** report output

## Project structure

```text
python-behave-examples/
├── behave.ini                      # Behave configuration (formats, outfiles, junit)
├── requirements.txt                # Python dependencies
├── README.md
├── reports/                        # Generated reports (created on run)
│   ├── pretty.txt                  # Human-readable pretty output
│   ├── results.json                # Machine-readable JSON summary
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
multi-line keys (paired by position):

```ini
format = pretty
    json
outfiles = reports/pretty.txt
    reports/results.json
```

To try a new report library, add its formatter name and output path:

```ini
format = pretty
    json
    html-pretty
outfiles = reports/pretty.txt
    reports/results.json
    reports/report.html
```

| File | Description |
|---|---|
| `reports/pretty.txt` | Human-readable pretty output (same as console) |
| `reports/results.json` | Machine-readable JSON summary (CI-friendly) |
| `reports/junit/*.xml` | JUnit XML — one file per feature (CI integration) |

## Requirements

- Python 3.10+
- behave 1.3.3
- Flask, requests, PyHamcrest, jsonschema
