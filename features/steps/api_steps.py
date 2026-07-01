"""
Step definitions for the Users REST API feature.

Corresponds to ``features/api/users_api.feature`` and
``features/api/csv_examples.feature``.

These steps use the ``requests`` library to make real HTTP calls against
the Flask SUT started in a background thread by ``environment.py``.
The base URL is stored in ``context.api_url``.

Note: Steps that accept a data table MUST end with a colon (``:``) in
behave 1.3.x — the framework no longer strips trailing colons.
"""
from __future__ import annotations

import requests
from behave import given, when, then


@given('a user exists with email "{email}"')
def step_user_exists(context, email):
    """Creates a user via POST and stores the id + endpoint for later steps.

    The created user's endpoint is stored in ``context.created_user_endpoint``
    so that subsequent GET/DELETE steps can reference it.
    """
    resp = requests.post(
        f"{context.api_url}/api/users",
        json={"name": "Temp User", "email": email, "role": "viewer"},
        timeout=2,
    )
    assert resp.status_code == 201, f"Could not create user: {resp.text}"
    context.created_user_id = resp.json()["id"]
    context.created_user_endpoint = f"/api/users/{context.created_user_id}"


@given("the following users exist:")
def step_users_exist_table(context):
    """Creates multiple users from a horizontal data table.

    The table must have columns: ``name``, ``email``, ``role``.
    Each row represents one user to create via POST.
    """
    for row in context.table:
        resp = requests.post(
            f"{context.api_url}/api/users",
            json={"name": row["name"], "email": row["email"], "role": row["role"]},
            timeout=2,
        )
        assert resp.status_code == 201, f"Could not create user {row}: {resp.text}"


@given('a user named "{name}" with email "{email}"')
def step_user_named(context, name, email):
    """Stores pending user data for use in a subsequent POST step.

    Used by the CSV examples feature where the user data comes from
    an external CSV file.
    """
    context.pending_user = {"name": name, "email": email}


@when('I send a {method} request to "{url}"')
def step_send_request(context, method, url):
    """Sends an HTTP request with no body and stores the response.

    ``method`` is injected from the step text (GET, POST, DELETE, etc.).
    The response is stored in ``context.response``.
    """
    context.response = requests.request(
        method,
        f"{context.api_url}{url}",
        timeout=2,
    )


@when('I send a {method} request to "{url}" with:')
def step_send_request_with_table(context, method, url):
    """Sends an HTTP request with a JSON body built from a vertical data table.

    The table must have columns: ``field``, ``value``.
    Each row becomes a key-value pair in the JSON payload.
    """
    data = {row["field"]: row["value"] for row in context.table.rows}
    context.response = requests.request(
        method,
        f"{context.api_url}{url}",
        json=data,
        timeout=2,
    )


@when("I send a GET request to the created user endpoint")
def step_get_created_user(context):
    """GETs the user created by a preceding ``Given a user exists`` step."""
    context.response = requests.get(
        f"{context.api_url}{context.created_user_endpoint}",
        timeout=2,
    )


@when("I send a DELETE request to the created user endpoint")
def step_delete_created_user(context):
    """DELETEs the user created by a preceding ``Given a user exists`` step."""
    context.response = requests.delete(
        f"{context.api_url}{context.created_user_endpoint}",
        timeout=2,
    )
