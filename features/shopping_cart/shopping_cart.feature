# Feature: Shopping cart
# Demonstrates: Data tables (step-level), DocStrings (triple-quoted blocks),
#   Scenario Outline with data table, Background, tags.
@shopping @unit
Feature: Shopping cart
  As a shopper
  I want to manage a shopping cart
  So that I can demonstrate data tables and DocStrings

  # Background: ensures every scenario starts with a clean cart.
  Background:
    Given I have an empty shopping cart

  # Data table: each row represents an item with name, price, and quantity.
  # The first row is the header (column names).
  @smoke
  Scenario: Adding items from a data table
    When I add the following items to the cart:
      | name    | price | quantity |
      | Apple   | 0.50  | 3        |
      | Banana  | 0.30  | 2        |
      | Milk    | 1.20  | 1        |
    Then the cart should contain 6 items
    And the subtotal should be 3.30

  # Scenario Outline: discount and tax are parameterized via Examples.
  # The data table inside the scenario is the same for every row,
  # but the expected values change based on the placeholders.
  @math
  Scenario Outline: Discount and tax calculation
    Given the cart has a discount of <discount>% and a tax of <tax>%
    When I add the following items to the cart:
      | name | price | quantity |
      | Book | 20.00 | 2        |
    Then the subtotal should be <subtotal>
    And the discount amount should be <discount_amount>
    And the tax amount should be <tax_amount>
    And the total should be <total>

    Examples:
      | discount | tax | subtotal | discount_amount | tax_amount | total |
      | 0        | 0   | 40.00    | 0.00            | 0.00       | 40.00 |
      | 10       | 10  | 40.00    | 4.00            | 3.60       | 39.60 |
      | 25       | 5   | 40.00    | 10.00           | 1.50       | 31.50 |

  # Removing a non-existent item should be a no-op (idempotent).
  @negative
  Scenario: Removing an item that does not exist
    When I add the following items to the cart:
      | name  | price | quantity |
      | Pen   | 1.50  | 2        |
    And I remove "Notebook" from the cart
    Then the cart should contain 2 items
    And the subtotal should be 3.00

  # DocString: the text between triple quotes ("""") is passed
  # to the step as context.text. Useful for multi-line expected output.
  @docstring
  Scenario: Receipt preview via DocString
    When I add the following items to the cart:
      | name  | price | quantity |
      | Pen   | 1.50  | 2        |
      | Book  | 12.00 | 1        |
    Then the receipt should be:
      """
      === RECEIPT ===
      Pen   x2 = 3.00
      Book  x1 = 12.00
      ----------------
      TOTAL: 15.00
      """
