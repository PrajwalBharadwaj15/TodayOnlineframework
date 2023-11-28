from behave import then,when
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.minutepage import click_minute_card

@when(u'I click on Minute card and navigate to respective article')
def find_and_clickminute(context):
  click_minute_card(context)


    





