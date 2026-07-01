# Feature: Async step support
# Demonstrates: async/await step definitions (native behave 1.3.x support),
#   Scenario Outline with async results, @smoke tags.
@async
Feature: Async step support
  As a developer
  I want to use async step definitions
  So that I can test asynchronous code with behave 1.3.x

  # Behave 1.3.x supports async def step functions natively.
  # The event loop is managed automatically by the framework.
  @smoke
  Scenario: Fetching a value asynchronously
    When I asynchronously fetch the value for "hello"
    Then the async result should be "world"

  # Scenario Outline: each row generates a scenario that
  # awaits an async call and checks the returned value.
  # The "<unknown>" placeholder tests the fallback path
  # when a key is not found in the async mapping.
  Scenario Outline: Async fetch with multiple keys
    When I asynchronously fetch the value for "<key>"
    Then the async result should be "<value>"

    Examples:
      | key    | value    |
      | hello  | world    |
      | behave | rocks    |
      | python | 3.12     |
      | unknown | <unknown> |

  # Async step that returns an integer (not a string).
  # The step definition uses {expected:d} type converter.
  @smoke
  Scenario: Doubling a number asynchronously
    When I asynchronously double the number 21
    Then the async result should be 42
