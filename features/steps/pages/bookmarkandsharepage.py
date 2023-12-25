from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from main.elementhelper import ElementHelper
from main.javascripthelper import Javascripthelper

class TodayWeb_BookmarkAndSharePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.js_helper = Javascripthelper(driver)
        self.ele_helper = ElementHelper(driver)
        self.init_elements()

    def init_elements(self):
        self.bookmarkIcon_anonymousUser = (By.XPATH, "//a[@class='link bookmark-link-anonymous use-ajax']/*[position()=1]")
        self.shareIcon = (By.XPATH, "//a[@class='link trigger-popup trigger-popup--share']/*[position()=1]")
        self.bookmarkIcon_LoggedInUser = (By.XPATH, "//a[contains(@class,'link bookmark-link')]/*[position()=1]")
        self.bookmarkMessage = (By.XPATH, "//div[@class='message-popup__content']//span")
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
        try:
            bookmark_icon = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.bookmarkIcon_anonymousUser)
            )
            bookmark_icon.click()
        except TimeoutException as e:
            print(f"Timeout waiting for bookmark icon for anonymous user: {e}")
        except NoSuchElementException as e:
            print(f"Error clicking bookmark icon for anonymous user: {e}")

    def click_on_bookmark_icon_logged_in_user(self):
        try:
            self.js_helper.fn_jsclick(self.bookmarkIcon_LoggedInUser)
        except NoSuchElementException as e:
            print(f"Error clicking bookmark icon for logged-in user: {e}")

    def click_on_unbookmark_option(self):
        try:
            self.js_helper.fn_jsclick(self.bookmarkIcon_LoggedInUser)
        except NoSuchElementException as e:
            print(f"Error clicking bookmark icon for unbookmark: {e}")

    def validate_bookmark_message(self):
     expected_message = "Added to your bookmarks."
     try:
        bookmark_message = self.wait.until(EC.presence_of_element_located(self.bookmarkMessage))
        message_text = self.ele_helper.get_text(bookmark_message)
        if message_text == expected_message:
            print(f"Bookmark message validated: '{message_text}' as expected")
        else:
            print(f"Bookmark message mismatch: expected '{expected_message}', actual '{message_text}'")
     except NoSuchElementException as e:
        print(f"Error finding bookmark message: {e}")


    def click_on_share_icon(self):
     self.js_helper.fn_jsclick(self.shareIcon)

    def validate_copy_link_button(self):
     try:
        self.wait.until(EC.presence_of_element_located(self.copyLinkButton))
        self.wait.until(EC.presence_of_element_located(self.copyLinktext))
        return "Copy link button and text available"
     except TimeoutException:
        return "Timed out waiting for copy link elements"
     except NoSuchElementException:
        return "Copy link button or text missing"

    def validate_share_via_social_platform_icons(self):
     try:
        self.wait.until(EC.presence_of_element_located(self.whatsappLink))
        self.wait.until(EC.presence_of_element_located(self.facebookLink))
        self.wait.until(EC.presence_of_element_located(self.twitterLink))
        self.wait.until(EC.presence_of_element_located(self.emailLink))
        self.wait.until(EC.presence_of_element_located(self.linkedINLink))
        return "All social platform icons are present"
     except TimeoutException:
        return "Timed out waiting for social platform icons"
     except NoSuchElementException:
        return "Missing one or more social platform icons"

    def validate_close_pop_up_button(self):
     if self.ele_helper.is_element_displayed_by(self.closePopUpButton):
        self.js_helper.fn_jsclick(self.closePopUpButton)
        return "Close button clicked successfully"
     else:
        return "Close button is not displayed"