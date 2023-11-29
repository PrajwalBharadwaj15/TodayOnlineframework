Feature: Signin Functionality

  Background: Common setup
    Given Launch chrome browser
    When Open home page

Scenario: Perform Signin
 Given    If user is on home page 
 Then     Click on Signin link
 Then     Enter the Email and password details
 Then     Click on Signin button 