# 📋 Step Catalog

**Generated:** 2026-07-01 15:25:42

49 step definitions across 6 files · Given 11, Then 22, When 16

---

## Statistics

| Metric         | Value |
| -------------- | ----- |
| Total steps    | 49    |
| Files          | 6     |
| Parameterised  | 35    |
| With docstring | 49    |
| Regex patterns | 0     |

## Steps by Keyword

| Keyword | Count |
| ------- | ----- |
| Given   | 11    |
| Then    | 22    |
| When    | 16    |

## Steps by File

| File                   | Count |
| ---------------------- | ----- |
| api_steps.py           | 7     |
| async_steps.py         | 2     |
| calculator_steps.py    | 13    |
| common_steps.py        | 7     |
| shopping_cart_steps.py | 10    |
| string_utils_steps.py  | 10    |

---

## Step Definitions

<details>
<summary>🔵 Given: a user exists with email "{email}" — `step_user_exists`</summary>

#### Location

`api_steps.py:21`

#### Parameters

- `email`

#### Description

> Creates a user via POST and stores the id + endpoint for later steps.
> 
> The created user's endpoint is stored in ``context.created_user_endpoint``
> so that subsequent GET/DELETE steps can reference it.

#### Source

```python
def step_user_exists(context, email):
    """Creates a user via POST and stores the id + endpoint for later steps.

    The created user's endpoint is stored in ``context.created_user_endpoint``
    so that subsequent GET/DELETE steps can reference it.
    """
    resp = requests.post(
        f"{context.api_url}/api/users",
        json={"name": "Temp User", "email": email, "role": "viewer"},
        timeout=2,
    )
    assert resp.status_code == 201, f"Could not create user: {resp.text}"
    context.created_user_id = resp.json()["id"]
    context.created_user_endpoint = f"/api/users/{context.created_user_id}"
```

</details>

<details>
<summary>🔵 Given: the following users exist: — `step_users_exist_table`</summary>

#### Location

`api_steps.py:38`

#### Description

> Creates multiple users from a horizontal data table.
> 
> The table must have columns: ``name``, ``email``, ``role``.
> Each row represents one user to create via POST.

#### Source

```python
def step_users_exist_table(context):
    """Creates multiple users from a horizontal data table.

    The table must have columns: ``name``, ``email``, ``role``.
    Each row represents one user to create via POST.
    """
    for row in context.table:
        resp = requests.post(
            f"{context.api_url}/api/users",
            json={"name": row["name"], "email": row["email"], "role": row["role"]},
            timeout=2,
        )
        assert resp.status_code == 201, f"Could not create user {row}: {resp.text}"
```

</details>

<details>
<summary>🔵 Given: a user named "{name}" with email "{email}" — `step_user_named`</summary>

#### Location

`api_steps.py:54`

#### Parameters

- `name`
- `email`

#### Description

> Stores pending user data for use in a subsequent POST step.
> 
> Used by the CSV examples feature where the user data comes from
> an external CSV file.

#### Source

```python
def step_user_named(context, name, email):
    """Stores pending user data for use in a subsequent POST step.

    Used by the CSV examples feature where the user data comes from
    an external CSV file.
    """
    context.pending_user = {"name": name, "email": email}
```

</details>

<details>
<summary>🟡 When: I send a {method} request to "{url}" — `step_send_request`</summary>

#### Location

`api_steps.py:64`

#### Parameters

- `method`
- `url`

#### Description

> Sends an HTTP request with no body and stores the response.
> 
> ``method`` is injected from the step text (GET, POST, DELETE, etc.).
> The response is stored in ``context.response``.

#### Source

```python
def step_send_request(context, method, url):
    """Sends an HTTP request with no body and stores the response.

    ``method`` is injected from the step text (GET, POST, DELETE, etc.).
    The response is stored in ``context.response``.
    """
    context.response = requests.request(
        method,
        f"{context.api_url}{url}",
        timeout=2,
    )
```

</details>

<details>
<summary>🟡 When: I send a {method} request to "{url}" with: — `step_send_request_with_table`</summary>

#### Location

`api_steps.py:78`

#### Parameters

- `method`
- `url`

