from selenium.webdriver.common.by import By
from main.elementhelper import elementhelper  # Import the class
  # Import the SigninHandler class
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def find_signin_link(context):
    element_handler = elementhelper()  # Create an instance of ElementHandler
    signin_link = context.driver.find_element(By.XPATH, '//a[contains(@class, "sign-in-link")]')
    element_handler.fn_click(context, signin_link)  # Access fn_click through the instance


def enter_email_and_password(context):
      # Create an instance of SigninHandler
    email_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'//input[@id="edit-email"]'))
    )
    email_input.send_keys("meprajwal123@gmail.com")

    password_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'//input[@id="edit-password"]'))
    )
    password_input.send_keys("meconnect@123")

def click_signin_btn(context):
    element_handler = elementhelper()  # Create an instance of ElementHandler
    signin_btn = context.driver.find_element(By.XPATH, "//button[contains(.,'Sign in')]")
    element_handler.fn_click(context, signin_btn)  # Access fn_click through the instance