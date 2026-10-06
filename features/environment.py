"""
Behave environment hooks — lifecycle management for the whole test run.

Demonstrates:
  * before_all  / after_all
  * before_feature / after_feature
  * before_rule / after_rule          (Gherkin v6 Rule support)
  * before_scenario / after_scenario
  * before_step / after_step
  * context.add_cleanup (stack-based cleanup)
  * SUT server start/stop

It also wires the ecosystem libraries so their features are active in
every scenario:

  * behave-kit       — setup/teardown, fixture manager, step suggestions
  * behave-data      — typed tables, dynamic Examples, declarative tags
  * behave-retry     — retry failed scenarios (only for @flaky scenarios)
  * behave-priority  — priority ordering + execution report
  * behave-steplib   — reusable step library (api, data, io, cli categories)
  * behave-comments  — comment-driven metadata and lifecycle hooks
  * behave-trace     — attach log/error entries to the trace report
"""
from __future__ import annotations

import logging
import os
import sys

# Make the project root importable so that ``from features.support.*`` works
# in step files and environment hooks.
HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(HERE)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from features.support.app import start_server  # noqa: E402

logger = logging.getLogger("behave.examples")

# Silence Werkzeug/Flask request logging so it doesn't clutter console output.
logging.getLogger("werkzeug").setLevel(logging.ERROR)


# --------------------------------------------------------------------- #
#  Run-level hooks
# --------------------------------------------------------------------- #
def before_all(context):
    """Runs once before any feature.

    Wires every ecosystem library: behave-kit environment management,
    behave-data hooks, behave-retry, behave-priority ordering, behave-steplib
    step autoload, and behave-comments lifecycle/metadata support.
    """
    context.config.setup_logging(logging.WARNING)

    # -- behave-kit: env management, fixtures, suggestions, soft asserts --
    from behave_kit import setup as kit_setup

    kit_setup(context, env="test")

    # -- behave-data: typed tables, dynamic Examples, declarative tags --
    from behave_data import setup_data

    setup_data(context)

    # -- behave-retry: retry only scenarios tagged @flaky --
    from behave_retry import setup_retry

    setup_retry(context, max_retries=2, retry_tags=["@flaky"], retry_delay=0.1)

    # -- behave-priority: order scenarios by @priority(N), report at the end --
    from behave_priority import setup_priority

    setup_priority(context, order=True, report=True)

    # -- behave-steplib: autoload reusable steps (requests backend for API) --
    from steplib.behave import autoload

    context.steplib = autoload(
        context,
        categories=["api", "data", "io", "cli"],
        backends={"api": "requests"},
    )

    # -- behave-comments: metadata annotations + comment lifecycle hooks --
    from behave_comments import run_before_all, setup_lifecycle_hooks_from_path

    setup_lifecycle_hooks_from_path(context, "features/")
    run_before_all(context)

    # -- SUT server for the API features --
    host = context.config.userdata.get("host", "localhost")
    port = int(context.config.userdata.get("port", 5000))
    context.api_url = f"http://{host}:{port}"

    logger.info("Starting SUT server on %s:%s", host, port)
    context.server = start_server(host=host, port=port)
    context.add_cleanup(_stop_server, context)

    # Shared counters — a plain dict so mutations survive context layer pops
    # (attributes assigned inside a scenario are discarded when it ends).
    context.run_stats = {"scenarios": 0, "steps": 0}


def after_all(context):
    """Runs once after all features."""
    stats = getattr(context, "run_stats", {})
    logger.info(
        "Test run finished — scenarios executed: %d, steps: %d",
        stats.get("scenarios", 0),
        stats.get("steps", 0),
    )

    # -- behave-retry: flakiness summary --
    from behave_retry import retry_report

    retry_report(context)

    # -- behave-priority: execution order report --
    from behave_priority import priority_report

    priority_report(context)

    # -- behave-comments --
    from behave_comments import run_after_all

    run_after_all(context)


def _stop_server(context):
    """Internal helper — shuts down the SUT server if it was started."""
    server = getattr(context, "server", None)
    if server is not None:
        logger.info("Stopping SUT server")
        server.shutdown()


# --------------------------------------------------------------------- #
#  Feature-level hooks
# --------------------------------------------------------------------- #
def before_feature(context, feature):
    """Runs before each feature."""
    logger.info("-- Feature: %s", feature.name)

    # -- behave-data: loads dynamic Examples (@load_examples:<source>) --
    from behave_data import before_feature_hook

    before_feature_hook(context, feature)

    # Behave only rebuilds outline scenarios when example.table.modified is
    # set; behave-data's row injection does not flag it, so mark the tables
    # here or stale (placeholder) rows would be used.
    for scenario in getattr(feature, "scenarios", []):
        for example in getattr(scenario, "examples", []):
            if example.table is not None:
                example.table.modified = True

    # -- behave-comments: inject # @key metadata + register hook comments --
    from behave_comments import (
        inject_metadata,
        run_before_feature,
        setup_lifecycle_hooks,
    )

    inject_metadata(context, feature)
    setup_lifecycle_hooks(context, feature)
    run_before_feature(context, feature)

    # -- behave-kit: feature-scoped fixtures --
    context.kit_fixtures.setup_for_feature(context, feature)


