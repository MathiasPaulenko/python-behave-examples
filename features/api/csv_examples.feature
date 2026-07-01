# Feature: External CSV examples
# Demonstrates: loading Examples table data from an external CSV file
#   instead of embedding it inline in the feature file.
#   The path in "Examples:" is relative to the feature file location.
@csv @integration
Feature: External CSV examples
  As a tester
  I want to load Examples table data from a CSV file
  So that I can keep large data sets outside the feature file

  # The Examples table is loaded from ../../support/data/users.csv
  # (relative to this feature file's directory: features/api/).
  # The CSV must have a header row matching the placeholder names.
  @smoke
  Scenario Outline: User data loaded from CSV
    Given a user named "<name>" with email "<email>"
    When I send a POST request to "/api/users" with:
      | field | value   |
      | name  | <name>  |
      | email | <email> |
      | role  | <role>  |
    Then the response status should be 201
    And the response field "name" should be "<name>"

    Examples: ../../support/data/users.csv
