# Feature: behave-kit
# Demonstrates: soft assertions, typed env() reads, get_path navigation,
#   wait_until polling, scoped attributes, @parameter_type converters,
#   and class-based steps (step_impl_base).
# Wired in environment.py via: kit_setup(context, env="test"),
#   kit_fixtures.setup_for_*, kit teardown(), and kit_suggestions.
@kit @unit
Feature: behave-kit utilities
  As a test author
  I want batteries-included helpers for assertions and context handling
  So that scenarios stay short and readable

  # Soft assertions collect ALL failures instead of stopping at the first
  # one. Failures are reported together by kit's teardown() in after_scenario.
  @smoke
  Scenario: Soft assertions collect several checks in one step
    When I check several conditions with soft assertions
    Then the soft assertion report should be clean

  # env() reads environment variables with type conversion and defaults.
  Scenario: Typed environment variable reads
    When I read the "KIT_DEMO_TIMEOUT" env var as int with default 30
    And I read the "KIT_DEMO_DEBUG" env var as bool with default true
    Then the env results should be 30 and true

  # get_path() navigates nested dicts with dot notation, including indexes.
  Scenario: Navigating nested data with get_path
    Given I have a nested response payload
    Then get_path "user.address.city" should return "Berlin"
    And get_path "users.0.name" should return "Alice"

  # wait_until() polls a condition until it holds or the timeout expires.
  Scenario: Polling a condition with wait_until
    When I wait until the counter reaches 3
    Then the wait should have succeeded

  # @parameter_type registers a converter usable in step patterns, and
  # @scoped auto-deletes the attribute when the scenario ends.
  Scenario: Custom parameter type and scoped attribute
    When I log in as "alice@example.com" using the kit Email type
    Then the parsed email should have domain "example.com"
    And the attribute should be scoped for cleanup

  # Class-based steps: steps are methods; self.context is bound and a
  # fresh instance is created per scenario.
  Scenario: Class-based step implementation
    Given I have a class-based account with balance 100
    When the class-based account deposits 50
    Then the class-based balance should be 150
