import pytest

from pages.header_page import HeaderPage
from pages.products_page import ProductsPage


@pytest.fixture
def checkout_page(add_product):
    products_page: ProductsPage = add_product
    header_page = HeaderPage(products_page.driver)

    first_product_info = products_page.get_first_product_info()
    cart_page = header_page.click_cart_icon()

    information_page = cart_page.click_checkout_button()

    return {
        "product_info": first_product_info,
        "information_page": information_page
    }

def test_incorrect_information(checkout_page, incorrect_checkout_information):
    information_page = checkout_page.get("information_page")

    for info in incorrect_checkout_information:
        information_page.enter_first_name(info.get("first_name"))
        information_page.enter_last_name(info.get("last_name"))
        information_page.enter_postal_code(info.get("postal_code"))
        information_page.click_continue_button()

        assert information_page.get_error_message_text() == info.get("message"), \
            f"Error messages do not match, found {information_page.get_error_message_text()}"


def test_correct_product_buy(checkout_page):
    information_page = checkout_page.get("information_page")
    first_product_info = checkout_page.get("product_info")

    information_page.enter_first_name("julian")
    information_page.enter_last_name("perez")
    information_page.enter_postal_code("123")
    overview_page = information_page.click_continue_button()

    overview_product_info = overview_page.get_product_info()

    assert overview_product_info.get("title") == first_product_info.get("title"), "Titles do not match"
    assert overview_product_info.get("price") == first_product_info.get("price"), "Prices do not match"

    confirm_page = overview_page.click_finish_button()

    assert confirm_page.is_checkout_container_displayed(), "Checkout container is not displayed"

    products_page = confirm_page.click_back_home_button()

    assert products_page.get_products_title_text().lower() == "products"
