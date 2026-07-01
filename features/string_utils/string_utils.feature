# Feature: String utilities
# Demonstrates: Gherkin v6 Rule blocks, Example keyword (alias for Scenario),
#   Background inside a Rule, Scenario Outline within a Rule.
@string @unit
Feature: String utilities
  As a developer
  I want to manipulate strings
  So that I can demonstrate Gherkin v6 Rule blocks

  # Rule 1: Each Rule groups related scenarios.
  # Background inside a Rule only applies to scenarios within that Rule.
  Rule: Palindromes are detected ignoring case and punctuation
    Background:
      Given I have the string utilities

    # "Example" is the Gherkin v6 keyword alias for "Scenario".
    Example: A simple palindrome
      When I reverse the string "racecar"
      Then the reversed string should be "racecar"
      And the string "racecar" should be a palindrome

    # Palindrome detection ignores punctuation, spaces, and case.
    Example: A palindrome with mixed case and punctuation
      When I reverse the string "A man, a plan, a canal: Panama"
      Then the string "A man, a plan, a canal: Panama" should be a palindrome

    # "But" keyword is used to contrast with the previous "Then".
    Example: A non-palindrome
      When I reverse the string "behave"
      Then the reversed string should be "evaheb"
      But the string "behave" should not be a palindrome

  # Rule 2: Vowel counting is case-insensitive (a, e, i, o, u).
  Rule: Vowels are counted case-insensitively
    Example: Counting vowels in a word
      When I count the vowels in "Education"
      Then the vowel count should be 5

    # Scenario Outline inside a Rule — placeholders are replaced
    # by each row in the Examples table.
    Scenario Outline: Vowel counting across inputs
      When I count the vowels in "<text>"
      Then the vowel count should be <count>

      Examples:
        | text     | count |
        | sky      | 0     |
        | AEIOU    | 5     |
        | Python   | 1     |
        | queueing | 5     |

  # Rule 3: Text transformations (title case and slugify).
  Rule: Text is transformed into title-case and slug form
    Example: Title case conversion
      When I convert "the quick brown fox" to title case
      Then the result should be "The Quick Brown Fox"

    Example: Slugify conversion
      When I slugify "Hello World! This is Behave 101"
      Then the result should be "hello-world-this-is-behave-101"
