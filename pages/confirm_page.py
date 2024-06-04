from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage
from pages.products_page import ProductsPage


class ConfirmPage(BasePage):
    CHECKOUT_COMPLETE_CONTAINER = (AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT: COMPLETE!")
    BACK_HOME_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-BACK HOME")

    def is_checkout_container_displayed(self) -> bool:
        return self.is_element_displayed(self.CHECKOUT_COMPLETE_CONTAINER)

    def click_back_home_button(self) -> ProductsPage:
        self.click_on(self.BACK_HOME_BUTTON)
        return ProductsPage(self.driver)
    