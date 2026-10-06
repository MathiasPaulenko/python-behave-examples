# Feature: behave-retry
# Demonstrates: automatic retry of failed scenarios — @flaky restricts
#   retrying to tagged scenarios, @retry:N overrides the global
#   max_retries=2 configured in environment.py via setup_retry().
#   after_all prints the flakiness report via retry_report().
@retry_lib @unit
Feature: behave-retry automatic retries
  As a test author
  I want flaky scenarios retried automatically
  So that transient failures don't break the suite

  # This scenario deterministically fails on attempt 1 and passes on
  # attempt 2 (a module-level counter survives the re-run). It proves
  # real re-execution: the retry report counts 1 retried scenario.
  @flaky @smoke
  Scenario: A flaky scenario passes on the second attempt
    When a step fails on its first attempt
    Then the scenario should pass after retrying

  # @retry:0 disables retries for this scenario even though it is @flaky.
  @flaky @retry:0
  Scenario: Per-scenario retry override disables retrying
    Then this scenario simply passes
