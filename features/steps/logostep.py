from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


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

@then('Verify logo presence')
def verify_logo_presence(context):
    try:
        # Use a CSS selector to locate the logo element on the home page.
        logo_link = context.driver.find_element(By.XPATH,'//a[@class="logo-link"]')
# can also add this with above xpath//img[@src="/themes/custom/mc_todayonline_theme/images/logo.svg"]
        # Check if the logo is displayed
        assert logo_link.is_displayed()
    except Exception as e:
        raise AssertionError('Logo not found or not visible: {}'.format(e))

    
@then(u'Exit chrome browser')
def exit_browser(context):
    # Close the Chrome browser.
    context.driver.quit()








