from behave import * 
from pages.bookmarkandsharepage import TodayWeb_BookmarkAndSharePage


@given('If user is anonymous login and bookmark')
def check_anonyuserlogin_bookmark(self):
    anony_bookandshare = TodayWeb_BookmarkAndSharePage()
    anony_bookandshare.click_on_bookmark_icon_anonymous_user(self)

@given('If user is logged in then bookmark')
def check_loggedinuserlogin_bookmark(self):
    loggedin_bookandshare = TodayWeb_BookmarkAndSharePage()
    loggedin_bookandshare.click_on_bookmark_icon_logged_in_user(self)

@then('Verify bookmark removal if user is logged in and bookmarked')
def check_bookmarkremoval(self):
    remove_bookmark = TodayWeb_BookmarkAndSharePage()
    remove_bookmark.click_on_unbookmark_option(self)

@given('Verify share button click')
def check_sharefun(self):
    check_sharebtn = TodayWeb_BookmarkAndSharePage()

@then('On clicking share user can share link to all social media')
