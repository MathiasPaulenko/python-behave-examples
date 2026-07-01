# Feature: Calculator
# Demonstrates: Background, Scenario Outline with multiple Examples tables,
#   tags (@smoke, @negative, @math), error handling assertions.
@calculator @unit
Feature: Calculator
  As a user
  I want to perform arithmetic operations
  So that I can verify behave's Background and Scenario Outline support

  # Background runs before every scenario in this feature.
  # Ensures a fresh calculator instance with accumulator = 0.
  Background:
    Given I have a calculator
    And the calculator is reset

  # Simple scenario with two consecutive additions.
  @smoke
  Scenario: Adding two numbers
    When I add 5 to the calculator
    And I add 3 to the calculator
    Then the result should be 8
    And the last operation should be "add"

  # Verifies that dividing by zero raises a ZeroDivisionError
  # rather than crashing the test runner.
  @negative
  Scenario: Division by zero raises an error
    When I add 10 to the calculator
    And I divide the calculator by 0
    Then a ZeroDivisionError should be raised

  # Scenario Outline with TWO Examples tables.
  # Each row in an Examples table generates a new scenario.
  # Placeholders <start>, <operation>, <value>, <expected>, <op_name>
  # are replaced with the column values at runtime.
  @smoke
  Scenario Outline: Arithmetic operations with two operands
    Given the calculator accumulator is <start>
    When I <operation> <value> to the calculator
    Then the result should be <expected>
    And the last operation should be "<op_name>"

    Examples: Basic arithmetic
      | start | operation | value | expected | op_name   |
      | 0     | add       | 5     | 5        | add       |
      | 10    | subtract  | 4     | 6        | subtract  |
      | 3     | multiply  | 4     | 12       | multiply  |
      | 20    | divide    | 4     | 5        | divide    |

    Examples: Edge cases
      | start | operation | value | expected | op_name  |
      | 0     | add       | 0     | 0        | add      |
      | 100   | divide    | 100   | 1        | divide   |
      | -5    | multiply  | -2    | 10       | multiply |

  # Square root of a positive number — happy path.
  @math
  Scenario: Square root of a positive number
    When I add 16 to the calculator
    And I take the square root
    Then the result should be 4

  # Square root of a negative number — error path.
  # Combines two tags: @math and @negative.
  @math @negative
  Scenario: Square root of a negative number raises an error
    When I add -9 to the calculator
    And I take the square root
    Then a ValueError should be raised
