from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *

driver = None
@when('I click on LB ads in Home page')
def click_lb_ads(context):
 try:
        lb_ad = WebDriverWait(context.driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='ad-desktop-lb1-1']")))
        lb_ad.click()     
 except Exception as e:
  raise AssertionError('LB ad not found or not visible: {}'.format(e))
 
from selenium import webdriver 
def switch_to_home():
 driver = webdriver.Chrome()
 driver.get('https://www.todayonline.com/')
 driver.maximize_window()
 #store list of windows in window_handles 
 windowsopened = driver.window_handles
 #use switch_to in window_handles to fetch specific window
 driver.switch_to.window(windowsopened[0])


@when('I click on IMU ads in Home page')
def click_imu_ads(context):
 try:
     imu_ad = WebDriverWait(context.driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-ad-entity='imu01_desktop']")))
     imu_ad.click()   
 except Exception as e:
     raise AssertionError('IMU ad not found or not visible: {}'.format(e))
 
 switch_to_home()
 
 @when('I click on outbrain ads in Home page')
 def click_outbrain_ads(context):
  context.driver.execute_script("window.scrollTo(0,10500);")
  try:
     outbrain_ad = WebDriverWait(context.driver, 3).until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='ob-unit ob-rec-image-container'])[1]")))#use [i] to intereact with specific position
     outbrain_ad.click()   
  except Exception as e:
     raise AssertionError('outbrain ad not found or not visible: {}'.format(e))