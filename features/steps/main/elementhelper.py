from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By

class ElementHelper:
    def __init__(self):
        self.bln_status = False
        self.driver = None

    def is_selected(self, elem):
        try:
            self.bln_status = elem.is_selected()
        except Exception as e:
            self.bln_status = False
        return self.bln_status

    def fn_is_selected(self, loc_strategy, loc_value):
        loc = (loc_strategy, loc_value)
        try:
            element = self.driver.find_element(*loc)
            self.bln_status = element.is_selected()
        except NoSuchElementException:
            self.bln_status = False
        return self.bln_status

    def is_enabled(self, elem):
        try:
            self.bln_status = elem.is_enabled()
        except Exception as e:
            self.bln_status = False
        return self.bln_status

    def fn_is_enabled(self, loc_strategy, loc_value):
        loc = (loc_strategy, loc_value)
        try:
            element = self.driver.find_element(*loc)
            self.bln_status = element.is_enabled()
        except NoSuchElementException:
            self.bln_status = False
        return self.bln_status

    def fn_is_element_present(self, loc_strategy, loc_value):
        loc = (loc_strategy, loc_value)
        try:
            elements = self.driver.find_elements(*loc)
            self.bln_status = len(elements) > 0
        except NoSuchElementException:
            self.bln_status = False
        return self.bln_status