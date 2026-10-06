# Feature: Dynamic Examples from external data
# Demonstrates: loading Scenario Outline rows from an external CSV file
#   via behave-data's @load_examples:<source> tag. The named source
#   "users_csv" is declared in behave_data.yml and resolves to
#   features/support/data/users.csv.
#   (Behave itself does NOT support "Examples: <path>" — the path would be
#   parsed as the Examples name and generate zero scenarios.)
@csv @integration
Feature: Dynamic Examples from external data
  As a tester
  I want to load Examples table data from a CSV file
  So that large data sets live outside the feature file

  # @load_examples:users_csv replaces the Examples table below with the
  # CSV rows — one scenario is generated per data row. The table must
  # declare its headers; the placeholder row is overwritten by the loader.
  @load_examples:users_csv @smoke
  Scenario Outline: User data loaded from CSV
    Given the API server is running
    And the users database is empty
    When I send a POST request to "/api/users" with:
      | field | value   |
      | name  | <name>  |
      | email | <email> |
      | role  | <role>  |
    Then the response status should be 201
    And the response field "name" should be "<name>"

    Examples:
      | name        | email       | role  |
      | placeholder | placeholder | guest |
