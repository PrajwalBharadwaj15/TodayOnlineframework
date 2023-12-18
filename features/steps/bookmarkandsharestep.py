from behave import * 
from pages.bookmarkandsharepage import TodayWeb_BookmarkAndSharePage
from pages.signinpage import enter_email_and_password,click_signin_btn

#bookmark for anonymous user
@Then('I click on Bookmark link for an anonymous user')
def check_anonyuserlogin_bookmark(self):
 anony_bookandshare = TodayWeb_BookmarkAndSharePage()
 anony_bookandshare.click_on_bookmark_icon_anonymous_user(self)


@then('I validate if MeConnect SignIN Page is displayed')
def enter_credentials(context):
  enter_email_and_password(context)

def submit_details(context):
  click_signin_btn(context)

@then('I validate if "Added to your bookmarks." toast message is displayed')
def verify_bookmark_toastmsg(self):
  anony_bookandshare = TodayWeb_BookmarkAndSharePage()
  anony_bookandshare.validate_bookmark_message(self)

#bookmark for logged in user
@then('click on Bookmark option for Logged In user')
def check_loggedinuser_bookmark(self):
  anony_bookandshare = TodayWeb_BookmarkAndSharePage()
  anony_bookandshare.click_on_bookmark_icon_logged_in_user(self)

@then('I validate if "Removed from your bookmarks." toast message is displayed')
def verify_bookmark_toastmsg_removal(self):
  anony_bookandshare = TodayWeb_BookmarkAndSharePage()
  anony_bookandshare.validate_bookmark_message(self)

#validate share functionality
@given('I click on share option from homepage')
def access_sharebtn(self):
  click_share = TodayWeb_BookmarkAndSharePage()
  click_share.click_on_share_icon(self)

@then('I validate Copy Link button and link text')
def validate_copy_linkandtxt(self):
  check_copy = TodayWeb_BookmarkAndSharePage()
  check_copy.validate_copy_link_button(self)

@then('I validate share via social platform links')
def verify_socialshare(self):
  check_socialshare = TodayWeb_BookmarkAndSharePage()
  check_socialshare.validate_share_via_social_platform_icons(self)

@then('I validate close pop up X button')
def verify_closepop(self):
  check_closebtn = TodayWeb_BookmarkAndSharePage()
  check_closebtn.validate_close_pop_up_button(self)
  

