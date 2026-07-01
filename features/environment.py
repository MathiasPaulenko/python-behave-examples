"""
Behave environment hooks — lifecycle management for the whole test run.

Demonstrates:
  * before_all  / after_all
  * before_feature / after_feature
  * before_rule / after_rule          (Gherkin v6 Rule support)
  * before_scenario / after_scenario
  * before_step / after_step
  * context.add_cleanup (stack-based cleanup)
  * active-tag support
  * SUT server start/stop
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
    """Runs once before any feature."""
    context.config.setup_logging(logging.WARNING)

    host = context.config.userdata.get("host", "localhost")
    port = int(context.config.userdata.get("port", 5000))
    context.api_url = f"http://{host}:{port}"

    logger.info("Starting SUT server on %s:%s", host, port)
    context.server = start_server(host=host, port=port)
    context.add_cleanup(_stop_server, context)

    # shared counters for demonstration
    context.scenario_count = 0
    context.step_count = 0


def after_all(context):
    """Runs once after all features."""
    logger.info(
        "Test run finished — scenarios executed: %d, steps: %d",
        getattr(context, "scenario_count", 0),
        getattr(context, "step_count", 0),
    )


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
    """Runs before each feature — logs the feature name."""
    logger.info("-- Feature: %s", feature.name)


def after_feature(context, feature):
    """Runs after each feature — logs the feature name and final status."""
    logger.info("-- Feature done: %s (status=%s)", feature.name, feature.status)


# --------------------------------------------------------------------- #
#  Rule-level hooks (Gherkin v6)
# --------------------------------------------------------------------- #
def before_rule(context, rule):
    """Runs before each Gherkin v6 Rule block — logs the rule name."""
    logger.info("  | Rule: %s", rule.name)


def after_rule(context, rule):
    """Runs after each Gherkin v6 Rule block — logs completion."""
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
    context.scenario_count += 1
    logger.info("  | Scenario: %s", scenario.name)

    # fresh domain objects per scenario
    from features.support.domain import Calculator, ShoppingCart, StringUtils

    context.calculator = Calculator()
    context.string_utils = StringUtils()
    context.cart = ShoppingCart()
    context.async_results = {}


def after_scenario(context, scenario):
    """Runs after each scenario — logs a warning if the scenario failed."""
    if scenario.status == "failed":
        logger.error("  | FAILED: %s", scenario.name)


# --------------------------------------------------------------------- #
#  Step-level hooks
# --------------------------------------------------------------------- #
def before_step(context, step):
    """Runs before each step — increments the step counter."""
    context.step_count += 1


def after_step(context, step):
    """Runs after each step — logs an error if the step failed."""
    if step.status == "failed":
        logger.error("  | Step failed: %s", step.name)
