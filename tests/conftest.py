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

@pytest.fixture
def valid_credentials():
    return {
        "username": "standard_user",
        "password": "secret_sauce"
    }

@pytest.fixture
def invalid_credentials():
    return [
        {
            "username": "",
            "password": "",
            "message": "Username is required"
        },
        {
            "username": "test",
            "password": "",
            "message": "Password is required"
        },
        {
            "username": "test",
            "password": "test",
            "message": "Username and password do not match any user in this service."
        }
    ]