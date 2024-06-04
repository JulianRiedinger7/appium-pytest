from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage
from pages.confirm_page import ConfirmPage


class OverviewPage(BasePage):
    PRODUCT_TITLE = (AppiumBy.XPATH, "//*[@content-desc='test-Description']/android.widget.TextView[1]")
    PRODUCT_PRICE = (AppiumBy.XPATH, "//*[@content-desc='test-Price']/android.widget.TextView")
    FINISH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-FINISH")

    def get_product_info(self):
        return {
            "title": self.wait_for_element(self.PRODUCT_TITLE).text,
            "price": self.wait_for_element(self.PRODUCT_PRICE).text
        }

    def click_finish_button(self) -> ConfirmPage:
        self.click_on(self.FINISH_BUTTON)
        return ConfirmPage(self.driver)
