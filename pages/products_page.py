from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class ProductsPage(BasePage):
    PRODUCTS_TITLE = (AppiumBy.XPATH, "//*[@content-desc='test-Cart drop "
                                      "zone']/android.view.ViewGroup/android.widget.TextView")
    ADD_TO_CART_BUTTONS = (AppiumBy.ACCESSIBILITY_ID, "test-ADD TO CART")

    def get_products_title_text(self) -> str:
        return self.wait_for_element(self.PRODUCTS_TITLE).text
    
    def click_all_add_to_cart_buttons(self):
        self.click_all(self.ADD_TO_CART_BUTTONS)
