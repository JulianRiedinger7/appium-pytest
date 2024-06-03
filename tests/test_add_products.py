from pages.header_page import HeaderPage
from pages.products_page import ProductsPage


def test_add_all_products_to_cart(login):
    products_page: ProductsPage = login
    header_page = HeaderPage(products_page.driver)
    amount_of_products = "6"

    assert products_page.get_products_title_text().lower() == "products"

    products_page.click_all_add_to_cart_buttons()

    assert header_page.get_cart_badge_number() == amount_of_products, \
        f"Incorrect number of products added, found {header_page.get_cart_badge_number()}"
