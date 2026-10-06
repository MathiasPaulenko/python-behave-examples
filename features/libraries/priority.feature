# Feature: behave-priority
# Demonstrates: @priority(N) ordering (lower = earlier), @critical marking,
#   and the execution report printed by setup_priority(order=True,
#   report=True) in environment.py. Untagged scenarios run last.
@priority_lib @unit
Feature: behave-priority ordering
  As a CI maintainer
  I want critical scenarios to run first
  So that failures surface as early as possible

  # Lower number = higher priority. These scenarios are listed in
  # "wrong" order on purpose — the sorter reorders them at runtime and
  # the after_all report shows the actual execution order.
  @priority(3)
  Scenario: Low priority check runs third
    Then this scenario simply passes

  @critical @priority(1)
  Scenario: Critical check runs first
    Then this scenario simply passes

  @priority(2)
  Scenario: Medium priority check runs second
    Then this scenario simply passes
