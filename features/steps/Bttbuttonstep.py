from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *

@when(u'I click on the first article on section page')
def click_first_article(context):
    try:
        
       wait = WebDriverWait(context.driver, 5)
       first_article = wait.until(EC.element_to_be_clickable((By.XPATH, "//body/div[1]/div[1]/div[2]/main[1]/div[1]/section[1]/article[1]/div[1]/div[3]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/picture[1]/img[1]")))
       first_article.click()
    except Exception as e:
        raise AssertionError('First article not found or not visible: {}'.format(e))
    
@then(u'I should click on BTT button in article detail page')
def click_on_btt(context):
    context.driver.execute_script("window.scrollTo(0,5000);")
    try:
        
       wait = WebDriverWait(context.driver, 6)
       btt_button = wait.until(EC.element_to_be_clickable((By.ID, "back-to-top")))
       btt_button.click()
    except Exception as e:
        raise AssertionError('BTT button not found or not visible: {}'.format(e))