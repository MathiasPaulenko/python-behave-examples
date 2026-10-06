# Feature: behave-data
# Demonstrates: typed table columns (name:str, age:int, active:bool,
#   price:float, created:date), null resolution for empty cells, and
#   typed_wrap()/typed_dicts(). Wired via setup_data() + hooks in
#   environment.py.
@data @unit
Feature: behave-data typed tables
  As a test author
  I want table cells converted to real Python types
  So that assertions need no manual parsing

  # Column headers carry a type suffix — cells arrive already converted:
  # "42" -> 42, "true" -> True, empty cell -> None.
  @smoke
  Scenario: Typed column conversion
    When I read the typed users table:
      | name:str | age:int | active:bool | price:float |
      | Alice    | 30      | true        | 9.99        |
      | Bob      | 42      | false       | 4.50        |
    Then the first row's age should be int 30
    And the second row's active should be bool false
    And the first row's price should be float 9.99

  # Empty cells resolve to None instead of "".
  Scenario: Null resolution
    When I read the typed users table:
      | name:str | age:int | city:str |
      | Alice    | 30      | Berlin   |
      | Bob      |         |          |
    Then Bob's age should be None
    And Bob's city should be None

  # Date columns convert to datetime.date objects.
  Scenario: Date type conversion
    When I read the typed users table:
      | name:str | created:date |
      | Alice    | 2026-01-15   |
    Then the created date should be year 2026 and month 1
