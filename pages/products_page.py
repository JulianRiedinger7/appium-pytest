from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class ProductsPage(BasePage):
    PRODUCTS_TITLE = (AppiumBy.XPATH, "//*[@content-desc='test-Cart drop "
                                      "zone']/android.view.ViewGroup/android.widget.TextView")

    def get_products_title_text(self) -> str:
        return self.wait_for_element(self.PRODUCTS_TITLE).text