#### Description

> Sends an HTTP request with a JSON body built from a vertical data table.
> 
> The table must have columns: ``field``, ``value``.
> Each row becomes a key-value pair in the JSON payload.

#### Source

```python
def step_send_request_with_table(context, method, url):
    """Sends an HTTP request with a JSON body built from a vertical data table.

    The table must have columns: ``field``, ``value``.
    Each row becomes a key-value pair in the JSON payload.
    """
    data = {row["field"]: row["value"] for row in context.table.rows}
    context.response = requests.request(
        method,
        f"{context.api_url}{url}",
        json=data,
        timeout=2,
    )
```

</details>

<details>
<summary>🟡 When: I send a GET request to the created user endpoint — `step_get_created_user`</summary>

#### Location

`api_steps.py:94`

#### Description

> GETs the user created by a preceding ``Given a user exists`` step.

#### Source

```python
def step_get_created_user(context):
    """GETs the user created by a preceding ``Given a user exists`` step."""
    context.response = requests.get(
        f"{context.api_url}{context.created_user_endpoint}",
        timeout=2,
    )
```

</details>

<details>
<summary>🟡 When: I send a DELETE request to the created user endpoint — `step_delete_created_user`</summary>

#### Location

`api_steps.py:103`

#### Description

> DELETEs the user created by a preceding ``Given a user exists`` step.

#### Source

```python
def step_delete_created_user(context):
    """DELETEs the user created by a preceding ``Given a user exists`` step."""
    context.response = requests.delete(
        f"{context.api_url}{context.created_user_endpoint}",
        timeout=2,
    )
```

</details>

<details>
<summary>🟢 Then: the async result should be "{expected}" — `step_async_result_str`</summary>

#### Location

`async_steps.py:40`

#### Parameters

- `expected`

#### Description

> Asserts that the last async result (as a string) equals ``expected``.
> 
> This step is synchronous — it reads from ``context.async_results``
> which was populated by a preceding async ``When`` step.

#### Source

```python
def step_async_result_str(context, expected):
    """Asserts that the last async result (as a string) equals ``expected``.

    This step is synchronous — it reads from ``context.async_results``
    which was populated by a preceding async ``When`` step.
    """
    last_key = list(context.async_results.keys())[-1]
    actual = str(context.async_results[last_key])
    assert actual == expected, f"Expected '{expected}', got '{actual}'"
```

</details>

<details>
<summary>🟢 Then: the async result should be {expected:d} — `step_async_result_int`</summary>

#### Location

`async_steps.py:52`

#### Parameters

- `expected:d`

#### Description

> Asserts that the last async result (as an integer) equals ``expected``.
> 
> Uses the ``{expected:d}`` type converter so behave parses the integer
> automatically from the step text.

#### Source

```python
def step_async_result_int(context, expected):
    """Asserts that the last async result (as an integer) equals ``expected``.

    Uses the ``{expected:d}`` type converter so behave parses the integer
    automatically from the step text.
    """
    last_key = list(context.async_results.keys())[-1]
    actual = context.async_results[last_key]
    assert actual == expected, f"Expected {expected}, got {actual}"
```

</details>

<details>
<summary>🔵 Given: I have a calculator — `step_have_calculator`</summary>

#### Location

`calculator_steps.py:18`

#### Description

> Verifies that a Calculator instance was injected by the environment.

#### Source

```python
def step_have_calculator(context):
    """Verifies that a Calculator instance was injected by the environment."""
    assert context.calculator is not None
```

</details>

<details>
<summary>🔵 Given: the calculator is reset — `step_reset`</summary>

#### Location

`calculator_steps.py:24`

#### Description

> Resets the calculator accumulator to 0 and clears the last operation.

#### Source

```python
def step_reset(context):
    """Resets the calculator accumulator to 0 and clears the last operation."""
    context.calculator.reset()
```

</details>

<details>
<summary>🔵 Given: the calculator accumulator is {value:d} — `step_set_accumulator`</summary>

#### Location

`calculator_steps.py:30`

#### Parameters

- `value:d`

#### Description

> Sets the accumulator to an explicit value (used by Scenario Outlines).

#### Source

