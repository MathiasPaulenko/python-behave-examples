"""
Common step definitions and custom type registrations shared across features.

This module is imported by behave automatically (it lives in ``features/steps/``)
and provides:

  * **Custom type converter** ``Boolean`` — registered via ``register_type``
    so that ``{flag:Boolean}`` in step patterns parses strings like
    "true", "yes", "1" into Python ``bool``.
  * **Generic API steps** — health check, database cleanup, response status
    and field assertions used by multiple API feature files.

These steps are reusable across any feature that needs to interact with
the Flask SUT or assert on HTTP responses.
"""
from __future__ import annotations

from behave import given, then, register_type


# --------------------------------------------------------------------- #
#  Custom type converters for step parsers
# --------------------------------------------------------------------- #
def parse_boolean(text: str) -> bool:
    """Converts a string to a boolean.

    Accepts: "true", "yes", "1" (case-insensitive) → ``True``.
    Everything else → ``False``.

    Registered as ``Boolean`` so steps can use ``{flag:Boolean}``.
    """
    return text.strip().lower() in ("true", "yes", "1")


register_type(Boolean=parse_boolean)


# --------------------------------------------------------------------- #
#  Generic API steps
# --------------------------------------------------------------------- #
@given("the API server is running")
def step_api_running(context):
    """Verifies that the Flask SUT is reachable by hitting ``/api/health``.

    The server is started in ``before_all`` (environment.py) in a
    background thread. This step acts as a smoke check before
    running API scenarios.
    """
    import requests

    resp = requests.get(f"{context.api_url}/api/health", timeout=2)
    assert resp.ok, f"API server not reachable: {resp.status_code}"


@given("the users database is empty")
def step_db_empty(context):
    """Deletes all users from the SUT to ensure a clean state.

    Fetches all users via GET, then DELETEs each one individually.
    This guarantees test isolation between scenarios that share
    the same SUT instance.
    """
    import requests

    resp = requests.get(f"{context.api_url}/api/users", timeout=2)
    assert resp.ok
    body = resp.json()
    for user in body.get("data", []):
        requests.delete(f"{context.api_url}/api/users/{user['id']}", timeout=2)


@then('the response status should be {status:d}')
def step_response_status(context, status):
    """Asserts that the last HTTP response status code equals ``status``.

    Uses ``{status:d}`` type converter to parse the integer from the step text.
    The response is stored in ``context.response`` by a preceding ``When`` step.
    """
    assert context.response.status_code == status, (
        f"Expected status {status}, got {context.response.status_code}: "
        f"{context.response.text}"
    )


@then('the response should contain "{field}"')
def step_response_contains(context, field):
    """Asserts that the JSON response body contains a top-level ``field`` key."""
    body = context.response.json()
    assert field in body, f"Response missing field '{field}': {body}"


@then('the response field "{field}" should be "{value}"')
def step_response_field(context, field, value):
    """Asserts that a string field in the JSON response equals ``value``.

    Both ``field`` and ``value`` are captured as quoted strings.
    The actual value is converted to ``str`` before comparison.
    """
    body = context.response.json()
    actual = str(body.get(field))
    assert actual == value, f"Field '{field}': expected '{value}', got '{actual}'"


@then('the response field "{field}" should be {value:d}')
def step_response_field_int(context, field, value):
    """Asserts that an integer field in the JSON response equals ``value``.

    Uses ``{value:d}`` type converter so behave parses the integer
    automatically. This avoids quoting issues with numeric fields
    like ``total`` or ``count``.
    """
    body = context.response.json()
    actual = body.get(field)
    assert actual == value, f"Field '{field}': expected {value}, got {actual}"


@then("the response should contain at most {count:d} items")
def step_response_at_most(context, count):
    """Asserts that the ``data`` array in the response has at most ``count`` items.

    Used for pagination testing — the API returns a ``data`` key with
    a slice of results and a ``total`` key with the full count.
    """
    body = context.response.json()
    data = body.get("data", body)
    assert len(data) <= count, f"Expected at most {count} items, got {len(data)}"
