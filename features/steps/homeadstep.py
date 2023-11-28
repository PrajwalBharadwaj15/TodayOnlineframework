from pages.homeadpage import click_imu_ads,click_lb_ads,click_outbrain_ads,switch_to_home
from behave import *

driver = None
@when('I click on LB ads in Home page')
def click_leaderboard_ads(context):
  click_lb_ads(context)
 
 
def switch_back_to(context):
  switch_to_home(context)
 


@when('I click on IMU ads in Home page')
def click_allIMU_ads(context):
 click_imu_ads(context)
 
 
def switch_back_to(context):
  switch_to_home(context)
 
@when('I click on outbrain ads in Home page')
def click_allOutbrain_ads(context):
   click_outbrain_ads(context)
 