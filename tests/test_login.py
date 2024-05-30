import pytest

from pages.login_page import LoginPage

def test_correct_login(driver, valid_credentials):
    login_page = LoginPage(driver)

    login_page.enter_username(valid_credentials.get("username"))
    login_page.enter_password(valid_credentials.get("password"))
    products_page = login_page.click_login_button()

    assert products_page.get_products_title_text().lower() == "products"

def test_incorrect_login(driver, invalid_credentials):
    login_page = LoginPage(driver)

    for credentials in invalid_credentials:
        login_page.enter_username(credentials.get("username"))
        login_page.enter_password(credentials.get("password"))
        login_page.click_login_button()

        assert login_page.get_error_message_text() == credentials.get("message")
