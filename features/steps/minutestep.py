from behave import then,when
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when(u'I click on Minute card and navigate to respective article')
def click_minute_card(context):
    context.driver.execute_script("window.scrollTo(0,1800);")
    try:
        
       wait = WebDriverWait(context.driver, 10)
       element = wait.until(EC.element_to_be_clickable((By.ID, "slick-slide10")))
       element.click()
    except Exception as e:
        raise AssertionError('Minute card not found or not visible: {}'.format(e))
    






