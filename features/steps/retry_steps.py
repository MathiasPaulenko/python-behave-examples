"""
Step definitions for the behave-retry feature.

Corresponds to ``features/libraries/retry.feature`` and demonstrates
automatic retry: a module-level counter survives re-execution, so the
scenario fails on attempt 1 and passes on attempt 2 — deterministic.
"""
from __future__ import annotations

from behave import then, when

# Module state persists across retries because the process is reused.
_ATTEMPTS = {"count": 0}


@when("a step fails on its first attempt")
def step_fail_first_attempt(context):
    """Fails on attempt 1, succeeds on attempt 2 — proving re-execution."""
    _ATTEMPTS["count"] += 1
    if _ATTEMPTS["count"] == 1:
        raise AssertionError("Simulated transient failure (attempt 1)")


@then("the scenario should pass after retrying")
def step_passed_after_retry(context):
    """Only reachable on the second attempt of the flaky scenario."""
    assert _ATTEMPTS["count"] >= 2, (
        f"Expected at least 2 attempts, ran {_ATTEMPTS['count']}"
    )
