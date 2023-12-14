
from elementhelper import ElementHelper 
from selenium.common.exceptions import NoSuchElementException

class Javascripthelper():
    def __init__(self):
        self.element_helper = ElementHelper()

    def fnjsclick(self, elem):
        bln_status = True 
        try:
            if self.element_helper.is_element_present(elem):
                elem.click()
        except NoSuchElementException:
            bln_status = False
        return bln_status
  
    def fn_jsclick(self, loc):
        bln_status = True
        try:
            if self.element_helper.fn_is_element_present(loc):
                elem = self.driver.find_element(*loc)
                javascript = "arguments[0].click();"      
                self.driver.execute_script(javascript, elem)
            else:
                raise NoSuchElementException("Element Not Present")
        except Exception as e:
            bln_status = False
        return bln_status

    def fnjsscrolltoview_by(self, driver, loc):
        try:
            js_executor = driver
            elem = driver.find_element(*loc)
            javascript = "arguments[0].scrollIntoView(true);"
            js_executor.execute_script(javascript, elem)
        except Exception as e:
            pass

    def fnjsscrolltoview(self, driver, elem):
        try:
            js_executor = driver
            javascript = "arguments[0].scrollIntoView(true);"
            js_executor.execute_script(javascript, elem)
        except Exception as e:
            pass

   



