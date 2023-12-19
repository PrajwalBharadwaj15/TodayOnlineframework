Feature: Bookmark and Share functionality

  Background: Common setup
    Given Launch chrome browser
    When Open home page

  Scenario: Bookmark functionality validation for anonymous user
    Then I click on Bookmark link for an anonymous user
    

  
  Scenario: Bookmark functionality validation for LoggedIn user
    Then I click on Bookmark option for Logged In user
    Then I validate if "Removed from your bookmarks." toast message is displayed

  
  Scenario: Validate Share Article Option from landing Page
    
    Given I click on share option from homepage
    Then I validate Copy Link button and link text
    Then I validate share via social platform links
    Then I validate close pop up X button