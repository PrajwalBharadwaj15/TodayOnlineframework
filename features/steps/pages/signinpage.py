from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main.elementhelper import fn_click
from main.signincredshelper import send_email_key,send_password_key

def find_signinlink(context):
   signin_link = context.driver.find_element(By.XPATH, '//a[@class[contains[.,"sign-in-link"]]]')
   fn_click(context,signin_link)

def enteremail_and_password(context):
  email = context.driver.find_element(By.XPATH, '//input[@id="edit-email"]')
  email.send_email_key(context)
  password = context.driver.find_element(By.XPATH, '//input[@id="edit-password"]')
  password.send_password_key(context)

def click_signin_btn(context):
   signin_btn = context.driver.find_element(By.XPATH, "//button[contains(.,'Sign in')]")
   fn_click(context,signin_btn)