def after_feature(context, feature):
    """Runs after each feature."""
    logger.info("-- Feature done: %s (status=%s)", feature.name, feature.status)

    # -- behave-kit: feature-scoped fixtures and attributes --
    from behave_kit import teardown_feature

    teardown_feature(context)

    # -- behave-comments --
    from behave_comments import run_after_feature

    run_after_feature(context, feature)


# --------------------------------------------------------------------- #
#  Rule-level hooks (Gherkin v6)
# --------------------------------------------------------------------- #
def before_rule(context, rule):
    """Runs before each Gherkin v6 Rule block."""
    logger.info("  | Rule: %s", rule.name)


def after_rule(context, rule):
    """Runs after each Gherkin v6 Rule block."""
    logger.info("  | Rule done: %s", rule.name)


# --------------------------------------------------------------------- #
#  Scenario-level hooks
# --------------------------------------------------------------------- #
def before_scenario(context, scenario):
    """Runs before each scenario.

    Creates fresh domain objects (Calculator, StringUtils, ShoppingCart)
    and stores them in ``context`` so steps can access them without
    worrying about state leakage between scenarios.
    """
    context.run_stats["scenarios"] += 1
    logger.info("  | Scenario: %s", scenario.name)

    # -- behave-data: declarative tags (@needs_data, @with_fixture, ...) --
    from behave_data import before_scenario_hook as data_before_scenario

    data_before_scenario(context, scenario)

    # -- behave-priority: skip scenario if fail-fast was triggered --
    from behave_priority import before_scenario_hook as priority_before_scenario

    priority_before_scenario(context, scenario)

    # -- behave-steplib: per-scenario variable/resource reset --
    context.steplib.reset()

    # -- behave-kit: tag-driven fixtures --
    context.kit_fixtures.setup_for_scenario(context, scenario)

    # -- behave-comments: @before-scenario comment steps --
    from behave_comments import run_before_scenario

    run_before_scenario(context, scenario)

    # fresh domain objects per scenario
    from features.support.domain import Calculator, ShoppingCart, StringUtils

    context.calculator = Calculator()
    context.string_utils = StringUtils()
    context.cart = ShoppingCart()
    context.async_results = {}


def after_scenario(context, scenario):
    """Runs after each scenario."""
    if scenario.status == "failed":
        logger.error("  | FAILED: %s", scenario.name)

    # -- behave-steplib: release per-scenario resources --
    context.steplib.cleanup()

    # -- behave-retry: record attempt stats --
    from behave_retry import after_scenario_hook as retry_after_scenario

    retry_after_scenario(context, scenario)

    # -- behave-priority: record result, evaluate fail-fast --
    from behave_priority import after_scenario_hook as priority_after_scenario

    priority_after_scenario(context, scenario)

    # -- behave-kit: fixture teardowns, scoped cleanup, soft-assert report --
    from behave_kit import teardown as kit_teardown

    kit_teardown(context)

    # -- behave-data: @cleanup_after tags --
    from behave_data import after_scenario_hook as data_after_scenario

    data_after_scenario(context, scenario)

    # -- behave-comments: @after-scenario comment steps --
    from behave_comments import run_after_scenario

    run_after_scenario(context, scenario)


# --------------------------------------------------------------------- #
#  Step-level hooks
# --------------------------------------------------------------------- #
def before_step(context, step):
    """Runs before each step."""
    context.run_stats["steps"] += 1

    # -- behave-data: dynamic step-data tags --
    from behave_data import before_step_hook as data_before_step

    data_before_step(context, step)

    # -- behave-comments: @before-step comment steps --
    from behave_comments import run_before_step

    run_before_step(context, step)


def after_step(context, step):
    """Runs after each step."""
    if step.status == "failed":
        logger.error("  | Step failed: %s", step.name)

        # -- behave-trace: record the failure in the trace report --
        from behave_trace import log as trace_log

        trace_log(context, f"Step failed: {step.name}")

    # -- behave-kit: "did you mean?" hints for undefined/failed steps --
    context.kit_suggestions(context, step)

    # -- behave-comments: @after-step comment steps --
    from behave_comments import run_after_step

    run_after_step(context, step)
