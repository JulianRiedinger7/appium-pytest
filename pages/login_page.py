from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage
from pages.products_page import ProductsPage


class LoginPage(BasePage):
    USERNAME_INPUT = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
    PASSWORD_INPUT = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")

    def enter_username(self, username: str):
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login_button(self) -> ProductsPage:
        self.click_on(self.LOGIN_BUTTON)
        return ProductsPage(self.driver)
