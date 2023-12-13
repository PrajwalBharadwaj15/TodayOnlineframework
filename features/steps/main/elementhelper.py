from selenium.common.exceptions import NoSuchElementException

<<<<<<< HEAD:features/main/elementhelper.py

class elementHandler:

    def fn_is_element_present(context, elem):
        try:
            return elem is not None and elem.is_displayed()
        except NoSuchElementException:
            return False
        
    def fn_click(context, elem):
=======
class elementhelper:
    def fn_click(self, context, elem):
>>>>>>> 376537453ace8bc9da3a80ab3c8c04e5141819a6:features/steps/main/elementhelper.py
        bln_status = True
        try:
            if self.fn_is_element_present(elem):
                context.elem.click()
            else:
                raise NoSuchElementException("Element Not Present")
        except Exception as e:
            bln_status = False
        return bln_status

<<<<<<< HEAD:features/main/elementhelper.py
    
=======
    def fn_is_element_present(self, elem):
        try:
            return elem is not None and elem.is_displayed()
        except NoSuchElementException:
            return False
>>>>>>> 376537453ace8bc9da3a80ab3c8c04e5141819a6:features/steps/main/elementhelper.py
    
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