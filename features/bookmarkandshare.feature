@TodayOnlineBookmarkAndShareFunctionalityScenarios
Feature: Bookmark and Share functionality scenarios

Background: Common setup
    Given Launch chrome browser
    When Open home page

  @TodayWeb_13 @Sanity_Web @Web_Sanity_Preprod
  Scenario: Bookmark functionality validation for anonymous user
    Given I click on Bookmark link for an anonymous user
    

  @TodayWeb_14 @Sanity_Web @Web_Sanity_Preprod
         
  
   Scenario: Perform Signin
    When     Click on Signin link
    Then     Enter the Email and password details
    Then     Click on Signin button 

    Scenario: Bookmark functionality validation for LoggedIn user
    Then I click on Bookmark option for Logged In user
    Then I validate if Added to your bookmarks. toast message is displayed
    Then I Click on unBookmark option
    Then I validate if Removed from your bookmarks. toast message is displayed

  @TodayWeb_15 @Sanity_Web @Web_Sanity_Preprod
  Scenario: Validate Share Article Option from landing Page
    Then I click on share option from homepage
    Then I validate Copy Link button and link text
    Then I validate share via social platform links
    Then I validate close pop up X button