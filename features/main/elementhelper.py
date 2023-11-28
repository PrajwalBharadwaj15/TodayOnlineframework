from selenium.common.exceptions import NoSuchElementException

class elementHandler:
    def fn_click(self, elem):
        bln_status = True
        try:
            if self.fn_is_element_present(elem):
                elem.click()
            else:
                raise NoSuchElementException("Element Not Present")
        except Exception as e:
            bln_status = False
        return bln_status

    def fn_is_element_present(self, elem):
        try:
            return elem is not None and elem.is_displayed()
        except NoSuchElementException:
            return False