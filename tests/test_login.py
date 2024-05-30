import time

from pages.login_page import LoginPage

valid_credentials = {
    "username": "standard_user",
    "password": "secret_sauce"
}

def test_correct_login(driver):
    login_page = LoginPage(driver)

    login_page.enter_username(valid_credentials.get("username"))
    login_page.enter_password(valid_credentials.get("password"))
    products_page = login_page.click_login_button()

    assert products_page.get_products_title_text().lower() == "products"
