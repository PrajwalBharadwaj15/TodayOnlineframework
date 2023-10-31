Feature: Today logo

  Background: Common setup
    Given Launch chrome browser
    When Open home page

  Scenario: Identify today logo in home page
    Then Verify logo presence
    And Exit chrome browser

