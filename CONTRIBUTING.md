# Contributing

Thanks for your interest in contributing! This repository is an educational
collection of Behave / Gherkin examples — contributions that add new
demonstrations, fix broken examples, or improve documentation are welcome.

## Getting started

Requirements: Python 3.10+

```bash
# Clone and create a virtual environment
git clone https://github.com/MathiasPaulenko/python-behave-examples.git
cd python-behave-examples
python -m venv .venv

# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt
```

## Running the suite

```bash
# Everything
behave

# Validate Gherkin syntax and step matching without executing
behave --dry-run

# List all registered step definitions before adding new ones
behave --steps-catalog
```

All scenarios should pass before submitting a change. Note that the report
formatter packages are required — `behave` will not start if a registered
formatter cannot be imported.

## Conventions

- **Gherkin**: write scenarios in business language, not technical steps.
  Reuse existing step definitions before creating new ones (check
  `behave --steps-catalog`).
- **Steps with data tables or DocStrings** must end their pattern with a
  colon (`:`) — behave 1.3.x no longer strips it.
- **Python**: PEP 8, `snake_case` for step functions. Keep domain logic in
  `features/support/`, step glue in `features/steps/`.
- **Commits**: [Conventional Commits](https://www.conventionalcommits.org/)
  (`feat:`, `fix:`, `docs:`...), small and atomic, in English.
- Never commit generated artifacts (`__pycache__`, ad-hoc output files) or
  secrets.

## Pull requests

1. Fork the repo and create a branch from `main`.
2. Make your change; add or update a `.feature` + steps if you're adding a
   demonstration.
3. Run `behave` and make sure everything passes.
4. Open a PR describing what the change demonstrates or fixes.
