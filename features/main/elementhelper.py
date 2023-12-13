from selenium.common.exceptions import NoSuchElementException


class elementHandler:

    def fn_is_element_present(context, elem):
        try:
            return elem is not None and elem.is_displayed()
        except NoSuchElementException:
            return False
        
    def fn_click(context, elem):
        bln_status = True
        try:
            if context.fn_is_element_present(elem):
                elem.click()
            else:
                raise NoSuchElementException("Element Not Present")
        except Exception as e:
            bln_status = False
        return bln_status

    
    
    def fn_scrolltoviewbtn(context):
        scroll = context.execute_script("window.scrollTo(0,4500);")
        return scroll
    
    #to take an element in a list of elements,grab the text and interact with case insensitivity 
    def verify_text_inlist(ele_list, str_value):
        try:
            for element in ele_list:
                str_txt = element.text
                if str_value.lower() in str_txt.lower():
                 return True 
        except Exception as e:
         pass
        return False       
                
        