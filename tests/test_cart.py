from pages.header_page import HeaderPage
from pages.products_page import ProductsPage


def test_correct_cart_product(add_product):
    products_page: ProductsPage = add_product
    header_page = HeaderPage(products_page.driver)

    first_product_info = products_page.get_first_product_info()

    cart_page = header_page.click_cart_icon()

    cart_product_info = cart_page.get_cart_product_info()

    assert first_product_info.get("title") == cart_product_info.get("title"), "Product titles do not match"
    assert first_product_info.get("price") == cart_product_info.get("price"), "Product prices do not match"
    assert cart_product_info.get("quantity") == "1", "Quantity do not match"
