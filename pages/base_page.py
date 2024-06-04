from appium.webdriver.webdriver import WebDriver
from selenium.common import TimeoutException, NoSuchElementException
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
        max_scroll_attempts = 3
        scroll_attempts = 0

        while scroll_attempts < max_scroll_attempts:
            try:
                element = self.wait_for_element(locator)
                if element.is_displayed():
                    element.click()
                    return
                else:
                    self.scroll_down()
            except NoSuchElementException:
                self.scroll_down()
            except TimeoutException:
                self.scroll_down()

            scroll_attempts += 1

        raise Exception(f"Could not find element after {max_scroll_attempts} scroll attempts")

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

    def is_element_displayed(self, locator: tuple[str, str]) -> bool:
        return self.wait_for_element(locator).is_displayed()
