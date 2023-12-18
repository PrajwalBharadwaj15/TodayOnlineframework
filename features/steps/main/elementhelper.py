from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By

class ElementHelper:
    def __init__(self, driver):
        self.driver = driver

    def is_selected(self, elem):
        try:
            return elem.is_selected()
        except Exception as e:
            return False

    def fn_is_selected(self, loc_strategy, loc_value):
        loc = (loc_strategy, loc_value)
        try:
            element = self.driver.find_element(*loc)
            return element.is_selected()
        except NoSuchElementException:
            return False

    def is_enabled(self, elem):
        try:
            return elem.is_enabled()
        except Exception as e:
            return False

    def fn_is_enabled(self, loc_strategy, loc_value):
        loc = (loc_strategy, loc_value)
        try:
            element = self.driver.find_element(*loc)
            return element.is_enabled()
        except NoSuchElementException:
            return False

    def fn_is_element_present(self, loc_strategy, loc_value):
        loc = (loc_strategy, loc_value)
        try:
            elements = self.driver.find_elements(*loc)
            return len(elements) > 0
        except NoSuchElementException:
            return False

    def is_element_present(self, elem):
        try:
            return elem.is_displayed()
        except NoSuchElementException:
            return False

    def is_element_displayed(self, elem):
        try:
            if self.is_element_present(elem):
                return elem.is_displayed()
            else:
                raise NoSuchElementException("Element Not Present")
        except Exception as e:
            return False

    def is_element_displayed_by(self, loc):
        try:
            if self.fn_is_element_present(*loc):
                return self.driver.find_element(*loc).is_displayed()
            else:
                raise NoSuchElementException("Element Not Present")
        except Exception as e:
            return False

    def get_text(self, elem):
        try:
            if self.is_element_present(elem):
                return elem.text
            else:
                raise NoSuchElementException("Element Not Present")
        except Exception as e:
            return ""
     
        