```python
def step_set_accumulator(context, value):
    """Sets the accumulator to an explicit value (used by Scenario Outlines)."""
    context.calculator.accumulator = float(value)
```

</details>

<details>
<summary>🟡 When: I add {value:d} to the calculator — `step_add`</summary>

#### Location

`calculator_steps.py:36`

#### Parameters

- `value:d`

#### Description

> Adds ``value`` to the accumulator.

#### Source

```python
def step_add(context, value):
    """Adds ``value`` to the accumulator."""
    context.calculator.add(float(value))
```

</details>

<details>
<summary>🟡 When: I subtract {value:d} to the calculator — `step_subtract`</summary>

#### Location

`calculator_steps.py:42`

#### Parameters

- `value:d`

#### Description

> Subtracts ``value`` from the accumulator.

#### Source

```python
def step_subtract(context, value):
    """Subtracts ``value`` from the accumulator."""
    context.calculator.subtract(float(value))
```

</details>

<details>
<summary>🟡 When: I multiply {value:d} to the calculator — `step_multiply`</summary>

#### Location

`calculator_steps.py:48`

#### Parameters

- `value:d`

#### Description

> Multiplies the accumulator by ``value``.

#### Source

```python
def step_multiply(context, value):
    """Multiplies the accumulator by ``value``."""
    context.calculator.multiply(float(value))
```

</details>

<details>
<summary>🟡 When: I divide the calculator by {value:d} — `step_divide`</summary>

#### Location

`calculator_steps.py:54`

#### Parameters

- `value:d`

#### Description

> Divides the accumulator by ``value``.
> 
> Catches ``ZeroDivisionError`` and stores it in ``context.exc``
> so a subsequent ``Then a ZeroDivisionError should be raised`` step
> can assert on it.

#### Source

```python
def step_divide(context, value):
    """Divides the accumulator by ``value``.

    Catches ``ZeroDivisionError`` and stores it in ``context.exc``
    so a subsequent ``Then a ZeroDivisionError should be raised`` step
    can assert on it.
    """
    try:
        context.calculator.divide(float(value))
        context.exc = None
    except Exception as e:
        context.exc = e
```

</details>

<details>
<summary>🟡 When: I divide {value:d} to the calculator — `step_divide_to`</summary>

#### Location

`calculator_steps.py:69`

#### Parameters

- `value:d`

#### Description

> Alternative phrasing for division (used by Scenario Outline rows).
> 
> Behave matches the literal step text, so both
> "I divide the calculator by 4" and "I divide 4 to the calculator"
> need their own step definition.

#### Source

```python
def step_divide_to(context, value):
    """Alternative phrasing for division (used by Scenario Outline rows).

    Behave matches the literal step text, so both
    "I divide the calculator by 4" and "I divide 4 to the calculator"
    need their own step definition.
    """
    try:
        context.calculator.divide(float(value))
        context.exc = None
    except Exception as e:
        context.exc = e
```

</details>

<details>
<summary>🟡 When: I take the square root — `step_sqrt`</summary>

#### Location

`calculator_steps.py:84`

#### Description

> Takes the square root of the current accumulator value.
> 
> Catches ``ValueError`` (negative input) and stores it in
> ``context.exc`` for later assertion.

#### Source

```python
def step_sqrt(context):
    """Takes the square root of the current accumulator value.

    Catches ``ValueError`` (negative input) and stores it in
    ``context.exc`` for later assertion.
    """
    try:
        context.calculator.sqrt()
        context.exc = None
    except Exception as e:
        context.exc = e
```

</details>

<details>
<summary>🟢 Then: the result should be {expected:d} — `step_result`</summary>

#### Location

`calculator_steps.py:98`

#### Parameters

- `expected:d`

#### Description

> Asserts that the accumulator equals ``expected``.

#### Source

```python
def step_result(context, expected):
    """Asserts that the accumulator equals ``expected``."""
    assert context.calculator.result() == float(expected), (
        f"Expected {expected}, got {context.calculator.result()}"
    )
```

</details>

<details>
<summary>🟢 Then: the last operation should be "{op_name}" — `step_last_op`</summary>

#### Location

`calculator_steps.py:106`

