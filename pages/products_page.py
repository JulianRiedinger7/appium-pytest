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

    def add_first_product(self):
        PRODUCT_ADD_LOCATOR = (
            AppiumBy.XPATH,
            "(//android.view.ViewGroup[@content-desc='test-ADD TO CART'])[1]"
        )

        self.click_on(PRODUCT_ADD_LOCATOR)

    def get_first_product_info(self):
        product_title_locator = (
            AppiumBy.XPATH,
            "(//*[@content-desc='test-Item title'])[1]"
        )
        product_price_locator = (
            AppiumBy.XPATH,
            "(//*[@content-desc='test-Price'])[1]"
        )

        return {
            "title": self.wait_for_element(product_title_locator).text,
            "price": self.wait_for_element(product_price_locator).text
        }
