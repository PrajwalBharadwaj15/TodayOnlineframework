from pages.BTTbuttonpage import click_first_article,click_on_btt
from behave import *

@when(u'I click on the first article on section page')
def click_visible_article(context):
    click_first_article(context)
    
    
@then(u'I should click on BTT button in article detail page')
def click_bttbtn(context):
    click_on_btt(context)

   