#### Parameters

- `op_name`

#### Description

> Asserts that ``last_operation`` matches the expected operation name.

#### Source

```python
def step_last_op(context, op_name):
    """Asserts that ``last_operation`` matches the expected operation name."""
    assert context.calculator.last_operation == op_name, (
        f"Expected '{op_name}', got '{context.calculator.last_operation}'"
    )
```

</details>

<details>
<summary>🟢 Then: a ZeroDivisionError should be raised — `step_zero_division`</summary>

#### Location

`calculator_steps.py:114`

#### Description

> Asserts that a ``ZeroDivisionError`` was caught during a previous step.

#### Source

```python
def step_zero_division(context):
    """Asserts that a ``ZeroDivisionError`` was caught during a previous step."""
    assert isinstance(context.exc, ZeroDivisionError), (
        f"Expected ZeroDivisionError, got {context.exc!r}"
    )
```

</details>

<details>
<summary>🟢 Then: a ValueError should be raised — `step_value_error`</summary>

#### Location

`calculator_steps.py:122`

#### Description

> Asserts that a ``ValueError`` was caught during a previous step.

#### Source

```python
def step_value_error(context):
    """Asserts that a ``ValueError`` was caught during a previous step."""
    assert isinstance(context.exc, ValueError), (
        f"Expected ValueError, got {context.exc!r}"
    )
```

</details>

<details>
<summary>🔵 Given: the API server is running — `step_api_running`</summary>

#### Location

`common_steps.py:42`

#### Description

> Verifies that the Flask SUT is reachable by hitting ``/api/health``.
> 
> The server is started in ``before_all`` (environment.py) in a
> background thread. This step acts as a smoke check before
> running API scenarios.

#### Source

```python
def step_api_running(context):
    """Verifies that the Flask SUT is reachable by hitting ``/api/health``.

    The server is started in ``before_all`` (environment.py) in a
    background thread. This step acts as a smoke check before
    running API scenarios.
    """
    import requests

    resp = requests.get(f"{context.api_url}/api/health", timeout=2)
    assert resp.ok, f"API server not reachable: {resp.status_code}"
```

</details>

<details>
<summary>🔵 Given: the users database is empty — `step_db_empty`</summary>

#### Location

`common_steps.py:56`

#### Description

> Deletes all users from the SUT to ensure a clean state.
> 
> Fetches all users via GET, then DELETEs each one individually.
> This guarantees test isolation between scenarios that share
> the same SUT instance.

#### Source

```python
def step_db_empty(context):
    """Deletes all users from the SUT to ensure a clean state.

    Fetches all users via GET, then DELETEs each one individually.
    This guarantees test isolation between scenarios that share
    the same SUT instance.
    """
    import requests

    resp = requests.get(f"{context.api_url}/api/users", timeout=2)
    assert resp.ok
    body = resp.json()
    for user in body.get("data", []):
        requests.delete(f"{context.api_url}/api/users/{user['id']}", timeout=2)
```

</details>

<details>
<summary>🟢 Then: the response status should be {status:d} — `step_response_status`</summary>

#### Location

`common_steps.py:73`

#### Parameters

- `status:d`

#### Description

> Asserts that the last HTTP response status code equals ``status``.
> 
> Uses ``{status:d}`` type converter to parse the integer from the step text.
> The response is stored in ``context.response`` by a preceding ``When`` step.

#### Source

```python
def step_response_status(context, status):
    """Asserts that the last HTTP response status code equals ``status``.

    Uses ``{status:d}`` type converter to parse the integer from the step text.
    The response is stored in ``context.response`` by a preceding ``When`` step.
    """
    assert context.response.status_code == status, (
        f"Expected status {status}, got {context.response.status_code}: "
        f"{context.response.text}"
    )
```

</details>

<details>
<summary>🟢 Then: the response should contain "{field}" — `step_response_contains`</summary>

#### Location

`common_steps.py:86`

#### Parameters

- `field`

#### Description

> Asserts that the JSON response body contains a top-level ``field`` key.

#### Source

```python
def step_response_contains(context, field):
    """Asserts that the JSON response body contains a top-level ``field`` key."""
    body = context.response.json()
    assert field in body, f"Response missing field '{field}': {body}"
```

