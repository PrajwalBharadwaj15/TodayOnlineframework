from behave import then
from selenium.webdriver.common.by import By
from pages.logopage import verify_logo_presence,exit_browser

@then('Verify logo presence')
def verify_if_logopresent(context):
  verify_logo_presence(context)

@then('Exit chrome browser')
def close_browser(context):
 exit_browser(context)   