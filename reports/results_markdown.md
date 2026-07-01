# ⚪ Behave Markdown Report

**Status:** Untested  
**Generated:** 2026-07-01 16:18:26  
**Duration:** 1.34s

---

## Table of Contents

- [Executive Summary](#executive-summary)
- [Statistics](#statistics)
- [Feature Summary](#feature-summary)
- [Tags](#tags)
- [Slowest Scenarios](#slowest-scenarios)
- [Scenario Details](#scenario-details)
- [Environment](#environment)

---

## Executive Summary

| Status | Count | Icon |
| ------ | ----- | ---- |
| Passed | 44    | ✅    |

## Statistics

| Metric         | Value   |
| -------------- | ------- |
| Features       | 6       |
| Scenarios      | 44      |
| Steps          | 194     |
| Pass rate      | 100.00% |
| Total duration | 1.34s   |
| Attachments    | 0       |
| Log lines      | 0       |

## Feature Summary

| Feature                                                 | Status     | Scenarios | Duration |
| ------------------------------------------------------- | ---------- | --------- | -------- |
| [Async step support](#feature-async-step-support)       | ✅ Passed   | 6         | 299ms    |
| [Calculator](#feature-calculator)                       | ✅ Passed   | 11        | 15ms     |
| [External CSV examples](#feature-external-csv-examples) | ⚪ Untested | 0         | 0ms      |
| [Shopping cart](#feature-shopping-cart)                 | ✅ Passed   | 6         | 7ms      |
| [String utilities](#feature-string-utilities)           | ✅ Passed   | 10        | 8ms      |
| [Users REST API](#feature-users-rest-api)               | ✅ Passed   | 11        | 355ms    |

## Tags

| Tag           | Count | Passed | Failed | Duration | Pass rate |
| ------------- | ----- | ------ | ------ | -------- | --------- |
| `unit`        | 27    | 27     | 0      | 31ms     | 100.00%   |
| `smoke`       | 13    | 13     | 0      | 148ms    | 100.00%   |
| `calculator`  | 11    | 11     | 0      | 15ms     | 100.00%   |
| `integration` | 11    | 11     | 0      | 355ms    | 100.00%   |
| `api`         | 11    | 11     | 0      | 355ms    | 100.00%   |
| `string`      | 10    | 10     | 0      | 8ms      | 100.00%   |
| `shopping`    | 6     | 6      | 0      | 7ms      | 100.00%   |
| `negative`    | 6     | 6      | 0      | 103ms    | 100.00%   |
| `async`       | 6     | 6      | 0      | 299ms    | 100.00%   |
| `math`        | 5     | 5      | 0      | 7ms      | 100.00%   |
| `docstring`   | 1     | 1      | 0      | 0ms      | 100.00%   |

## Slowest Scenarios

| Rank | Scenario                                                                                                        | Feature            | Duration |
| ---- | --------------------------------------------------------------------------------------------------------------- | ------------------ | -------- |
| 1    | [Async fetch with multiple keys -- @1.3 ](#scenario-async-step-support-async-fetch-with-multiple-keys-----1-3-) | Async step support | 58ms     |
| 2    | [Async fetch with multiple keys -- @1.2 ](#scenario-async-step-support-async-fetch-with-multiple-keys-----1-2-) | Async step support | 57ms     |
| 3    | [Async fetch with multiple keys -- @1.4 ](#scenario-async-step-support-async-fetch-with-multiple-keys-----1-4-) | Async step support | 57ms     |
| 4    | [Health check](#scenario-users-rest-api-health-check)                                                           | Users REST API     | 57ms     |
| 5    | [Async fetch with multiple keys -- @1.1 ](#scenario-async-step-support-async-fetch-with-multiple-keys-----1-1-) | Async step support | 57ms     |
| 6    | [Fetching a value asynchronously](#scenario-async-step-support-fetching-a-value-asynchronously)                 | Async step support | 54ms     |
| 7    | [Role-based user creation -- @1.3 ](#scenario-users-rest-api-role-based-user-creation-----1-3-)                 | Users REST API     | 50ms     |
| 8    | [Get a user by id](#scenario-users-rest-api-get-a-user-by-id)                                                   | Users REST API     | 43ms     |
| 9    | [Duplicate email is rejected](#scenario-users-rest-api-duplicate-email-is-rejected)                             | Users REST API     | 42ms     |
| 10   | [List users with pagination](#scenario-users-rest-api-list-users-with-pagination)                               | Users REST API     | 36ms     |

## Scenario Details

<details>
<summary>Feature: External CSV examples</summary>

> As a tester
> I want to load Examples table data from a CSV file
> So that I can keep large data sets outside the feature file

Tags: `csv` `integration`

#### [External CSV examples](#feature-external-csv-examples)

</details>

<details>
<summary>Feature: Users REST API</summary>

> As an API consumer
> I want to manage users via a REST API
> So that I can demonstrate behave testing against a real HTTP server

Tags: `api` `integration`

#### [Users REST API](#feature-users-rest-api)

<details>
<summary>✅ Scenario: Health check</summary>

**Status:** ✅ Passed

**Duration:** 57ms

**Location:** `features/api/users_api.feature:20`

**Tags:** `smoke`

##### Background

⚪ **Given** the API server is running — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:15`</sub>

⚪ **And** the users database is empty — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:16`</sub>

##### Steps

✅ **Given** the API server is running — `28ms` (Passed)

<sub>Location: `features/api/users_api.feature:15`</sub>

✅ **And** the users database is empty — `14ms` (Passed)

<sub>Location: `features/api/users_api.feature:16`</sub>

✅ **When** I send a GET request to "/api/health" — `14ms` (Passed)

<sub>Location: `features/api/users_api.feature:21`</sub>

✅ **Then** the response status should be 200 — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:22`</sub>

✅ **And** the response field "status" should be "ok" — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:23`</sub>

</details>

<details>
<summary>✅ Scenario: Create a user with a data table</summary>

**Status:** ✅ Passed

**Duration:** 10ms

**Location:** `features/api/users_api.feature:28`

**Tags:** `smoke`

##### Background

⚪ **Given** the API server is running — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:15`</sub>

⚪ **And** the users database is empty — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:16`</sub>

##### Steps

✅ **Given** the API server is running — `2ms` (Passed)

<sub>Location: `features/api/users_api.feature:15`</sub>

✅ **And** the users database is empty — `2ms` (Passed)

<sub>Location: `features/api/users_api.feature:16`</sub>

✅ **When** I send a POST request to "/api/users" with: — `4ms` (Passed)

<sub>Location: `features/api/users_api.feature:29`</sub>
| field | value            |
| ----- | ---------------- |
| name  | Test User        |
| email | test@example.com |
| role  | admin            |

✅ **Then** the response status should be 201 — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:34`</sub>

✅ **And** the response should contain "id" — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:35`</sub>

✅ **And** the response field "name" should be "Test User" — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:36`</sub>

✅ **And** the response field "email" should be "test@example.com" — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:37`</sub>

</details>

<details>
<summary>✅ Scenario: Create a user without required fields</summary>

**Status:** ✅ Passed

**Duration:** 27ms

**Location:** `features/api/users_api.feature:41`

**Tags:** `negative`

##### Background

⚪ **Given** the API server is running — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:15`</sub>

⚪ **And** the users database is empty — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:16`</sub>

##### Steps

✅ **Given** the API server is running — `3ms` (Passed)

<sub>Location: `features/api/users_api.feature:15`</sub>

✅ **And** the users database is empty — `20ms` (Passed)

<sub>Location: `features/api/users_api.feature:16`</sub>

✅ **When** I send a POST request to "/api/users" with: — `4ms` (Passed)

<sub>Location: `features/api/users_api.feature:42`</sub>
| field | value |
| ----- | ----- |
| name  |       |
| email |       |

✅ **Then** the response status should be 400 — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:46`</sub>

✅ **And** the response field "error" should be "name and email are required" — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:47`</sub>

</details>

<details>
<summary>✅ Scenario: Duplicate email is rejected</summary>

**Status:** ✅ Passed

**Duration:** 42ms

**Location:** `features/api/users_api.feature:51`

**Tags:** `negative`

##### Background

⚪ **Given** the API server is running — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:15`</sub>

⚪ **And** the users database is empty — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:16`</sub>

##### Steps

✅ **Given** the API server is running — `21ms` (Passed)

<sub>Location: `features/api/users_api.feature:15`</sub>

✅ **And** the users database is empty — `14ms` (Passed)

<sub>Location: `features/api/users_api.feature:16`</sub>

✅ **Given** a user exists with email "dup@example.com" — `2ms` (Passed)

<sub>Location: `features/api/users_api.feature:52`</sub>

✅ **When** I send a POST request to "/api/users" with: — `3ms` (Passed)

<sub>Location: `features/api/users_api.feature:53`</sub>
| field | value           |
| ----- | --------------- |
| name  | Another User    |
| email | dup@example.com |

✅ **Then** the response status should be 409 — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:57`</sub>

✅ **And** the response field "error" should be "email already exists" — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:58`</sub>

</details>

<details>
<summary>✅ Scenario: List users with pagination</summary>

**Status:** ✅ Passed

**Duration:** 36ms

**Location:** `features/api/users_api.feature:62`

##### Background

⚪ **Given** the API server is running — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:15`</sub>

⚪ **And** the users database is empty — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:16`</sub>

##### Steps

✅ **Given** the API server is running — `2ms` (Passed)

<sub>Location: `features/api/users_api.feature:15`</sub>

✅ **And** the users database is empty — `19ms` (Passed)

<sub>Location: `features/api/users_api.feature:16`</sub>

✅ **Given** the following users exist: — `9ms` (Passed)

<sub>Location: `features/api/users_api.feature:63`</sub>
| name   | email          | role   |
| ------ | -------------- | ------ |
| User 1 | u1@example.com | viewer |
| User 2 | u2@example.com | viewer |
| User 3 | u3@example.com | viewer |

✅ **When** I send a GET request to "/api/users?page=1&limit=2" — `4ms` (Passed)

<sub>Location: `features/api/users_api.feature:68`</sub>

✅ **Then** the response status should be 200 — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:69`</sub>

✅ **And** the response should contain at most 2 items — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:70`</sub>

✅ **And** the response field "total" should be 3 — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:71`</sub>

</details>

<details>
<summary>✅ Scenario: Get a user by id</summary>

**Status:** ✅ Passed

**Duration:** 43ms

**Location:** `features/api/users_api.feature:74`

##### Background

⚪ **Given** the API server is running — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:15`</sub>

⚪ **And** the users database is empty — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:16`</sub>

##### Steps

✅ **Given** the API server is running — `23ms` (Passed)

<sub>Location: `features/api/users_api.feature:15`</sub>

✅ **And** the users database is empty — `12ms` (Passed)

<sub>Location: `features/api/users_api.feature:16`</sub>

✅ **Given** a user exists with email "getme@example.com" — `3ms` (Passed)

<sub>Location: `features/api/users_api.feature:75`</sub>

✅ **When** I send a GET request to the created user endpoint — `2ms` (Passed)

<sub>Location: `features/api/users_api.feature:76`</sub>

✅ **Then** the response status should be 200 — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:77`</sub>

✅ **And** the response field "email" should be "getme@example.com" — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:78`</sub>

</details>

<details>
<summary>✅ Scenario: Delete a user returns 204</summary>

**Status:** ✅ Passed

**Duration:** 36ms

**Location:** `features/api/users_api.feature:81`

##### Background

⚪ **Given** the API server is running — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:15`</sub>

⚪ **And** the users database is empty — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:16`</sub>

##### Steps

✅ **Given** the API server is running — `2ms` (Passed)

<sub>Location: `features/api/users_api.feature:15`</sub>

✅ **And** the users database is empty — `5ms` (Passed)

<sub>Location: `features/api/users_api.feature:16`</sub>

✅ **Given** a user exists with email "deleteme@example.com" — `3ms` (Passed)

<sub>Location: `features/api/users_api.feature:82`</sub>

✅ **When** I send a DELETE request to the created user endpoint — `24ms` (Passed)

<sub>Location: `features/api/users_api.feature:83`</sub>

✅ **Then** the response status should be 204 — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:84`</sub>

</details>

<details>
<summary>✅ Scenario: Get a non-existent user returns 404</summary>

**Status:** ✅ Passed

**Duration:** 29ms

**Location:** `features/api/users_api.feature:88`

**Tags:** `negative`

##### Background

⚪ **Given** the API server is running — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:15`</sub>

⚪ **And** the users database is empty — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:16`</sub>

##### Steps

✅ **Given** the API server is running — `2ms` (Passed)

<sub>Location: `features/api/users_api.feature:15`</sub>

✅ **And** the users database is empty — `23ms` (Passed)

<sub>Location: `features/api/users_api.feature:16`</sub>

✅ **When** I send a GET request to "/api/users/9999" — `2ms` (Passed)

<sub>Location: `features/api/users_api.feature:89`</sub>

✅ **Then** the response status should be 404 — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:90`</sub>

✅ **And** the response field "error" should be "not found" — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:91`</sub>

</details>

<details>
<summary>✅ Scenario: Role-based user creation -- @1.1 </summary>

**Status:** ✅ Passed

**Duration:** 9ms

**Location:** `features/api/users_api.feature:107`

##### Background

⚪ **Given** the API server is running — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:15`</sub>

⚪ **And** the users database is empty — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:16`</sub>

##### Steps

✅ **Given** the API server is running — `2ms` (Passed)

<sub>Location: `features/api/users_api.feature:15`</sub>

✅ **And** the users database is empty — `2ms` (Passed)

<sub>Location: `features/api/users_api.feature:16`</sub>

✅ **When** I send a POST request to "/api/users" with: — `3ms` (Passed)

<sub>Location: `features/api/users_api.feature:97`</sub>
| field | value              |
| ----- | ------------------ |
| name  | Admin 1            |
| email | admin1@example.com |
| role  | admin              |

✅ **Then** the response status should be 201 — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:102`</sub>

✅ **And** the response field "role" should be "admin" — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:103`</sub>

</details>

<details>
<summary>✅ Scenario: Role-based user creation -- @1.2 </summary>

**Status:** ✅ Passed

**Duration:** 12ms

**Location:** `features/api/users_api.feature:108`

##### Background

⚪ **Given** the API server is running — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:15`</sub>

⚪ **And** the users database is empty — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:16`</sub>

##### Steps

✅ **Given** the API server is running — `2ms` (Passed)

<sub>Location: `features/api/users_api.feature:15`</sub>

✅ **And** the users database is empty — `6ms` (Passed)

<sub>Location: `features/api/users_api.feature:16`</sub>

✅ **When** I send a POST request to "/api/users" with: — `2ms` (Passed)

<sub>Location: `features/api/users_api.feature:97`</sub>
| field | value             |
| ----- | ----------------- |
| name  | Editor 1          |
| email | edit1@example.com |
| role  | editor            |

✅ **Then** the response status should be 201 — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:102`</sub>

✅ **And** the response field "role" should be "editor" — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:103`</sub>

</details>

<details>
<summary>✅ Scenario: Role-based user creation -- @1.3 </summary>

**Status:** ✅ Passed

**Duration:** 50ms

**Location:** `features/api/users_api.feature:109`

##### Background

⚪ **Given** the API server is running — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:15`</sub>

⚪ **And** the users database is empty — `0ms` (Untested)

<sub>Location: `features/api/users_api.feature:16`</sub>

##### Steps

✅ **Given** the API server is running — `3ms` (Passed)

<sub>Location: `features/api/users_api.feature:15`</sub>

✅ **And** the users database is empty — `20ms` (Passed)

<sub>Location: `features/api/users_api.feature:16`</sub>

✅ **When** I send a POST request to "/api/users" with: — `26ms` (Passed)

<sub>Location: `features/api/users_api.feature:97`</sub>
| field | value             |
| ----- | ----------------- |
| name  | Viewer 1          |
| email | view1@example.com |
| role  | viewer            |

✅ **Then** the response status should be 201 — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:102`</sub>

✅ **And** the response field "role" should be "viewer" — `0ms` (Passed)

<sub>Location: `features/api/users_api.feature:103`</sub>

</details>

</details>

<details>
<summary>Feature: Async step support</summary>

> As a developer
> I want to use async step definitions
> So that I can test asynchronous code with behave 1.3.x

Tags: `async`

#### [Async step support](#feature-async-step-support)

<details>
<summary>✅ Scenario: Fetching a value asynchronously</summary>

**Status:** ✅ Passed

**Duration:** 54ms

**Location:** `features/async/async_steps.feature:13`

**Tags:** `smoke`

##### Steps

✅ **When** I asynchronously fetch the value for "hello" — `53ms` (Passed)

<sub>Location: `features/async/async_steps.feature:14`</sub>

✅ **Then** the async result should be "world" — `0ms` (Passed)

<sub>Location: `features/async/async_steps.feature:15`</sub>

</details>

<details>
<summary>✅ Scenario: Async fetch with multiple keys -- @1.1 </summary>

**Status:** ✅ Passed

**Duration:** 57ms

**Location:** `features/async/async_steps.feature:27`

##### Steps

✅ **When** I asynchronously fetch the value for "hello" — `57ms` (Passed)

<sub>Location: `features/async/async_steps.feature:22`</sub>

✅ **Then** the async result should be "world" — `0ms` (Passed)

<sub>Location: `features/async/async_steps.feature:23`</sub>

</details>

<details>
<summary>✅ Scenario: Async fetch with multiple keys -- @1.2 </summary>

**Status:** ✅ Passed

**Duration:** 57ms

**Location:** `features/async/async_steps.feature:28`

##### Steps

✅ **When** I asynchronously fetch the value for "behave" — `57ms` (Passed)

<sub>Location: `features/async/async_steps.feature:22`</sub>

✅ **Then** the async result should be "rocks" — `0ms` (Passed)

<sub>Location: `features/async/async_steps.feature:23`</sub>

</details>

<details>
<summary>✅ Scenario: Async fetch with multiple keys -- @1.3 </summary>

**Status:** ✅ Passed

**Duration:** 58ms

**Location:** `features/async/async_steps.feature:29`

##### Steps

✅ **When** I asynchronously fetch the value for "python" — `57ms` (Passed)

<sub>Location: `features/async/async_steps.feature:22`</sub>

✅ **Then** the async result should be "3.12" — `0ms` (Passed)

<sub>Location: `features/async/async_steps.feature:23`</sub>

</details>

<details>
<summary>✅ Scenario: Async fetch with multiple keys -- @1.4 </summary>

**Status:** ✅ Passed

**Duration:** 57ms

**Location:** `features/async/async_steps.feature:30`

##### Steps

✅ **When** I asynchronously fetch the value for "unknown" — `57ms` (Passed)

<sub>Location: `features/async/async_steps.feature:22`</sub>

✅ **Then** the async result should be "<unknown>" — `0ms` (Passed)

<sub>Location: `features/async/async_steps.feature:23`</sub>

</details>

<details>
<summary>✅ Scenario: Doubling a number asynchronously</summary>

**Status:** ✅ Passed

**Duration:** 13ms

**Location:** `features/async/async_steps.feature:35`

**Tags:** `smoke`

##### Steps

✅ **When** I asynchronously double the number 21 — `13ms` (Passed)

<sub>Location: `features/async/async_steps.feature:36`</sub>

✅ **Then** the async result should be 42 — `0ms` (Passed)

<sub>Location: `features/async/async_steps.feature:37`</sub>

</details>

</details>

<details>
<summary>Feature: Calculator</summary>

> As a user
> I want to perform arithmetic operations
> So that I can verify behave's Background and Scenario Outline support

Tags: `calculator` `unit`

#### [Calculator](#feature-calculator)

<details>
<summary>✅ Scenario: Adding two numbers</summary>

**Status:** ✅ Passed

**Duration:** 1ms

**Location:** `features/calculator/calculator.feature:18`

**Tags:** `smoke`

##### Background

⚪ **Given** I have a calculator — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

⚪ **And** the calculator is reset — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

##### Steps

✅ **Given** I have a calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

✅ **And** the calculator is reset — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

✅ **When** I add 5 to the calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:19`</sub>

✅ **And** I add 3 to the calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:20`</sub>

✅ **Then** the result should be 8 — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:21`</sub>

✅ **And** the last operation should be "add" — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:22`</sub>

</details>

<details>
<summary>✅ Scenario: Division by zero raises an error</summary>

**Status:** ✅ Passed

**Duration:** 1ms

**Location:** `features/calculator/calculator.feature:27`

**Tags:** `negative`

##### Background

⚪ **Given** I have a calculator — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

⚪ **And** the calculator is reset — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

##### Steps

✅ **Given** I have a calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

✅ **And** the calculator is reset — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

✅ **When** I add 10 to the calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:28`</sub>

✅ **And** I divide the calculator by 0 — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:29`</sub>

✅ **Then** a ZeroDivisionError should be raised — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:30`</sub>

</details>

<details>
<summary>✅ Scenario: Arithmetic operations with two operands -- @1.1 Basic arithmetic</summary>

**Status:** ✅ Passed

**Duration:** 1ms

**Location:** `features/calculator/calculator.feature:45`

**Tags:** `smoke`

##### Background

⚪ **Given** I have a calculator — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

⚪ **And** the calculator is reset — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

##### Steps

✅ **Given** I have a calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

✅ **And** the calculator is reset — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

✅ **Given** the calculator accumulator is 0 — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:38`</sub>

✅ **When** I add 5 to the calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:39`</sub>

✅ **Then** the result should be 5 — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:40`</sub>

✅ **And** the last operation should be "add" — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:41`</sub>

</details>

<details>
<summary>✅ Scenario: Arithmetic operations with two operands -- @1.2 Basic arithmetic</summary>

**Status:** ✅ Passed

**Duration:** 1ms

**Location:** `features/calculator/calculator.feature:46`

**Tags:** `smoke`

##### Background

⚪ **Given** I have a calculator — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

⚪ **And** the calculator is reset — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

##### Steps

✅ **Given** I have a calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

✅ **And** the calculator is reset — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

✅ **Given** the calculator accumulator is 10 — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:38`</sub>

✅ **When** I subtract 4 to the calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:39`</sub>

✅ **Then** the result should be 6 — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:40`</sub>

✅ **And** the last operation should be "subtract" — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:41`</sub>

</details>

<details>
<summary>✅ Scenario: Arithmetic operations with two operands -- @1.3 Basic arithmetic</summary>

**Status:** ✅ Passed

**Duration:** 1ms

**Location:** `features/calculator/calculator.feature:47`

**Tags:** `smoke`

##### Background

⚪ **Given** I have a calculator — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

⚪ **And** the calculator is reset — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

##### Steps

✅ **Given** I have a calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

✅ **And** the calculator is reset — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

✅ **Given** the calculator accumulator is 3 — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:38`</sub>

✅ **When** I multiply 4 to the calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:39`</sub>

✅ **Then** the result should be 12 — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:40`</sub>

✅ **And** the last operation should be "multiply" — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:41`</sub>

</details>

<details>
<summary>✅ Scenario: Arithmetic operations with two operands -- @1.4 Basic arithmetic</summary>

**Status:** ✅ Passed

**Duration:** 1ms

**Location:** `features/calculator/calculator.feature:48`

**Tags:** `smoke`

##### Background

⚪ **Given** I have a calculator — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

⚪ **And** the calculator is reset — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

##### Steps

✅ **Given** I have a calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

✅ **And** the calculator is reset — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

✅ **Given** the calculator accumulator is 20 — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:38`</sub>

✅ **When** I divide 4 to the calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:39`</sub>

✅ **Then** the result should be 5 — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:40`</sub>

✅ **And** the last operation should be "divide" — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:41`</sub>

</details>

<details>
<summary>✅ Scenario: Arithmetic operations with two operands -- @2.1 Edge cases</summary>

**Status:** ✅ Passed

**Duration:** 1ms

**Location:** `features/calculator/calculator.feature:52`

**Tags:** `smoke`

##### Background

⚪ **Given** I have a calculator — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

⚪ **And** the calculator is reset — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

##### Steps

✅ **Given** I have a calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

✅ **And** the calculator is reset — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

✅ **Given** the calculator accumulator is 0 — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:38`</sub>

✅ **When** I add 0 to the calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:39`</sub>

✅ **Then** the result should be 0 — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:40`</sub>

✅ **And** the last operation should be "add" — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:41`</sub>

</details>

<details>
<summary>✅ Scenario: Arithmetic operations with two operands -- @2.2 Edge cases</summary>

**Status:** ✅ Passed

**Duration:** 1ms

**Location:** `features/calculator/calculator.feature:53`

**Tags:** `smoke`

##### Background

⚪ **Given** I have a calculator — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

⚪ **And** the calculator is reset — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

##### Steps

✅ **Given** I have a calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

✅ **And** the calculator is reset — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

✅ **Given** the calculator accumulator is 100 — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:38`</sub>

✅ **When** I divide 100 to the calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:39`</sub>

✅ **Then** the result should be 1 — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:40`</sub>

✅ **And** the last operation should be "divide" — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:41`</sub>

</details>

<details>
<summary>✅ Scenario: Arithmetic operations with two operands -- @2.3 Edge cases</summary>

**Status:** ✅ Passed

**Duration:** 1ms

**Location:** `features/calculator/calculator.feature:54`

**Tags:** `smoke`

##### Background

⚪ **Given** I have a calculator — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

⚪ **And** the calculator is reset — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

##### Steps

✅ **Given** I have a calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

✅ **And** the calculator is reset — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

✅ **Given** the calculator accumulator is -5 — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:38`</sub>

✅ **When** I multiply -2 to the calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:39`</sub>

✅ **Then** the result should be 10 — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:40`</sub>

✅ **And** the last operation should be "multiply" — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:41`</sub>

</details>

<details>
<summary>✅ Scenario: Square root of a positive number</summary>

**Status:** ✅ Passed

**Duration:** 1ms

**Location:** `features/calculator/calculator.feature:58`

**Tags:** `math`

##### Background

⚪ **Given** I have a calculator — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

⚪ **And** the calculator is reset — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

##### Steps

✅ **Given** I have a calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

✅ **And** the calculator is reset — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

✅ **When** I add 16 to the calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:59`</sub>

✅ **And** I take the square root — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:60`</sub>

✅ **Then** the result should be 4 — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:61`</sub>

</details>

<details>
<summary>✅ Scenario: Square root of a negative number raises an error</summary>

**Status:** ✅ Passed

**Duration:** 1ms

**Location:** `features/calculator/calculator.feature:66`

**Tags:** `math` `negative`

##### Background

⚪ **Given** I have a calculator — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

⚪ **And** the calculator is reset — `0ms` (Untested)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

##### Steps

✅ **Given** I have a calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:13`</sub>

✅ **And** the calculator is reset — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:14`</sub>

✅ **When** I add -9 to the calculator — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:67`</sub>

✅ **And** I take the square root — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:68`</sub>

✅ **Then** a ValueError should be raised — `0ms` (Passed)

<sub>Location: `features/calculator/calculator.feature:69`</sub>

</details>

</details>

<details>
<summary>Feature: Shopping cart</summary>

> As a shopper
> I want to manage a shopping cart
> So that I can demonstrate data tables and DocStrings

Tags: `shopping` `unit`

#### [Shopping cart](#feature-shopping-cart)

<details>
<summary>✅ Scenario: Adding items from a data table</summary>

**Status:** ✅ Passed

**Duration:** 1ms

**Location:** `features/shopping_cart/shopping_cart.feature:17`

**Tags:** `smoke`

##### Background

⚪ **Given** I have an empty shopping cart — `0ms` (Untested)

<sub>Location: `features/shopping_cart/shopping_cart.feature:12`</sub>

##### Steps

✅ **Given** I have an empty shopping cart — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:12`</sub>

✅ **When** I add the following items to the cart: — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:18`</sub>
| name   | price | quantity |
| ------ | ----- | -------- |
| Apple  | 0.50  | 3        |
| Banana | 0.30  | 2        |
| Milk   | 1.20  | 1        |

✅ **Then** the cart should contain 6 items — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:23`</sub>

✅ **And** the subtotal should be 3.30 — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:24`</sub>

</details>

<details>
<summary>✅ Scenario: Discount and tax calculation -- @1.1 </summary>

**Status:** ✅ Passed

**Duration:** 1ms

**Location:** `features/shopping_cart/shopping_cart.feature:42`

**Tags:** `math`

##### Background

⚪ **Given** I have an empty shopping cart — `0ms` (Untested)

<sub>Location: `features/shopping_cart/shopping_cart.feature:12`</sub>

##### Steps

✅ **Given** I have an empty shopping cart — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:12`</sub>

✅ **Given** the cart has a discount of 0% and a tax of 0% — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:31`</sub>

✅ **When** I add the following items to the cart: — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:32`</sub>
| name | price | quantity |
| ---- | ----- | -------- |
| Book | 20.00 | 2        |

✅ **Then** the subtotal should be 40.00 — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:35`</sub>

✅ **And** the discount amount should be 0.00 — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:36`</sub>

✅ **And** the tax amount should be 0.00 — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:37`</sub>

✅ **And** the total should be 40.00 — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:38`</sub>

</details>

<details>
<summary>✅ Scenario: Discount and tax calculation -- @1.2 </summary>

**Status:** ✅ Passed

**Duration:** 1ms

**Location:** `features/shopping_cart/shopping_cart.feature:43`

**Tags:** `math`

##### Background

⚪ **Given** I have an empty shopping cart — `0ms` (Untested)

<sub>Location: `features/shopping_cart/shopping_cart.feature:12`</sub>

##### Steps

✅ **Given** I have an empty shopping cart — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:12`</sub>

✅ **Given** the cart has a discount of 10% and a tax of 10% — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:31`</sub>

✅ **When** I add the following items to the cart: — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:32`</sub>
| name | price | quantity |
| ---- | ----- | -------- |
| Book | 20.00 | 2        |

✅ **Then** the subtotal should be 40.00 — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:35`</sub>

✅ **And** the discount amount should be 4.00 — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:36`</sub>

✅ **And** the tax amount should be 3.60 — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:37`</sub>

✅ **And** the total should be 39.60 — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:38`</sub>

</details>

<details>
<summary>✅ Scenario: Discount and tax calculation -- @1.3 </summary>

**Status:** ✅ Passed

**Duration:** 1ms

**Location:** `features/shopping_cart/shopping_cart.feature:44`

**Tags:** `math`

##### Background

⚪ **Given** I have an empty shopping cart — `0ms` (Untested)

<sub>Location: `features/shopping_cart/shopping_cart.feature:12`</sub>

##### Steps

✅ **Given** I have an empty shopping cart — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:12`</sub>

✅ **Given** the cart has a discount of 25% and a tax of 5% — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:31`</sub>

✅ **When** I add the following items to the cart: — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:32`</sub>
| name | price | quantity |
| ---- | ----- | -------- |
| Book | 20.00 | 2        |

✅ **Then** the subtotal should be 40.00 — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:35`</sub>

✅ **And** the discount amount should be 10.00 — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:36`</sub>

✅ **And** the tax amount should be 1.50 — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:37`</sub>

✅ **And** the total should be 31.50 — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:38`</sub>

</details>

<details>
<summary>✅ Scenario: Removing an item that does not exist</summary>

**Status:** ✅ Passed

**Duration:** 1ms

**Location:** `features/shopping_cart/shopping_cart.feature:48`

**Tags:** `negative`

##### Background

⚪ **Given** I have an empty shopping cart — `0ms` (Untested)

<sub>Location: `features/shopping_cart/shopping_cart.feature:12`</sub>

##### Steps

✅ **Given** I have an empty shopping cart — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:12`</sub>

✅ **When** I add the following items to the cart: — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:49`</sub>
| name | price | quantity |
| ---- | ----- | -------- |
| Pen  | 1.50  | 2        |

✅ **And** I remove "Notebook" from the cart — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:52`</sub>

✅ **Then** the cart should contain 2 items — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:53`</sub>

✅ **And** the subtotal should be 3.00 — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:54`</sub>

</details>

<details>
<summary>✅ Scenario: Receipt preview via DocString</summary>

**Status:** ✅ Passed

**Duration:** 0ms

**Location:** `features/shopping_cart/shopping_cart.feature:59`

**Tags:** `docstring`

##### Background

⚪ **Given** I have an empty shopping cart — `0ms` (Untested)

<sub>Location: `features/shopping_cart/shopping_cart.feature:12`</sub>

##### Steps

✅ **Given** I have an empty shopping cart — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:12`</sub>

✅ **When** I add the following items to the cart: — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:60`</sub>
| name | price | quantity |
| ---- | ----- | -------- |
| Pen  | 1.50  | 2        |
| Book | 12.00 | 1        |

✅ **Then** the receipt should be: — `0ms` (Passed)

<sub>Location: `features/shopping_cart/shopping_cart.feature:64`</sub>
```gherkin
=== RECEIPT ===
Pen   x2 = 3.00
Book  x1 = 12.00
----------------
TOTAL: 15.00
```

</details>

</details>

<details>
<summary>Feature: String utilities</summary>

> As a developer
> I want to manipulate strings
> So that I can demonstrate Gherkin v6 Rule blocks

Tags: `string` `unit`

#### [String utilities](#feature-string-utilities)

<details>
<summary>✅ Scenario: A simple palindrome</summary>

**Status:** ✅ Passed

**Duration:** 1ms

**Location:** `features/string_utils/string_utils.feature:17`

##### Steps

✅ **Given** I have the string utilities — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:14`</sub>

✅ **When** I reverse the string "racecar" — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:18`</sub>

✅ **Then** the reversed string should be "racecar" — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:19`</sub>

✅ **And** the string "racecar" should be a palindrome — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:20`</sub>

</details>

<details>
<summary>✅ Scenario: A palindrome with mixed case and punctuation</summary>

**Status:** ✅ Passed

**Duration:** 0ms

**Location:** `features/string_utils/string_utils.feature:23`

##### Steps

✅ **Given** I have the string utilities — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:14`</sub>

✅ **When** I reverse the string "A man, a plan, a canal: Panama" — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:24`</sub>

✅ **Then** the string "A man, a plan, a canal: Panama" should be a palindrome — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:25`</sub>

</details>

<details>
<summary>✅ Scenario: A non-palindrome</summary>

**Status:** ✅ Passed

**Duration:** 1ms

**Location:** `features/string_utils/string_utils.feature:28`

##### Steps

✅ **Given** I have the string utilities — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:14`</sub>

✅ **When** I reverse the string "behave" — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:29`</sub>

✅ **Then** the reversed string should be "evaheb" — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:30`</sub>

✅ **But** the string "behave" should not be a palindrome — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:31`</sub>

</details>

<details>
<summary>✅ Scenario: Counting vowels in a word</summary>

**Status:** ✅ Passed

**Duration:** 0ms

**Location:** `features/string_utils/string_utils.feature:35`

##### Steps

✅ **When** I count the vowels in "Education" — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:36`</sub>

✅ **Then** the vowel count should be 5 — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:37`</sub>

</details>

<details>
<summary>✅ Scenario: Vowel counting across inputs -- @1.1 </summary>

**Status:** ✅ Passed

**Duration:** 0ms

**Location:** `features/string_utils/string_utils.feature:47`

##### Steps

✅ **When** I count the vowels in "sky" — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:42`</sub>

✅ **Then** the vowel count should be 0 — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:43`</sub>

</details>

<details>
<summary>✅ Scenario: Vowel counting across inputs -- @1.2 </summary>

**Status:** ✅ Passed

**Duration:** 0ms

**Location:** `features/string_utils/string_utils.feature:48`

##### Steps

✅ **When** I count the vowels in "AEIOU" — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:42`</sub>

✅ **Then** the vowel count should be 5 — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:43`</sub>

</details>

<details>
<summary>✅ Scenario: Vowel counting across inputs -- @1.3 </summary>

**Status:** ✅ Passed

**Duration:** 0ms

**Location:** `features/string_utils/string_utils.feature:49`

##### Steps

✅ **When** I count the vowels in "Python" — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:42`</sub>

✅ **Then** the vowel count should be 1 — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:43`</sub>

</details>

<details>
<summary>✅ Scenario: Vowel counting across inputs -- @1.4 </summary>

**Status:** ✅ Passed

**Duration:** 0ms

**Location:** `features/string_utils/string_utils.feature:50`

##### Steps

✅ **When** I count the vowels in "queueing" — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:42`</sub>

✅ **Then** the vowel count should be 5 — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:43`</sub>

</details>

<details>
<summary>✅ Scenario: Title case conversion</summary>

**Status:** ✅ Passed

**Duration:** 0ms

**Location:** `features/string_utils/string_utils.feature:54`

##### Steps

✅ **When** I convert "the quick brown fox" to title case — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:55`</sub>

✅ **Then** the result should be "The Quick Brown Fox" — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:56`</sub>

</details>

<details>
<summary>✅ Scenario: Slugify conversion</summary>

**Status:** ✅ Passed

**Duration:** 0ms

**Location:** `features/string_utils/string_utils.feature:58`

##### Steps

✅ **When** I slugify "Hello World! This is Behave 101" — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:59`</sub>

✅ **Then** the result should be "hello-world-this-is-behave-101" — `0ms` (Passed)

<sub>Location: `features/string_utils/string_utils.feature:60`</sub>

</details>

</details>

---

## Environment

| Variable          | Value                                                     |
| ----------------- | --------------------------------------------------------- |
| Python version    | 3.14.5                                                    |
| Behave version    | 1.3.3                                                     |
| Operating system  | Windows 10 (AMD64)                                        |
| Hostname          | MathiasLaptop                                             |
| Working directory | `D:\Codigo\python-behave-examples`                        |
| Execution command | `D:\Codigo\python-behave-examples\.venv\Scripts\behave`   |
| User              | mathi                                                     |
| CPU count         | 12                                                        |
| Memory (MB)       | unknown                                                   |
| Git branch        | main                                                      |
| Git commit        | 08806bb                                                   |
| Git remote        | git@github.com:MathiasPaulenko/python-behave-examples.git |

### CI / Environment Variables

| Variable    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LANG        | en_US.UTF-8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| PATH        | D:\Codigo\python-behave-examples\.venv\Scripts;C:\Python314\Scripts\;C:\Python314\;C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;C:\Program Files\Common Files\Oracle\Java\javapath;C:\Program Files (x86)\Common Files\Oracle\Java\java8path;C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\Program Files\dotnet\;C:\Program Files\Microsoft SQL Server\130\Tools\Binn\;C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\;D:\Softwares\grpcurl;C:\Program Files\Docker\Docker\resources\bin;C:\Program Files\Git\cmd;C:\Program Files\Maven\apache-maven-3.9.9\bin;C:\Program Files\AutoFirma\AutoFirma;C:\Program Files\nodejs\;C:\ProgramData\chocolatey\bin;C:\Users\mathi\AppData\Local\Programs\Python\Python312\Scripts\;C:\Users\mathi\AppData\Local\Programs\Python\Python312\;C:\Users\mathi\AppData\Local\Programs\Python\Python310\Scripts\;C:\Users\mathi\AppData\Local\Programs\Python\Python310\;C:\Users\mathi\AppData\Local\Programs\Python\Python39\Scripts\;C:\Users\mathi\AppData\Local\Programs\Python\Python39\;C:\Users\mathi\AppData\Local\Programs\Python\Python36-32\Scripts\;C:\Users\mathi\AppData\Local\Programs\Python\Python36-32\;C:\Users\mathi\AppData\Local\Microsoft\WindowsApps;C:\Program Files\JetBrains\PyCharm Community Edition 2022.1\bin;C:\Program Files\JetBrains\IntelliJ IDEA 2020.2.3\bin;C:\Users\mathi\.dotnet\tools;C:\Users\mathi\AppData\Local\Programs\Microsoft VS Code\bin;C:\Program Files\JetBrains\PyCharm 2020.3.3\bin;C:\Program Files\JetBrains\PyCharm 2024.1.2\bin;;C:\Program Files\JetBrains\IntelliJ IDEA 2023.1.2\bin;;C:\Program Files\JetBrains\PyCharm Community Edition 2023.1.2\bin;;C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2023.2.3\bin;;C:\Users\mathi\AppData\Local\Programs\MiKTeX\miktex\bin\x64\;C:\Users\mathi\AppData\Local\Programs\Windsurf\bin;C:\Users\mathi\AppData\Roaming\npm;C:\Users\mathi\AppData\Local\Programs\Devin\bin;c:\Users\mathi\.devin\extensions\ms-python.debugpy-2026.6.0-win32-x64\bundled\scripts\noConfigScripts |
| USERPROFILE | C:\Users\mathi                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

---

*Report generated by Behave Markdown Report on 2026-07-01 16:18:26.*
