from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@then(u'I click the search button')
def click_on_search(context):
    # Use WebDriverWait to wait for the element to be visible and clickable
    search_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Search')]")) #//span[@class="inline-menu__link-text"][text()="Search"]
    )
    print("before click")
    search_button.click()
    print("After click")