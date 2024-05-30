import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture()
def driver():
    capabilities = {
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:deviceName": "ZY32FJMCTJ",
        "appium:platformVersion": "12.0",
        "appium:appPackage": "com.swaglabsmobileapp",
        "appium:appActivity": ".MainActivity"
    }
    appium_server_url = 'http://localhost:4723'

    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    yield driver
    driver.quit()
