"""
Step definitions for the behave-comments feature.

Corresponds to ``features/libraries/comments.feature`` and demonstrates
metadata annotation injection (``context.metadata``), typed doc-string
parsing via ``@with_parsed_text``, and steps referenced by
comment-declared lifecycle hooks.
"""
from __future__ import annotations

from behave import given, then
from behave_comments import with_parsed_text


def _metadata_values(context, scope):
    """Returns the list of {key, value} annotations for a scope."""
    metadata = getattr(context, "metadata", {})
    return metadata.get(scope, [])


@then('the feature metadata should contain owner "{expected}"')
def step_feature_owner(context, expected):
    entries = _metadata_values(context, "feature")
    owners = [e["value"] for e in entries if e.get("key") == "owner"]
    assert expected in owners, f"owner entries: {owners}"


@then('the scenario metadata should contain id "{expected}"')
def step_scenario_id(context, expected):
    entries = _metadata_values(context, "scenario")
    ids = [e["value"] for e in entries if e.get("key") == "id"]
    assert expected in ids, f"id entries: {ids}"


# --------------------------------------------------------------------- #
#  Typed doc string parsing
# --------------------------------------------------------------------- #
@given("a JSON user document:")
@with_parsed_text()
def step_json_document(context, text_block):
    """Parses the ``\"\"\"json`` doc string into a Python object.

    ``@with_parsed_text`` detects the content type declared on the doc
    string and injects a TextBlock; ``.parsed`` holds the real data.
    """
    context.doc = text_block.parsed


@then('the parsed document name should be "{expected}"')
def step_doc_name(context, expected):
    assert context.doc["name"] == expected


@then("the parsed document should have {count:d} roles")
def step_doc_roles(context, count):
    assert len(context.doc["roles"]) == count


# --------------------------------------------------------------------- #
#  Lifecycle hook steps (referenced by comments in the feature file)
# --------------------------------------------------------------------- #
@given("the lifecycle flag is set")
def step_lifecycle_flag_set(context):
    """Executed by the ``# @before-scenario:`` comment hook."""
    context.lifecycle_flag = True


@then("the lifecycle flag is cleared")
def step_lifecycle_flag_clear(context):
    """Executed by the ``# @after-scenario:`` comment hook."""
    context.lifecycle_flag = False


@then("the lifecycle flag should be set by the before hook")
def step_lifecycle_flag_check(context):
    """Asserts the comment-declared hook ran before this scenario."""
    assert context.lifecycle_flag is True
