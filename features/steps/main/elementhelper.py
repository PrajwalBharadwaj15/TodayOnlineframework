from selenium.common.exceptions import NoSuchElementException

class elementhelper:
    def fn_click(self, context, elem):
        bln_status = True
        try:
            if self.fn_is_element_present(elem):
                context.elem.click()
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
    
    def fn_scroll_to_view_btn(self, context):
        scroll = context.execute_script("window.scrollTo(0,4500);")
        return scroll
    
    def verify_text_in_list(self, ele_list, str_value):
        try:
            for element in ele_list:
                str_txt = element.text
                if str_value.lower() in str_txt.lower():
                    return True 
        except Exception as e:
            pass
        return False       