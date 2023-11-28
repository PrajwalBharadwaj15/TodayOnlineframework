def verify_logo_presence(context):
    try:
        # Use a CSS selector to locate the logo element on the home page.
        logo_link = context.driver.find_element(By.XPATH, '//a[@class="logo-link"]')
        # can also add this with the above XPath //img[@src="/themes/custom/mc_todayonline_theme/images/logo.svg"]
        # Check if the logo is displayed
        assert logo_link.is_displayed()
    except Exception as e:
        raise AssertionError('Logo not found or not visible: {}'.format(e))
    
def exit_browser(context):
    # Close the Chrome browser.
    context.driver.quit()