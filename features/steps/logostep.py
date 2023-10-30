from behave import *
from selenium import webdriver

@given(u'Launch chrome browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Launch chrome browser')


@when(u'Open home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Open home page')


@then(u'Veify logo presence and click')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Veify logo presence and click')


@then(u'Exit chome browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Exit chome browser')