</details>

<details>
<summary>🟢 Then: the response field "{field}" should be "{value}" — `step_response_field`</summary>

#### Location

`common_steps.py:93`

#### Parameters

- `field`
- `value`

#### Description

> Asserts that a string field in the JSON response equals ``value``.
> 
> Both ``field`` and ``value`` are captured as quoted strings.
> The actual value is converted to ``str`` before comparison.

#### Source

```python
def step_response_field(context, field, value):
    """Asserts that a string field in the JSON response equals ``value``.

    Both ``field`` and ``value`` are captured as quoted strings.
    The actual value is converted to ``str`` before comparison.
    """
    body = context.response.json()
    actual = str(body.get(field))
    assert actual == value, f"Field '{field}': expected '{value}', got '{actual}'"
```

</details>

<details>
<summary>🟢 Then: the response field "{field}" should be {value:d} — `step_response_field_int`</summary>

#### Location

`common_steps.py:105`

#### Parameters

- `field`
- `value:d`

#### Description

> Asserts that an integer field in the JSON response equals ``value``.
> 
> Uses ``{value:d}`` type converter so behave parses the integer
> automatically. This avoids quoting issues with numeric fields
> like ``total`` or ``count``.

#### Source

```python
def step_response_field_int(context, field, value):
    """Asserts that an integer field in the JSON response equals ``value``.

    Uses ``{value:d}`` type converter so behave parses the integer
    automatically. This avoids quoting issues with numeric fields
    like ``total`` or ``count``.
    """
    body = context.response.json()
    actual = body.get(field)
    assert actual == value, f"Field '{field}': expected {value}, got {actual}"
```

</details>

<details>
<summary>🟢 Then: the response should contain at most {count:d} items — `step_response_at_most`</summary>

#### Location

`common_steps.py:118`

#### Parameters

- `count:d`

#### Description

> Asserts that the ``data`` array in the response has at most ``count`` items.
> 
> Used for pagination testing — the API returns a ``data`` key with
> a slice of results and a ``total`` key with the full count.

#### Source

```python
def step_response_at_most(context, count):
    """Asserts that the ``data`` array in the response has at most ``count`` items.

    Used for pagination testing — the API returns a ``data`` key with
    a slice of results and a ``total`` key with the full count.
    """
    body = context.response.json()
    data = body.get("data", body)
    assert len(data) <= count, f"Expected at most {count} items, got {len(data)}"
```

</details>

<details>
<summary>🔵 Given: I have an empty shopping cart — `step_empty_cart`</summary>

#### Location

`shopping_cart_steps.py:20`

#### Description

> Clears all items, discount, and tax from the cart.

#### Source

```python
def step_empty_cart(context):
    """Clears all items, discount, and tax from the cart."""
    context.cart.items.clear()
    context.cart.discount_percent = 0.0
    context.cart.tax_percent = 0.0
```

</details>

<details>
<summary>🟡 When: I add the following items to the cart: — `step_add_items_table`</summary>

#### Location

`shopping_cart_steps.py:28`

#### Description

> Adds items from a data table to the cart.
> 
> The table must have columns: ``name``, ``price``, ``quantity``.
> The first row is the header (column names).

#### Source

```python
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
```

</details>

<details>
<summary>🟡 When: I remove "{name}" from the cart — `step_remove_item`</summary>

#### Location

`shopping_cart_steps.py:43`

#### Parameters

- `name`

#### Description

> Removes the item with the given ``name`` from the cart.
> 
> If the item does not exist, the cart remains unchanged (idempotent).

#### Source

```python
def step_remove_item(context, name):
    """Removes the item with the given ``name`` from the cart.

    If the item does not exist, the cart remains unchanged (idempotent).
    """
    context.cart.remove_item(name)
```

</details>

<details>
<summary>🔵 Given: the cart has a discount of {discount:d}% and a tax of {tax:d}% — `step_set_discount_tax`</summary>

#### Location

`shopping_cart_steps.py:52`

#### Parameters

- `discount:d`
- `tax:d`

#### Description

> Sets the discount and tax percentages on the cart.

