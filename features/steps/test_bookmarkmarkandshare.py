from behave import *
from pages.bookmarkandsharepage import TodayWeb_BookmarkAndSharePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#bookmark for anonymous user
@Given("I click on Bookmark link for an anonymous user")
def check_anonyuserlogin_bookmark(context):
 anony_bookandshare = TodayWeb_BookmarkAndSharePage(context.driver)
 anony_bookandshare.click_on_bookmark_icon_anonymous_user()

@Then("I click on Bookmark option for Logged In user")
def check_anonyuserlogin_bookmark(context):
    anony_bookandshare = TodayWeb_BookmarkAndSharePage(context.driver)
    anony_bookandshare.click_on_bookmark_icon_logged_in_user()
    toast_message_locator = (By.XPATH, "//div[contains(@class,'message-popup__content')]//span")
    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(toast_message_locator))

@Then("I validate if Added to your bookmarks. toast message is displayed")
def verify_bookmark_toastmsg(context):
  anony_bookandshare = TodayWeb_BookmarkAndSharePage(context.driver)
  anony_bookandshare.validate_bookmark_message()

@Then("I Click on unBookmark option")
def remove_bookmark(context):
  unbookmark = TodayWeb_BookmarkAndSharePage(context.driver)
  unbookmark.click_on_unbookmark_option()

@Then("I validate if Removed from your bookmarks. toast message is displayed")
def verify_bookmark_toastmsg(context):
  anony_bookandshare = TodayWeb_BookmarkAndSharePage(context.driver)
  anony_bookandshare.validate_bookmark_message()

@Then("I click on share option from homepage")
def access_sharebtn(context):
  click_share = TodayWeb_BookmarkAndSharePage(context.driver)
  click_share.click_on_share_icon()
    

@Then("I validate Copy Link button and link text")
def validate_copy_linkandtxt(context):
  check_copy = TodayWeb_BookmarkAndSharePage(context.driver)
  check_copy.validate_copy_link_button()  

@Then("I validate share via social platform links")
def verify_socialshare(context):
  check_socialshare = TodayWeb_BookmarkAndSharePage(context.driver)
  check_socialshare.validate_share_via_social_platform_icons()   

@Then("I validate close pop up X button")
def verify_closepop(context):
  check_closebtn = TodayWeb_BookmarkAndSharePage(context.driver)
  check_closebtn.validate_close_pop_up_button()  
                                                       
 











  

