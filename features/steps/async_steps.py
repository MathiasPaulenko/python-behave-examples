"""
Async step definitions — behave 1.3.x supports ``async def`` steps natively.

Corresponds to ``features/async/async_steps.feature``.

The event loop is managed automatically by behave. Async results are stored
in ``context.async_results`` (a dict) so that subsequent ``Then`` steps can
assert on them without needing to be async themselves.
"""
from __future__ import annotations

from behave import then, when


@when('I asynchronously fetch the value for "{key}"')
async def step_async_fetch(context, key):
    """Asynchronously fetches a value for ``key`` from the async mapping.

    The result is stored in ``context.async_results[key]``.
    Uses ``await`` to call the async helper from ``features.support.domain``.
    """
    from features.support.domain import async_fetch_value

    context.async_results[key] = await async_fetch_value(key)
    context.last_async_key = key


@when("I asynchronously double the number {value:d}")
async def step_async_double(context, value):
    """Asynchronously doubles ``value`` and stores the result.

    The result key is ``double_{value}`` to avoid collisions with
    other async results in the same scenario.
    """
    from features.support.domain import async_double

    result_key = f"double_{value}"
    context.async_results[result_key] = await async_double(value)
    context.last_async_key = result_key


@then('the async result should be "{expected}"')
def step_async_result_str(context, expected):
    """Asserts that the last async result (as a string) equals ``expected``.

    This step is synchronous — it reads ``context.last_async_key``, set by
    the preceding async ``When`` step, so the asserted result is explicit
    even when several async operations ran in the same scenario.
    """
    actual = str(context.async_results[context.last_async_key])
    assert actual == expected, f"Expected '{expected}', got '{actual}'"


@then("the async result should be {expected:d}")
def step_async_result_int(context, expected):
    """Asserts that the last async result (as an integer) equals ``expected``.

    Uses the ``{expected:d}`` type converter so behave parses the integer
    automatically from the step text.
    """
    actual = context.async_results[context.last_async_key]
    assert actual == expected, f"Expected {expected}, got {actual}"
