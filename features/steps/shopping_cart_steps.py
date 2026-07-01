"""
Step definitions for the Shopping cart feature.

Corresponds to ``features/shopping_cart/shopping_cart.feature`` which
demonstrates data tables (step-level), DocStrings (triple-quoted blocks),
and Scenario Outline with embedded data tables.

The ``ShoppingCart`` instance is created in ``before_scenario`` and stored
in ``context.cart``.

Note: Steps that accept a data table or DocString MUST end with a colon
(``:``) in behave 1.3.x — the framework no longer strips trailing colons.
"""
from __future__ import annotations

from behave import given, when, then


@given("I have an empty shopping cart")
def step_empty_cart(context):
    """Clears all items, discount, and tax from the cart."""
    context.cart.items.clear()
    context.cart.discount_percent = 0.0
    context.cart.tax_percent = 0.0


@when("I add the following items to the cart:")
def step_add_items_table(context):
    """Adds items from a data table to the cart.

    The table must have columns: ``name``, ``price``, ``quantity``.
    The first row is the header (column names).
    """
    for row in context.table:
        context.cart.add_item(
            name=row["name"],
            price=float(row["price"]),
            quantity=int(row["quantity"]),
        )


@when('I remove "{name}" from the cart')
def step_remove_item(context, name):
    """Removes the item with the given ``name`` from the cart.

    If the item does not exist, the cart remains unchanged (idempotent).
    """
    context.cart.remove_item(name)


@given("the cart has a discount of {discount:d}% and a tax of {tax:d}%")
def step_set_discount_tax(context, discount, tax):
    """Sets the discount and tax percentages on the cart."""
    context.cart.discount_percent = float(discount)
    context.cart.tax_percent = float(tax)


@then("the cart should contain {count:d} items")
def step_cart_count(context, count):
    """Asserts that the total number of items (including quantities) equals ``count``."""
    assert context.cart.item_count() == count, (
        f"Expected {count} items, got {context.cart.item_count()}"
    )


@then("the subtotal should be {expected:f}")
def step_subtotal(context, expected):
    """Asserts that the cart subtotal (sum of item subtotals) equals ``expected``."""
    assert context.cart.subtotal() == expected, (
        f"Expected subtotal {expected}, got {context.cart.subtotal()}"
    )


@then("the discount amount should be {expected:f}")
def step_discount_amount(context, expected):
    """Asserts that the discount amount equals ``expected``."""
    assert context.cart.discount_amount() == expected, (
        f"Expected discount {expected}, got {context.cart.discount_amount()}"
    )


@then("the tax amount should be {expected:f}")
def step_tax_amount(context, expected):
    """Asserts that the tax amount equals ``expected``."""
    assert context.cart.tax_amount() == expected, (
        f"Expected tax {expected}, got {context.cart.tax_amount()}"
    )


@then("the total should be {expected:f}")
def step_total(context, expected):
    """Asserts that the final total (subtotal - discount + tax) equals ``expected``."""
    assert context.cart.total() == expected, (
        f"Expected total {expected}, got {context.cart.total()}"
    )


@then("the receipt should be:")
def step_receipt_docstring(context):
    """Compares a DocString (``context.text``) against a generated receipt.

    The DocString content (triple-quoted block in the feature file) is
    available as ``context.text``. The step generates a receipt from the
    current cart state and compares it line-by-line.
    """
    expected = context.text.strip()
    lines = ["=== RECEIPT ==="]
    for item in context.cart.items:
        lines.append(f"{item.name:<5} x{item.quantity} = {item.subtotal:.2f}")
    lines.append("-" * 16)
    lines.append(f"TOTAL: {context.cart.total():.2f}")
    actual = "\n".join(lines)
    assert actual == expected, f"\n--- expected ---\n{expected}\n--- actual ---\n{actual}"
