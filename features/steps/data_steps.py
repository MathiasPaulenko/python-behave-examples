"""
Step definitions for the behave-data feature.

Corresponds to ``features/libraries/data.feature`` and demonstrates
typed table columns (``age:int``, ``active:bool``, ``price:float``,
``created:date``), null resolution, and ``typed_wrap()``.
"""
from __future__ import annotations

from behave import then, when
from behave_data import typed_wrap


@when("I read the typed users table:")
def step_read_typed_table(context):
    """Converts ``context.table`` rows into typed dicts.

    Column headers carry a ``name:type`` suffix — ``age:int`` arrives as
    ``int``, ``active:bool`` as ``bool``, and empty cells as ``None``.
    """
    context.typed_rows = typed_wrap(context.table).typed_dicts()


@then("the first row's age should be int {expected:d}")
def step_age_int(context, expected):
    age = context.typed_rows[0]["age"]
    assert isinstance(age, int), f"Expected int, got {type(age).__name__}"
    assert age == expected


@then("the second row's active should be bool false")
def step_active_bool(context):
    active = context.typed_rows[1]["active"]
    assert isinstance(active, bool), f"Expected bool, got {type(active).__name__}"
    assert active is False


@then("the first row's price should be float {expected:f}")
def step_price_float(context, expected):
    price = context.typed_rows[0]["price"]
    assert isinstance(price, float), f"Expected float, got {type(price).__name__}"
    assert price == expected


@then("Bob's age should be None")
def step_age_none(context):
    assert context.typed_rows[1]["age"] is None


@then("Bob's city should be None")
def step_city_none(context):
    assert context.typed_rows[1]["city"] is None


@then("the created date should be year {year:d} and month {month:d}")
def step_date_parts(context, year, month):
    created = context.typed_rows[0]["created"]
    assert created.year == year
    assert created.month == month
