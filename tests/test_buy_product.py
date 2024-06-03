import pytest

from pages.header_page import HeaderPage
from pages.login_page import LoginPage


@pytest.fixture()
def login(driver, valid_credentials):
    login_page = LoginPage(driver)
    return login_page.login(valid_credentials.get("username"), valid_credentials.get("password"))


def test_buy_all_products(login):
    products_page = login
    header_page = HeaderPage(products_page.driver)
    amount_of_products = "6"

    assert products_page.get_products_title_text().lower() == "products"

    products_page.click_all_add_to_cart_buttons()

    assert header_page.get_cart_badge_number() == amount_of_products, \
        f"Incorrect number of products added, found {header_page.get_cart_badge_number()}"
