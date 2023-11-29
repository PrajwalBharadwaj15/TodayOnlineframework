from selenium import webdriver

global driver
driver = None

class signinHandler:
 def send_email_key(context):
   driver.sendkeys("meprajwal123@gmail.com")

 def send_password_key(context):
   driver.sendkeys("meconnect@123")