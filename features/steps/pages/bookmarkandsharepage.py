from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


from selenium.webdriver.support import expected_conditions as EC
from main.elementhelper import ElementHelper
from main.javascripthelper import Javascripthelper


class TodayWeb_BookmarkAndSharePage:
    driver = webdriver.Chrome()
    js_helper = Javascripthelper(driver)
    ele_helper = ElementHelper(driver)
    def __init__(self, driver):
        self.driver = driver
        self.init_elements()

    def init_elements(self):
        self.bookmarkIcon_anonymousUser = (By.XPATH, "//a[@class='link bookmark-link-anonymous use-ajax']/*[position()=1]")
        self.shareIcon = (By.XPATH, "//a[@class='link trigger-popup trigger-popup--share']/*[position()=1]")
        self.bookmarkIcon_LoggedInUser = (By.XPATH, "//a[contains(@class,'link bookmark-link')]/*[position()=1]")
        self.bookmarkMessage = (By.XPATH, "//div[contains(@class,'message-popup__content')]//span")
        self.copyLinkButton = (By.XPATH, "//div[@class='copy-link']//button")
        self.copyLinktext = (By.XPATH, "//div[@class='copy-link']//input")
        self.shareNewsPopUp = (By.XPATH, "//div[contains(@class,'popup__dialog--share-link')]")
        self.whatsappLink = (By.XPATH, "//div[contains(@class,'popup__content--share-link')]//span[contains(.,'WhatsApp')]/ancestor::a")
        self.facebookLink = (By.XPATH, "//div[contains(@class,'popup__content--share-link')]//span[contains(.,'Facebook')]/ancestor::a")
        self.twitterLink = (By.XPATH, "//div[contains(@class,'popup__content--share-link')]//span[contains(.,'Twitter')]/ancestor::a")
        self.emailLink = (By.XPATH, "//div[contains(@class,'popup__content--share-link')]//span[contains(.,'Email')]/ancestor::a")
        self.linkedINLink = (By.XPATH, "//div[contains(@class,'popup__content--share-link')]//span[contains(.,'LinkedIn')]/ancestor::a")
        self.closePopUpButton = (By.XPATH, "//a[@class='popup__close']")
        self.shareHomePage = (By.XPATH, "//a[contains(@class,'share')]")

    def click_on_bookmark_icon_anonymous_user(self):
        self.js_helper.fn_jsclick(self.bookmarkIcon_anonymousUser)

    def click_on_bookmark_icon_logged_in_user(self):
        self.js_helper.fn_jsclick(self.bookmarkIcon_LoggedInUser)

    def click_on_unbookmark_option(self):
        import time
        time.sleep(4)
        self.js_helper.fn_jsclick(self.bookmarkIcon_LoggedInUser)

    def validate_bookmark_message(self):
        import time
        time.sleep(4)
        msg = self.ele_helper.get_text(self.bookmarkMessage)
        print(msg)
        return msg

    def click_on_share_icon(self):
        self.js_helper.fn_jsclick(self.shareIcon)

    def validate_copy_link_button(self):
        import time
        time.sleep(5)
        copy_options = False
        bln1 = self.ele_helper.is_element_displayed_by(self.copyLinkButton)
        bln2 = self.ele_helper.is_element_displayed_by(self.copyLinktext)

        if bln1 and bln2:
            copy_options = True
        return copy_options

    def validate_share_via_social_platform_icons(self):
        import time
        time.sleep(5)
        share_links = False
        bln1 = self.ele_helper.is_element_displayed_by(self.whatsappLink)
        bln2 = self.ele_helper.is_element_displayed_by(self.facebookLink)
        bln3 = self.ele_helper.is_element_displayed_by(self.twitterLink)
        bln4 = self.ele_helper.is_element_displayed_by(self.emailLink)
        bln5 = self.ele_helper.is_element_displayed_by(self.linkedINLink)

        if bln1 and bln2 and bln3 and bln4 and bln5:
            share_links = True
        return share_links

    def validate_close_pop_up_button(self):
        self.ele_helper.is_element_displayed_by(self.closePopUpButton)
        self.js_helper.fn_jsclick(self.closePopUpButton)