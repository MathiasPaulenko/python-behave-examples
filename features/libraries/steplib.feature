# Feature: behave-steplib
# Demonstrates: pre-built steps from the steplib api, data, io and cli
#   modules — no step code written in this project. Autoloaded via
#   steplib.behave.autoload(categories=[...], backends={"api": "requests"})
#   in environment.py.
# NOTE: steplib step patterns take unquoted arguments (e.g. /api/health),
#   which is different from the quoted steps defined in this repo.
@integration @steplib
Feature: behave-steplib reusable steps
  As a test author
  I want a library of ready-made step definitions
  So that common API/data/IO/CLI testing needs no step code

  Background:
    Given the API server is running
    And the users database is empty

  # API module: base url config, request, status + JSON path assertions.
  @smoke
  Scenario: API steps against the SUT
    Given the API base url is http://localhost:5000
    When I send a GET request to /api/health
    Then the response status is 200
    And the JSON path $.status equals ok

  # Data module: variable lifecycle — set, assert, compare.
  Scenario: Variable management steps
    Given I set the variable user_id to 42
    Then the variable user_id equals 42
    And the variable user_id is greater than 40

  # IO module: filesystem operations under a temp directory.
  Scenario: File and directory steps
    Given I create the directory output/steplib
    When I write hello steplib to the file output/steplib/demo.txt
    Then the file output/steplib/demo.txt exists
    When I delete the directory output
    Then the directory output does not exist

  # CLI module: run shell commands and assert on output.
  Scenario: Command execution steps
    When I run the command echo steplib-works using the default timeout
    Then the command exit code equals 0
    And the command output contains steplib-works
