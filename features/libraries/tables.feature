# Feature: behave-tables
# Demonstrates: wrap() — as_dicts, as_models (dataclass), column, find_row,
#   find_all_rows, select, sort, unique, count, to_csv, to_json, transpose.
@tables @unit
Feature: behave-tables data table API
  As a test author
  I want a polished API over context.table
  So that table handling needs no boilerplate

  @smoke
  Scenario: Converting a table to dicts and models
    When I wrap the following users table:
      | name  | age | city   |
      | Alice | 30  | Berlin |
      | Bob   | 25  | Madrid |
      | Carol | 35  | Rome   |
    Then the table has 3 rows as dicts
    And converting to dataclass models gives 3 users
    And the "name" column is "Alice, Bob, Carol"

  Scenario: Querying rows
    When I wrap the following users table:
      | name  | age | city   |
      | Alice | 30  | Berlin |
      | Bob   | 25  | Madrid |
      | Carol | 35  | Rome   |
    Then find_row name=Bob returns age "25"
    And find_all_rows with city "Rome" returns 1 row
    And count with age "30" is 1
    And first row name is "Alice" and last row name is "Carol"

  Scenario: Transforming tables
    When I wrap the following users table:
      | name  | age | city   |
      | Alice | 30  | Berlin |
      | Bob   | 25  | Madrid |
      | Carol | 35  | Rome   |
    Then select "name" gives a 1-column table
    And sorting by "age" descending starts with "Carol"
    And unique "city" returns "Berlin, Madrid, Rome"

  Scenario: Exporting tables
    When I wrap the following users table:
      | name  | age |
      | Alice | 30  |
      | Bob   | 25  |
    Then to_csv produces "name,age" headers
    And to_json produces a 2-element array
    And a CSV round-trip restores the table
