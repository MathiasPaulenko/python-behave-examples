# Feature: behave-comments
# Demonstrates: metadata annotations (# @key value attached to feature and
#   scenario), typed doc strings ("""json parsed automatically), and
#   comment-declared lifecycle hooks (@before-scenario / @after-scenario
#   that run real steps).
# Wired via setup_lifecycle_hooks_from_path + run_* hooks + inject_metadata.
# @owner qa-team
# @jira BEHAVE-100
@comments @unit
Feature: behave-comments annotations and hooks
  As a test author
  I want metadata and lifecycle logic declared in feature comments
  So that documentation and wiring live next to the scenarios

  # The @id annotation attaches to this scenario; feature-level
  # @owner/@jira attach to the feature. inject_metadata() exposes them
  # as context.metadata.
  # @id SC-101
  @smoke
  Scenario: Metadata annotations are injected into context
    Then the feature metadata should contain owner "qa-team"
    And the scenario metadata should contain id "SC-101"

  # """json marks the doc string content type; @with_parsed_text injects
  # a TextBlock whose .parsed attribute is real Python data.
  Scenario: Typed doc string parsing
    Given a JSON user document:
      """json
      {"name": "Ada", "age": 36, "roles": ["admin", "editor"]}
      """
    Then the parsed document name should be "Ada"
    And the parsed document should have 2 roles

  # Lifecycle hooks declared in comments run real step definitions.
  # @before-scenario: Given the lifecycle flag is set
  # @after-scenario: Then the lifecycle flag is cleared
  Scenario: Comment-declared lifecycle hooks
    Then the lifecycle flag should be set by the before hook
