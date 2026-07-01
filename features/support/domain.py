"""
Domain helpers exercised by the non-API feature files.

These are intentionally simple so that the focus stays on demonstrating
Behave / Gherkin capabilities (Background, Rule, Scenario Outline,
data tables, DocStrings, tags, async steps, etc.).
"""
from __future__ import annotations

import asyncio
import math
import re
from dataclasses import dataclass, field


# --------------------------------------------------------------------- #
#  Calculator
# --------------------------------------------------------------------- #
class Calculator:
    """A tiny calculator with memory (accumulator).

    Supports add, subtract, multiply, divide, and square root.
    Tracks the last operation performed in ``last_operation``.
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        """Resets the accumulator to 0 and clears ``last_operation``."""
        self.accumulator: float = 0.0
        self.last_operation: str | None = None

    def add(self, value: float) -> float:
        """Adds ``value`` to the accumulator and returns the new value."""
        self.accumulator += value
        self.last_operation = "add"
        return self.accumulator

    def subtract(self, value: float) -> float:
        """Subtracts ``value`` from the accumulator and returns the new value."""
        self.accumulator -= value
        self.last_operation = "subtract"
        return self.accumulator

    def multiply(self, value: float) -> float:
        """Multiplies the accumulator by ``value`` and returns the new value."""
        self.accumulator *= value
        self.last_operation = "multiply"
        return self.accumulator

    def divide(self, value: float) -> float:
        """Divides the accumulator by ``value`` and returns the new value.

        Raises:
            ZeroDivisionError: if ``value`` is 0.
        """
        if value == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        self.accumulator /= value
        self.last_operation = "divide"
        return self.accumulator

    def sqrt(self) -> float:
        """Replaces the accumulator with its square root.

        Raises:
            ValueError: if the accumulator is negative.
        """
        if self.accumulator < 0:
            raise ValueError("Cannot take square root of a negative number")
        self.accumulator = math.sqrt(self.accumulator)
        self.last_operation = "sqrt"
        return self.accumulator

    def result(self) -> float:
        """Returns the current accumulator value."""
        return self.accumulator


# --------------------------------------------------------------------- #
#  StringUtils
# --------------------------------------------------------------------- #
class StringUtils:
    """String manipulation utilities used by the Rule-based feature.

    All methods are static — no instance state is needed.
    """

    @staticmethod
    def reverse(text: str) -> str:
        """Returns ``text`` reversed (e.g. "behave" → "evaheb")."""
        return text[::-1]

    @staticmethod
    def is_palindrome(text: str) -> bool:
        """Returns ``True`` if ``text`` is a palindrome.

        Comparison ignores case, punctuation, and whitespace.
        Examples:
            "racecar" → True
            "A man, a plan, a canal: Panama" → True
            "behave" → False
        """
        cleaned = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
        return cleaned == cleaned[::-1]

    @staticmethod
    def count_vowels(text: str) -> int:
        """Counts vowels (a, e, i, o, u) in ``text`` case-insensitively."""
        return sum(1 for ch in text.lower() if ch in "aeiou")

    @staticmethod
    def to_title_case(text: str) -> str:
        """Converts ``text`` to title case (first letter of each word uppercase)."""
        return text.title()

    @staticmethod
    def slugify(text: str) -> str:
        """Converts ``text`` to a URL-friendly slug.

        Removes non-word characters, converts to lowercase, and replaces
        spaces/underscores with hyphens.
        Example: "Hello World! This is Behave 101" → "hello-world-this-is-behave-101"
        """
        slug = re.sub(r"[^\w\s-]", "", text).strip().lower()
        return re.sub(r"[\s_]+", "-", slug)


# --------------------------------------------------------------------- #
#  ShoppingCart
# --------------------------------------------------------------------- #
@dataclass
class CartItem:
    """Represents a single line item in the shopping cart.

    Attributes:
        name: The product name (used as the key for deduplication).
        price: The unit price.
        quantity: The number of units.
    """

    name: str
    price: float
    quantity: int

    @property
    def subtotal(self) -> float:
        """Returns ``price * quantity`` rounded to 2 decimal places."""
        return round(self.price * self.quantity, 2)


@dataclass
class ShoppingCart:
    """A shopping cart with discount and tax support.

    Attributes:
        items: List of ``CartItem`` objects.
        discount_percent: Discount percentage (0-100).
        tax_percent: Tax percentage (0-100).
    """

    items: list[CartItem] = field(default_factory=list)
    discount_percent: float = 0.0
    tax_percent: float = 0.0

    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        """Adds an item to the cart.

        If an item with the same name already exists, its quantity is
        incremented rather than creating a duplicate entry.
        """
        for item in self.items:
            if item.name == name:
                item.quantity += quantity
                return
        self.items.append(CartItem(name=name, price=price, quantity=quantity))

    def remove_item(self, name: str) -> None:
        """Removes all items with the given ``name`` (no-op if not found)."""
        self.items = [i for i in self.items if i.name != name]

    def subtotal(self) -> float:
        """Returns the sum of all item subtotals, rounded to 2 decimals."""
        return round(sum(i.subtotal for i in self.items), 2)

    def discount_amount(self) -> float:
        """Returns the discount amount (subtotal * discount_percent / 100)."""
        return round(self.subtotal() * (self.discount_percent / 100), 2)

    def taxed_base(self) -> float:
        """Returns the base after discount (subtotal - discount_amount)."""
        return round(self.subtotal() - self.discount_amount(), 2)

    def tax_amount(self) -> float:
        """Returns the tax amount (taxed_base * tax_percent / 100)."""
        return round(self.taxed_base() * (self.tax_percent / 100), 2)

    def total(self) -> float:
        """Returns the final total (taxed_base + tax_amount)."""
        return round(self.taxed_base() + self.tax_amount(), 2)

    def item_count(self) -> int:
        """Returns the total quantity of all items in the cart."""
        return sum(i.quantity for i in self.items)


# --------------------------------------------------------------------- #
#  Async worker (for async-step demonstration)
# --------------------------------------------------------------------- #
async def async_fetch_value(key: str) -> str:
    """Simulates an async I/O call returning a value for a key."""
    await asyncio.sleep(0.05)
    mapping = {"hello": "world", "behave": "rocks", "python": "3.12"}
    return mapping.get(key, "<unknown>")


async def async_double(value: int) -> int:
    """Simulates an async computation that doubles ``value``."""
    await asyncio.sleep(0.01)
    return value * 2
