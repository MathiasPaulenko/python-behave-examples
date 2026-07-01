"""
Step definitions for the String utilities feature.

Corresponds to ``features/string_utils/string_utils.feature`` which uses
Gherkin v6 Rule blocks to group related scenarios.

The ``StringUtils`` instance is created in ``before_scenario`` and stored
in ``context.string_utils``. Intermediate results are kept in
``context.last_result`` for assertion in subsequent ``Then`` steps.
"""
from __future__ import annotations

from behave import given, when, then


@given("I have the string utilities")
def step_have_string_utils(context):
    """Verifies that a ``StringUtils`` instance was injected by the environment."""
    assert context.string_utils is not None


@when('I reverse the string "{text}"')
def step_reverse(context, text):
    """Reverses ``text`` and stores the result in ``context.last_result``."""
    context.last_input = text
    context.last_result = context.string_utils.reverse(text)


@then('the reversed string should be "{expected}"')
def step_reversed_should_be(context, expected):
    """Asserts that the last reversal result equals ``expected``."""
    assert context.last_result == expected, (
        f"Expected '{expected}', got '{context.last_result}'"
    )


@then('the string "{text}" should be a palindrome')
def step_is_palindrome(context, text):
    """Asserts that ``text`` is a palindrome (ignoring case and punctuation)."""
    assert context.string_utils.is_palindrome(text), (
        f"'{text}' is not a palindrome"
    )


@then('the string "{text}" should not be a palindrome')
def step_not_palindrome(context, text):
    """Asserts that ``text`` is NOT a palindrome."""
    assert not context.string_utils.is_palindrome(text), (
        f"'{text}' was unexpectedly a palindrome"
    )


@when('I count the vowels in "{text}"')
def step_count_vowels(context, text):
    """Counts vowels (a, e, i, o, u) in ``text`` case-insensitively."""
    context.last_input = text
    context.last_result = context.string_utils.count_vowels(text)


@then("the vowel count should be {count:d}")
def step_vowel_count(context, count):
    """Asserts that the last vowel count equals ``count``."""
    assert context.last_result == count, (
        f"Expected {count} vowels, got {context.last_result}"
    )


@when('I convert "{text}" to title case')
def step_title_case(context, text):
    """Converts ``text`` to title case and stores the result."""
    context.last_input = text
    context.last_result = context.string_utils.to_title_case(text)


@then('the result should be "{expected}"')
def step_result_should_be(context, expected):
    """Generic assertion: the last transformation result equals ``expected``.

    This step is shared by title-case and slugify scenarios.
    """
    assert context.last_result == expected, (
        f"Expected '{expected}', got '{context.last_result}'"
    )


@when('I slugify "{text}"')
def step_slugify(context, text):
    """Converts ``text`` to a URL-friendly slug and stores the result."""
    context.last_input = text
    context.last_result = context.string_utils.slugify(text)
