import pytest

from pages.login_page import LoginPage

valid_credentials = {
    "username": "standard_user",
    "password": "secret_sauce"
}

invalid_credentials = [
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


def test_correct_login(driver):
    login_page = LoginPage(driver)

    login_page.enter_username(valid_credentials.get("username"))
    login_page.enter_password(valid_credentials.get("password"))
    products_page = login_page.click_login_button()

    assert products_page.get_products_title_text().lower() == "products"

@pytest.mark.parametrize("credentials", invalid_credentials)
def test_incorrect_login(driver, credentials):
    login_page = LoginPage(driver)

    login_page.enter_username(credentials.get("username"))
    login_page.enter_password(credentials.get("password"))
    login_page.click_login_button()

    assert login_page.get_error_message_text() == credentials.get("message")
