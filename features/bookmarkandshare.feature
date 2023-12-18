Feature: Bookmark and Share functionality

  Background: Common setup
    Given Launch chrome browser
    When Open home page

Scenario Outline:  Bookmark for anonymous user
Then I click on Bookmark link for an anonymous user
And  I validate if MeConnect SignIN Page is displayed


Scenario Outline:  Bookmark for Signed-in user
When I click on Sign In option from primary Links section
    Then I validate if MeConnect SignIN Page is displayed
    And I enter valid username and Password
    Then I click on SignIn button
    Then I validate if user is logged in to application successfully
    Then I click on Bookmark option for Logged In user
    And I validate if "Added to your bookmarks." toast message is displayed
    Then I Click on unBookmark option
    And I validate if "Removed from your bookmarks." toast message is displayed

Scenario Outline: Share functionality 
And I click on share option from homepage
    Then I validate Copy Link button and link text
    And I validate share via social platform links
    And I validate close pop up X button
