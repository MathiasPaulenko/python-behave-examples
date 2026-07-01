# Feature: Users REST API
# Demonstrates: REST API testing with the requests library against a real
#   Flask server (started in a background thread by environment.py),
#   data tables (vertical key-value format), pagination, CRUD operations,
#   Scenario Outline, Background, tags (@smoke, @negative, @api, @integration).
@api @integration
Feature: Users REST API
  As an API consumer
  I want to manage users via a REST API
  So that I can demonstrate behave testing against a real HTTP server

  # Background: runs before every scenario in this feature.
  # Ensures the SUT server is alive and the database is clean.
  Background:
    Given the API server is running
    And the users database is empty

  # Simple health check endpoint.
  @smoke
  Scenario: Health check
    When I send a GET request to "/api/health"
    Then the response status should be 200
    And the response field "status" should be "ok"

  # Create a user using a vertical data table (field|value format).
  # The first row is the header; subsequent rows are key-value pairs.
  @smoke
  Scenario: Create a user with a data table
    When I send a POST request to "/api/users" with:
      | field | value            |
      | name  | Test User        |
      | email | test@example.com |
      | role  | admin            |
    Then the response status should be 201
    And the response should contain "id"
    And the response field "name" should be "Test User"
    And the response field "email" should be "test@example.com"

  # Validation: empty name and email should return 400.
  @negative
  Scenario: Create a user without required fields
    When I send a POST request to "/api/users" with:
      | field | value |
      | name  |       |
      | email |       |
    Then the response status should be 400
    And the response field "error" should be "name and email are required"

  # Uniqueness constraint: duplicate email returns 409 Conflict.
  @negative
  Scenario: Duplicate email is rejected
    Given a user exists with email "dup@example.com"
    When I send a POST request to "/api/users" with:
      | field | value           |
      | name  | Another User    |
      | email | dup@example.com |
    Then the response status should be 409
    And the response field "error" should be "email already exists"

  # Pagination: the API supports ?page=N&limit=M query parameters.
  # The response includes "data" (array) and "total" (int).
  Scenario: List users with pagination
    Given the following users exist:
      | name   | email             | role   |
      | User 1 | u1@example.com    | viewer |
      | User 2 | u2@example.com    | viewer |
      | User 3 | u3@example.com    | viewer |
    When I send a GET request to "/api/users?page=1&limit=2"
    Then the response status should be 200
    And the response should contain at most 2 items
    And the response field "total" should be 3

  # GET by id — happy path using the created user endpoint.
  Scenario: Get a user by id
    Given a user exists with email "getme@example.com"
    When I send a GET request to the created user endpoint
    Then the response status should be 200
    And the response field "email" should be "getme@example.com"

  # DELETE returns 204 No Content on success.
  Scenario: Delete a user returns 204
    Given a user exists with email "deleteme@example.com"
    When I send a DELETE request to the created user endpoint
    Then the response status should be 204

  # GET by id — error path: non-existent user returns 404.
  @negative
  Scenario: Get a non-existent user returns 404
    When I send a GET request to "/api/users/9999"
    Then the response status should be 404
    And the response field "error" should be "not found"

  # Scenario Outline: parameterized role-based user creation.
  # Each row in Examples generates a scenario that creates a user
  # with a specific role and verifies the role in the response.
  Scenario Outline: Role-based user creation
    When I send a POST request to "/api/users" with:
      | field | value   |
      | name  | <name>  |
      | email | <email> |
      | role  | <role>  |
    Then the response status should be 201
    And the response field "role" should be "<role>"

    Examples:
      | name      | email              | role   |
      | Admin 1   | admin1@example.com | admin  |
      | Editor 1  | edit1@example.com  | editor |
      | Viewer 1  | view1@example.com  | viewer |
