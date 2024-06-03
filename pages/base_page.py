from appium.webdriver.webdriver import WebDriver
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_for_element(self, locator: tuple[str, str], timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_elements(self, locator: tuple[str, str], timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def click_on(self, locator: tuple[str, str]):
        self.wait_for_element(locator).click()

    def click_all(self, locator: tuple[str, str]):
        # Clicks all elements including those not visible without scrolling first
        elements_clicked = set()
        elements_before_scroll = set()

        while True:
            try:
                elements = self.wait_for_elements(locator)
                elements_before_scroll.update(elements)

                for element in elements:
                    if element.is_displayed() and element not in elements_clicked:
                        element.click()
                        elements_clicked.add(element)

                # Scroll down to find more elements
                self.scroll_down()

                # Check if new elements are found after scrolling
                elements_after_scroll = self.wait_for_elements(locator)
                if elements_before_scroll == set(elements_after_scroll):
                    break

            except TimeoutException:
                break

    def scroll_down(self):
        # Scroll down by swiping up
        window_size = self.driver.get_window_size()
        start_x = window_size["width"] / 2
        start_y = window_size["height"] * 0.8
        end_y = window_size["height"] * 0.2
        self.driver.swipe(start_x, start_y, start_x, end_y, 800)

    def enter_text(self, locator: tuple[str, str], text: str):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)
