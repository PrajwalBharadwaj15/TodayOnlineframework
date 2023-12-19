from behave import * 
from pages.bookmarkandsharepage import TodayWeb_BookmarkAndSharePage
from pages.signinpage import enter_email_and_password,click_signin_btn

#bookmark for anonymous user
@Then('I click on Bookmark link for an anonymous user')
def check_anonyuserlogin_bookmark(context):
 anony_bookandshare = TodayWeb_BookmarkAndSharePage(context.driver)
 anony_bookandshare.click_on_bookmark_icon_anonymous_user()




#bookmark for logged in user
@then('I click on Bookmark option for Logged In user')
def check_anonyuserlogin_bookmark(context):
    anony_bookandshare = TodayWeb_BookmarkAndSharePage(context.driver)
    anony_bookandshare.click_on_bookmark_icon_anonymous_user()

@then('I validate if "Removed from your bookmarks." toast message is displayed')
def verify_bookmark_toastmsg_removal(context):
  anony_bookandshare = TodayWeb_BookmarkAndSharePage(context.driver)
  anony_bookandshare.validate_bookmark_message()

#validate share functionality
@given('I click on share option from homepage')
def access_sharebtn(context):
  click_share = TodayWeb_BookmarkAndSharePage(context.driver)
  click_share.click_on_share_icon()

@then('I validate Copy Link button and link text')
def validate_copy_linkandtxt(context):
  check_copy = TodayWeb_BookmarkAndSharePage(context.driver)
  check_copy.validate_copy_link_button()

@then('I validate share via social platform links')
def verify_socialshare(context):
  check_socialshare = TodayWeb_BookmarkAndSharePage(context.driver)
  check_socialshare.validate_share_via_social_platform_icons()

@then('I validate close pop up X button')
def verify_closepop(context):
  check_closebtn = TodayWeb_BookmarkAndSharePage(context.driver)
  check_closebtn.validate_close_pop_up_button()
  

