from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_for_element(self, locator: tuple[str, str], timeout=10):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    def click_on(self, locator: tuple[str, str]):
        self.wait_for_element(locator).click()

    def enter_text(self, locator: tuple[str, str], text: str):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)