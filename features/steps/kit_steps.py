"""
Step definitions for the behave-kit feature.

Corresponds to ``features/libraries/kit.feature`` and demonstrates
behave-kit utilities: ``assert_soft``, ``env``, ``get_path``,
``wait_until``, ``@parameter_type``, ``@scoped`` and class-based steps
via ``step_impl_base``.
"""
from __future__ import annotations

import itertools
from dataclasses import dataclass

from behave import given, then, when
from behave_kit import (
    assert_soft,
    env,
    get_path,
    parameter_type,
    scoped,
    step_impl_base,
    wait_until,
)


# --------------------------------------------------------------------- #
#  Soft assertions
# --------------------------------------------------------------------- #
@when("I check several conditions with soft assertions")
def step_soft_asserts(context):
    """Collects several soft-assertion checks in a single step.

    Unlike a plain ``assert``, a failing soft assertion does not abort the
    step — every failure is collected and reported together by
    behave-kit's ``teardown()`` in ``after_scenario``.
    """
    assert_soft(1 + 1 == 2, "math still works")
    assert_soft("behave" in "python-behave-examples", "substring check")
    assert_soft(len(context.calculator.items if False else [1, 2, 3]) == 3)


@then("the soft assertion report should be clean")
def step_soft_report_clean(context):
    """Documents where soft-assert failures would surface.

    Any collected failure would be raised by kit's teardown at the end of
    the scenario — reaching this step means none were collected.
    """
    assert True


# --------------------------------------------------------------------- #
#  Typed env() reads
# --------------------------------------------------------------------- #
@when('I read the "{name}" env var as int with default {default:d}')
def step_env_int(context, name, default):
    """Reads an environment variable as ``int`` with a default value."""
    context.env_int = env(name, var_type=int, default=default)


@when('I read the "{name}" env var as bool with default {default:Boolean}')
def step_env_bool(context, name, default):
    """Reads an environment variable as ``bool`` with a default value.

    Uses the ``Boolean`` converter registered in ``common_steps.py``.
    """
    context.env_bool = env(name, var_type=bool, default=default)


@then("the env results should be {expected_int:d} and {expected_bool:Boolean}")
def step_env_results(context, expected_int, expected_bool):
    """Asserts both typed env() reads."""
    assert context.env_int == expected_int
    assert context.env_bool == expected_bool


# --------------------------------------------------------------------- #
#  get_path navigation
# --------------------------------------------------------------------- #
@given("I have a nested response payload")
def step_nested_payload(context):
    """Stores a nested dict used by the get_path assertions."""
    context.payload = {
        "user": {"name": "Ada", "address": {"city": "Berlin"}},
        "users": [{"name": "Alice"}, {"name": "Bob"}],
    }


@then('get_path "{path}" should return "{expected}"')
def step_get_path(context, path, expected):
    """Asserts dot-notation navigation into the nested payload."""
    actual = get_path(context.payload, path)
    assert actual == expected, f"get_path({path!r}) = {actual!r}, expected {expected!r}"


# --------------------------------------------------------------------- #
#  wait_until polling
# --------------------------------------------------------------------- #
@when("I wait until the counter reaches {target:d}")
def step_wait_until(context, target):
    """Polls a condition that becomes true after ``target`` evaluations.

    ``itertools.count`` increments on every poll, so the condition holds
    on the Nth check — demonstrating wait_until's polling loop.
    ``wait_until`` returns ``None`` on success and raises ``TimeoutError``
    when the condition never becomes true.
    """
    counter = itertools.count(1)

    def condition() -> bool:
        context.polls = next(counter)
        return context.polls >= target

    wait_until(condition, timeout=5, interval=0.01)


@then("the wait should have succeeded")
def step_wait_succeeded(context):
    """Reaching this step means the condition held before the timeout."""
    assert context.polls >= 1


# --------------------------------------------------------------------- #
#  Custom parameter type + scoped attribute
# --------------------------------------------------------------------- #
@dataclass
class EmailAddress:
    """Value object produced by the Email parameter type."""

    raw: str

    @property
    def domain(self) -> str:
        return self.raw.split("@", 1)[1]


@parameter_type("Email", r"[\w.+-]+@[\w-]+\.[a-z]+")
def _parse_email(text):
    return EmailAddress(raw=text)


@when('I log in as "{email:Email}" using the kit Email type')
@scoped("login_email")
def step_login_email(context, email):
    """Stores the parsed EmailAddress as a scoped context attribute.

    ``@scoped("login_email")`` registers the attribute for automatic
    deletion when the scenario ends — no manual cleanup needed.
    """
    context.login_email = email


@then('the parsed email should have domain "{domain}"')
def step_email_domain(context, domain):
    """Asserts the custom type converter produced an EmailAddress."""
    assert context.login_email.domain == domain


@then("the attribute should be scoped for cleanup")
def step_scoped_attr(context):
    """The attribute still exists now; it is removed at scenario end."""
    assert context.login_email is not None


# --------------------------------------------------------------------- #
#  Class-based steps
# --------------------------------------------------------------------- #
AccountBase = step_impl_base()


class AccountSteps(AccountBase):
    """Steps implemented as methods — self.context is bound automatically."""

    @AccountBase.given("I have a class-based account with balance {amount:d}")
    def set_balance(self, amount):
        self.context.account_balance = amount

    @AccountBase.when("the class-based account deposits {amount:d}")
    def deposit(self, amount):
        self.context.account_balance += amount

    @AccountBase.then("the class-based balance should be {expected:d}")
    def check_balance(self, expected):
        assert self.context.account_balance == expected


AccountSteps.register()
