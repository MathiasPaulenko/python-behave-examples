"""
Step definitions for the behave-model feature.

Corresponds to ``features/libraries/model.feature`` — a meta example:
the suite loads its own ``features/`` tree with behave-model's
``load_project()``, queries scenarios by tag, and runs the Validator.
"""
from __future__ import annotations

from behave import then, when
from behave_model import Validator, load_project


@when('I load the behave project model for "{path}"')
def step_load_project(context, path):
    """Parses the whole features/ tree into the canonical model."""
    context.model_project = load_project(path)


@then("the project should contain at least {count:d} features")
def step_min_features(context, count):
    stats = context.model_project.statistics()
    assert stats["features"] >= count, f"features={stats['features']}"


@then("the project should contain at least {count:d} scenarios")
def step_min_scenarios(context, count):
    stats = context.model_project.statistics()
    assert stats["scenarios"] >= count, f"scenarios={stats['scenarios']}"


@then('searching for "{tag}" scenarios should find at least {count:d}')
def step_find_by_tag(context, tag, count):
    scenarios = context.model_project.find_scenarios(tag=tag)
    assert len(scenarios) >= count, f"found {len(scenarios)} scenarios for {tag}"


@then("validation should complete with a list of issues")
def step_validate(context):
    issues = Validator().validate(context.model_project)
    assert isinstance(issues, list)
