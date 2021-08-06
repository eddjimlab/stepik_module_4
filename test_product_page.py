from .pages.product_page import PageObject


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.add_product_to_cart()
    product_page.product_added_and_basket_equal() # test added and cart product name
    product_page.price_added_and_basket_equal() # test price in cart and added is equal


