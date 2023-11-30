from selenium.webdriver.common.by import By
class SigninHandler:
    def send_email_key(self, context):
        email_input = context.driver.find_element(By.XPATH, '//input[@id="edit-email"]')
        email_input.send_keys("meprajwal123@gmail.com")

    def send_password_key(self, context):
        password_input = context.driver.find_element(By.XPATH, '//input[@id="edit-password"]')
        password_input.send_keys("meconnect@123")