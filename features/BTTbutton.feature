Feature: BTT button functionality

  Background: Common setup
    Given Launch chrome browser
    When Open home page

  Scenario: Find the first article on section page
   When I click on the first article on section page
   Then I should click on BTT button in article detail page