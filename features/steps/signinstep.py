from behave import * 
from pages.signinpage import find_signinlink,enteremail_and_password,click_signin_btn

@then('Click on Signin link')
def sign_in_click(context):
  find_signinlink(context)

@then('Enter the Email and password details')
def enter_credentials(context):
  enteremail_and_password(context)

@then('Click on Signin button ')
def submit_details(context):
  click_signin_btn(context)