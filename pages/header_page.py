from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage
from pages.cart_page import CartPage


class HeaderPage(BasePage):
    CART_ICON = (AppiumBy.ACCESSIBILITY_ID, "test-Cart")
    CART_BADGE = (AppiumBy.XPATH, "//*[@content-desc = 'test-Cart']//android.widget.TextView")

    def get_cart_badge_number(self):
        return self.wait_for_element(self.CART_BADGE).text

    def click_cart_icon(self) -> CartPage:
        self.click_on(self.CART_ICON)
        return CartPage(self.driver)
