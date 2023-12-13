from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def find_signin_link(context):
    signin_link = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(@class,"sign-in-link")]'))
    )
    signin_link.click()

def enter_email_and_password(context):
    email_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="edit-email"]'))
    )
    email_input.send_keys("meprajwal123@gmail.com")

    password_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="edit-password"]'))
    )
    password_input.send_keys("meconnect@123")

def click_signin_btn(context):
    # Locate the Sign In button
    signin_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Sign in')]"))
    )
    # Scroll to the Sign In button
    context.driver.execute_script("arguments[0].scrollIntoView();", signin_btn)
    
    # Wait for a moment before clicking
    WebDriverWait(context.driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Sign in')]")))
    
    # Click the Sign In button using JavaScript
    context.driver.execute_script("arguments[0].click();", signin_btn)