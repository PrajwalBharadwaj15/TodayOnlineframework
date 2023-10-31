from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = None

@given('Launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()

@when('Open home page')
def open_home_page(context):
    # Navigate to the URL of your home page.
    context.driver.get('https://www.todayonline.com/')  # Replace with the actual URL.

@then('Verify logo presence and click')
def verify_logo_and_click(context):
    # Use a CSS selector to locate the logo element on the home page.
    logo = context.driver.find_element(By.CSS_SELECTOR, 'logo__image')  # Replace with the actual CSS selector for the logo.

    # Check if the logo element is displayed.
    if logo.is_displayed():
        # If the logo is displayed, click on it.
        logo.click()
    else:
        raise AssertionError('Logo not found or not visible')

@then('Exit chrome browser')
def exit_browser(context):
    # Close the Chrome browser.
    context.driver.quit()








