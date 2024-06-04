from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage
from pages.information_page import InformationPage


class CartPage(BasePage):
    PRODUCT_QUANTITY = (AppiumBy.XPATH, "//*[@content-desc='test-Amount']/android.widget.TextView")
    PRODUCT_TITLE = (AppiumBy.XPATH, "//*[@content-desc='test-Description']/android.widget.TextView[1]")
    PRODUCT_PRICE = (AppiumBy.XPATH, "//*[@content-desc='test-Price']/android.widget.TextView")
    CHECKOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT")

    def get_cart_product_info(self):
        return {
            "title": self.wait_for_element(self.PRODUCT_TITLE).text,
            "quantity": self.wait_for_element(self.PRODUCT_QUANTITY).text,
            "price": self.wait_for_element(self.PRODUCT_PRICE).text
        }

    def click_checkout_button(self) -> InformationPage:
        self.click_on(self.CHECKOUT_BUTTON)
        return InformationPage(self.driver)