#### Source

```python
def step_set_discount_tax(context, discount, tax):
    """Sets the discount and tax percentages on the cart."""
    context.cart.discount_percent = float(discount)
    context.cart.tax_percent = float(tax)
```

</details>

<details>
<summary>🟢 Then: the cart should contain {count:d} items — `step_cart_count`</summary>

#### Location

`shopping_cart_steps.py:59`

#### Parameters

- `count:d`

#### Description

> Asserts that the total number of items (including quantities) equals ``count``.

#### Source

```python
def step_cart_count(context, count):
    """Asserts that the total number of items (including quantities) equals ``count``."""
    assert context.cart.item_count() == count, (
        f"Expected {count} items, got {context.cart.item_count()}"
    )
```

</details>

<details>
<summary>🟢 Then: the subtotal should be {expected:f} — `step_subtotal`</summary>

#### Location

`shopping_cart_steps.py:67`

#### Parameters

- `expected:f`

#### Description

> Asserts that the cart subtotal (sum of item subtotals) equals ``expected``.

#### Source

```python
def step_subtotal(context, expected):
    """Asserts that the cart subtotal (sum of item subtotals) equals ``expected``."""
    assert context.cart.subtotal() == expected, (
        f"Expected subtotal {expected}, got {context.cart.subtotal()}"
    )
```

</details>

<details>
<summary>🟢 Then: the discount amount should be {expected:f} — `step_discount_amount`</summary>

#### Location

`shopping_cart_steps.py:75`

#### Parameters

- `expected:f`

#### Description

> Asserts that the discount amount equals ``expected``.

#### Source

```python
def step_discount_amount(context, expected):
    """Asserts that the discount amount equals ``expected``."""
    assert context.cart.discount_amount() == expected, (
        f"Expected discount {expected}, got {context.cart.discount_amount()}"
    )
```

</details>

<details>
<summary>🟢 Then: the tax amount should be {expected:f} — `step_tax_amount`</summary>

#### Location

`shopping_cart_steps.py:83`

#### Parameters

- `expected:f`

#### Description

> Asserts that the tax amount equals ``expected``.

#### Source

```python
def step_tax_amount(context, expected):
    """Asserts that the tax amount equals ``expected``."""
    assert context.cart.tax_amount() == expected, (
        f"Expected tax {expected}, got {context.cart.tax_amount()}"
    )
```

</details>

<details>
<summary>🟢 Then: the total should be {expected:f} — `step_total`</summary>

#### Location

`shopping_cart_steps.py:91`

#### Parameters

- `expected:f`

#### Description

> Asserts that the final total (subtotal - discount + tax) equals ``expected``.

#### Source

```python
def step_total(context, expected):
    """Asserts that the final total (subtotal - discount + tax) equals ``expected``."""
    assert context.cart.total() == expected, (
        f"Expected total {expected}, got {context.cart.total()}"
    )
```

</details>

<details>
<summary>🟢 Then: the receipt should be: — `step_receipt_docstring`</summary>

#### Location

`shopping_cart_steps.py:99`

#### Description

> Compares a DocString (``context.text``) against a generated receipt.
> 
> The DocString content (triple-quoted block in the feature file) is
> available as ``context.text``. The step generates a receipt from the
> current cart state and compares it line-by-line.

#### Source

```python
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
```

</details>

<details>
<summary>🔵 Given: I have the string utilities — `step_have_string_utils`</summary>

#### Location

`string_utils_steps.py:17`

#### Description

> Verifies that a ``StringUtils`` instance was injected by the environment.

#### Source

```python
def step_have_string_utils(context):
    """Verifies that a ``StringUtils`` instance was injected by the environment."""
    assert context.string_utils is not None
```

</details>

<details>
<summary>🟡 When: I reverse the string "{text}" — `step_reverse`</summary>

#### Location

`string_utils_steps.py:23`

#### Parameters

- `text`

#### Description

> Reverses ``text`` and stores the result in ``context.last_result``.

#### Source

```python
def step_reverse(context, text):
    """Reverses ``text`` and stores the result in ``context.last_result``."""
    context.last_input = text
    context.last_result = context.string_utils.reverse(text)
```

