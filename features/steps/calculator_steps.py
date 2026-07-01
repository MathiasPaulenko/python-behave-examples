"""
Step definitions for the Calculator feature.

Each step function corresponds to a Gherkin step in
``features/calculator/calculator.feature``. The calculator instance is
created fresh in ``before_scenario`` (environment.py) and stored in
``context.calculator``.

Steps use behave's built-in ``{value:d}`` type converter which parses
integers automatically.
"""
from __future__ import annotations

from behave import given, when, then


@given("I have a calculator")
def step_have_calculator(context):
    """Verifies that a Calculator instance was injected by the environment."""
    assert context.calculator is not None


@given("the calculator is reset")
def step_reset(context):
    """Resets the calculator accumulator to 0 and clears the last operation."""
    context.calculator.reset()


@given("the calculator accumulator is {value:d}")
def step_set_accumulator(context, value):
    """Sets the accumulator to an explicit value (used by Scenario Outlines)."""
    context.calculator.accumulator = float(value)


@when("I add {value:d} to the calculator")
def step_add(context, value):
    """Adds ``value`` to the accumulator."""
    context.calculator.add(float(value))


@when("I subtract {value:d} to the calculator")
def step_subtract(context, value):
    """Subtracts ``value`` from the accumulator."""
    context.calculator.subtract(float(value))


@when("I multiply {value:d} to the calculator")
def step_multiply(context, value):
    """Multiplies the accumulator by ``value``."""
    context.calculator.multiply(float(value))


@when("I divide the calculator by {value:d}")
def step_divide(context, value):
    """Divides the accumulator by ``value``.

    Catches ``ZeroDivisionError`` and stores it in ``context.exc``
    so a subsequent ``Then a ZeroDivisionError should be raised`` step
    can assert on it.
    """
    try:
        context.calculator.divide(float(value))
        context.exc = None
    except Exception as e:
        context.exc = e


@when("I divide {value:d} to the calculator")
def step_divide_to(context, value):
    """Alternative phrasing for division (used by Scenario Outline rows).

    Behave matches the literal step text, so both
    "I divide the calculator by 4" and "I divide 4 to the calculator"
    need their own step definition.
    """
    try:
        context.calculator.divide(float(value))
        context.exc = None
    except Exception as e:
        context.exc = e


@when("I take the square root")
def step_sqrt(context):
    """Takes the square root of the current accumulator value.

    Catches ``ValueError`` (negative input) and stores it in
    ``context.exc`` for later assertion.
    """
    try:
        context.calculator.sqrt()
        context.exc = None
    except Exception as e:
        context.exc = e


@then("the result should be {expected:d}")
def step_result(context, expected):
    """Asserts that the accumulator equals ``expected``."""
    assert context.calculator.result() == float(expected), (
        f"Expected {expected}, got {context.calculator.result()}"
    )


@then('the last operation should be "{op_name}"')
def step_last_op(context, op_name):
    """Asserts that ``last_operation`` matches the expected operation name."""
    assert context.calculator.last_operation == op_name, (
        f"Expected '{op_name}', got '{context.calculator.last_operation}'"
    )


@then("a ZeroDivisionError should be raised")
def step_zero_division(context):
    """Asserts that a ``ZeroDivisionError`` was caught during a previous step."""
    assert isinstance(context.exc, ZeroDivisionError), (
        f"Expected ZeroDivisionError, got {context.exc!r}"
    )


@then("a ValueError should be raised")
def step_value_error(context):
    """Asserts that a ``ValueError`` was caught during a previous step."""
    assert isinstance(context.exc, ValueError), (
        f"Expected ValueError, got {context.exc!r}"
    )
