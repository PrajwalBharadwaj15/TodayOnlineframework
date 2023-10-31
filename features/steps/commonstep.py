from behave import given,when
from selenium import webdriver

# Initialize the WebDriver
global driver
driver = None

@given(u'Launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()

@when(u'Open home page')
def open_home_page(context):
    # Navigate to the URL of your home page.
    context.driver.get('https://www.todayonline.com/')  # Replace with the actual URL.