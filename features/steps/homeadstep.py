from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *


driver = None
@when('I click on LB ads in Home page')
def click_lb_ads(context):
 try:
        lb_ad = WebDriverWait(context.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='ad-desktop-lb1-1']")))
        lb_ad.click()     
 except Exception as e:
  raise AssertionError('LB ad not found or not visible: {}'.format(e))
 
 p = driver.current_window_handle
 chwd = driver.window_handles
 for w in chwd:
#switch focus to child window
    if(w!=p):
      driver.switch_to.window(w)

@when('I click on IMU ads in Home page')
def click_imu_ads(context):
 try:
     imu_ad = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-ad-entity='imu01_desktop']")))
     imu_ad.click()   
 except Exception as e:
     raise AssertionError('IMU ad not found or not visible: {}'.format(e))