</details>

<details>
<summary>🟢 Then: the reversed string should be "{expected}" — `step_reversed_should_be`</summary>

#### Location

`string_utils_steps.py:30`

#### Parameters

- `expected`

#### Description

> Asserts that the last reversal result equals ``expected``.

#### Source

```python
def step_reversed_should_be(context, expected):
    """Asserts that the last reversal result equals ``expected``."""
    assert context.last_result == expected, (
        f"Expected '{expected}', got '{context.last_result}'"
    )
```

</details>

<details>
<summary>🟢 Then: the string "{text}" should be a palindrome — `step_is_palindrome`</summary>

#### Location

`string_utils_steps.py:38`

#### Parameters

- `text`

#### Description

> Asserts that ``text`` is a palindrome (ignoring case and punctuation).

#### Source

```python
def step_is_palindrome(context, text):
    """Asserts that ``text`` is a palindrome (ignoring case and punctuation)."""
    assert context.string_utils.is_palindrome(text), (
        f"'{text}' is not a palindrome"
    )
```

</details>

<details>
<summary>🟢 Then: the string "{text}" should not be a palindrome — `step_not_palindrome`</summary>

#### Location

`string_utils_steps.py:46`

#### Parameters

- `text`

#### Description

> Asserts that ``text`` is NOT a palindrome.

#### Source

```python
def step_not_palindrome(context, text):
    """Asserts that ``text`` is NOT a palindrome."""
    assert not context.string_utils.is_palindrome(text), (
        f"'{text}' was unexpectedly a palindrome"
    )
```

</details>

<details>
<summary>🟡 When: I count the vowels in "{text}" — `step_count_vowels`</summary>

#### Location

`string_utils_steps.py:54`

#### Parameters

- `text`

#### Description

> Counts vowels (a, e, i, o, u) in ``text`` case-insensitively.

#### Source

```python
def step_count_vowels(context, text):
    """Counts vowels (a, e, i, o, u) in ``text`` case-insensitively."""
    context.last_input = text
    context.last_result = context.string_utils.count_vowels(text)
```

</details>

<details>
<summary>🟢 Then: the vowel count should be {count:d} — `step_vowel_count`</summary>

#### Location

`string_utils_steps.py:61`

#### Parameters

- `count:d`

#### Description

> Asserts that the last vowel count equals ``count``.

#### Source

```python
def step_vowel_count(context, count):
    """Asserts that the last vowel count equals ``count``."""
    assert context.last_result == count, (
        f"Expected {count} vowels, got {context.last_result}"
    )
```

</details>

<details>
<summary>🟡 When: I convert "{text}" to title case — `step_title_case`</summary>

#### Location

`string_utils_steps.py:69`

#### Parameters

- `text`

#### Description

> Converts ``text`` to title case and stores the result.

#### Source

```python
def step_title_case(context, text):
    """Converts ``text`` to title case and stores the result."""
    context.last_input = text
    context.last_result = context.string_utils.to_title_case(text)
```

</details>

<details>
<summary>🟢 Then: the result should be "{expected}" — `step_result_should_be`</summary>

#### Location

`string_utils_steps.py:76`

#### Parameters

- `expected`

#### Description

> Generic assertion: the last transformation result equals ``expected``.
> 
> This step is shared by title-case and slugify scenarios.

#### Source

```python
def step_result_should_be(context, expected):
    """Generic assertion: the last transformation result equals ``expected``.

    This step is shared by title-case and slugify scenarios.
    """
    assert context.last_result == expected, (
        f"Expected '{expected}', got '{context.last_result}'"
    )
```

</details>

<details>
<summary>🟡 When: I slugify "{text}" — `step_slugify`</summary>

#### Location

`string_utils_steps.py:87`

#### Parameters

- `text`

#### Description

> Converts ``text`` to a URL-friendly slug and stores the result.

#### Source

```python
def step_slugify(context, text):
    """Converts ``text`` to a URL-friendly slug and stores the result."""
    context.last_input = text
    context.last_result = context.string_utils.slugify(text)
```

</details>

---

*Generated by Behave Markdown Report on 2026-07-01 15:25:42.*
