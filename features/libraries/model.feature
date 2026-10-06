# Feature: behave-model
# Demonstrates: load_project() over this very repo's features/ directory —
#   statistics, tag-filtered scenario search, and the Validator rule
#   framework. Meta-testing: the suite analyzes itself.
@model @unit
Feature: behave-model project model
  As a tooling author
  I want a canonical object model of the test suite
  So that analysis tools don't re-implement parsing

  @smoke
  Scenario: Loading the project and reading statistics
    When I load the behave project model for "features/"
    Then the project should contain at least 8 features
    And the project should contain at least 40 scenarios

  Scenario: Querying scenarios by tag
    When I load the behave project model for "features/"
    Then searching for "@smoke" scenarios should find at least 5

  Scenario: Validating the project
    When I load the behave project model for "features/"
    Then validation should complete with a list of issues
