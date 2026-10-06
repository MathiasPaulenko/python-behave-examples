"""
Step definitions for the behave-tables feature.

Corresponds to ``features/libraries/tables.feature`` and demonstrates
the ``wrap()`` API from behave-tables: conversion, querying,
transformation, and export of ``context.table``.
"""
from __future__ import annotations

from dataclasses import dataclass

from behave import then, when
from behave_tables import TableWrapper, wrap


@dataclass
class TableUser:
    """Dataclass model used by ``as_models``."""

    name: str
    age: str
    city: str = ""


@when("I wrap the following users table:")
def step_wrap_table(context):
    """Wraps ``context.table`` with the TableWrapper API."""
    context.wrapped = wrap(context.table)


# -- conversion -------------------------------------------------------- #
@then("the table has {count:d} rows as dicts")
def step_as_dicts(context, count):
    rows = context.wrapped.as_dicts()
    assert len(rows) == count
    assert all(isinstance(r, dict) for r in rows)


@then("converting to dataclass models gives {count:d} users")
def step_as_models(context, count):
    users = context.wrapped.as_models(TableUser)
    assert len(users) == count
    assert all(isinstance(u, TableUser) for u in users)


@then('the "{column}" column is "{expected}"')
def step_column(context, column, expected):
    values = context.wrapped.column(column)
    assert ", ".join(values) == expected


# -- querying ---------------------------------------------------------- #
@then('find_row name={name} returns age "{expected_age}"')
def step_find_row(context, name, expected_age):
    row = context.wrapped.find_row(name=name)
    assert row is not None and row["age"] == expected_age


@then('find_all_rows with city "{city}" returns {count:d} row')
def step_find_all(context, city, count):
    assert len(context.wrapped.find_all_rows(city=city)) == count


@then('count with age "{age}" is {expected:d}')
def step_count(context, age, expected):
    assert context.wrapped.count(age=age) == expected


@then('first row name is "{first_name}" and last row name is "{last_name}"')
def step_first_last(context, first_name, last_name):
    assert context.wrapped.first()["name"] == first_name
    assert context.wrapped.last()["name"] == last_name


# -- transformation ---------------------------------------------------- #
@then('select "{column}" gives a 1-column table')
def step_select(context, column):
    selected = context.wrapped.select(column)
    assert selected.headers == [column]
    assert len(selected) == len(context.wrapped)


@then('sorting by "{column}" descending starts with "{first}"')
def step_sort(context, column, first):
    sorted_table = context.wrapped.sort(column, reverse=True)
    assert sorted_table.first()[column] == first or sorted_table.first()["name"] == first


@then('unique "{column}" returns "{expected}"')
def step_unique(context, column, expected):
    assert ", ".join(context.wrapped.unique(column)) == expected


# -- export ------------------------------------------------------------ #
@then('to_csv produces "{header}" headers')
def step_to_csv(context, header):
    first_line = context.wrapped.to_csv().splitlines()[0]
    assert first_line == header


@then("to_json produces a {count:d}-element array")
def step_to_json(context, count):
    import json

    assert len(json.loads(context.wrapped.to_json())) == count


@then("a CSV round-trip restores the table")
def step_csv_roundtrip(context):
    restored = TableWrapper.from_csv(context.wrapped.to_csv())
    assert restored.as_dicts() == context.wrapped.as_dicts()
