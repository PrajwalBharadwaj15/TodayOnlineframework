from behave import * 
from pages.signinpage import find_signin_link,enter_email_and_password,click_signin_btn

@when('Click on Signin link')
def sign_in_click(context):
  find_signin_link(context)

@then('Enter the Email and password details')
def enter_credentials(context):
  enter_email_and_password(context)

@then('Click on Signin button')
def submit_details(context):
  click_signin_btn(context)