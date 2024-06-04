from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage
from pages.overview_page import OverviewPage


class InformationPage(BasePage):
    FIRST_NAME_INPUT = (AppiumBy.ACCESSIBILITY_ID, "test-First Name")
    LAST_NAME_INPUT = (AppiumBy.ACCESSIBILITY_ID, "test-Last Name")
    POSTAL_CODE_INPUT = (AppiumBy.ACCESSIBILITY_ID, "test-Zip/Postal Code")
    CONTINUE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-CONTINUE")
    ERROR_MESSAGE = (AppiumBy.XPATH, "//*[@content-desc='test-Error message']/android.widget.TextView")

    def enter_first_name(self, first_name: str):
        self.enter_text(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name: str):
        self.enter_text(self.LAST_NAME_INPUT, last_name)

    def enter_postal_code(self, postal_code: str):
        self.enter_text(self.POSTAL_CODE_INPUT, postal_code)

    def get_error_message_text(self):
        return self.wait_for_element(self.ERROR_MESSAGE).text

    def click_continue_button(self) -> OverviewPage:
        self.click_on(self.CONTINUE_BUTTON)
        return OverviewPage(self.driver)
