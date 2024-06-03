from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class CartPage(BasePage):
    PRODUCT_QUANTITY = (AppiumBy.XPATH, "//*[@content-desc='test-Amount']/android.widget.TextView")
    PRODUCT_TITLE = (AppiumBy.XPATH, "//*[@content-desc='test-Description']/android.widget.TextView[1]")
    PRODUCT_PRICE = (AppiumBy.XPATH, "//*[@content-desc='test-Price']/android.widget.TextView")

    def get_cart_product_info(self):
        return {
            "title": self.wait_for_element(self.PRODUCT_TITLE).text,
            "quantity": self.wait_for_element(self.PRODUCT_QUANTITY).text,
            "price": self.wait_for_element(self.PRODUCT_PRICE).text
        }
