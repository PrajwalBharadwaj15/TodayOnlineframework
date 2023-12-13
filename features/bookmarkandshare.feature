Feature: Bookmark and Share functionality

  Background: Common setup
    Given Launch chrome browser
    When Open home page

Given If user is anonymous login and bookmark
Given If user is logged in then bookmark 
Then  Verify bookmark removal if user is logged in and bookmarked 
Given Verify share button click 
Then  On clicking share user can share link to all social media 