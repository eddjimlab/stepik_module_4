import pytest

from .pages.product_page import PageObject

base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"


@pytest.mark.parametrize('link', [f'{base_link}0', f'{base_link}1', f'{base_link}2', f'{base_link}3', f'{base_link}4',
                                  f'{base_link}5', f'{base_link}6',
                                  pytest.param(f'{base_link}7', marks=pytest.mark.xfail(reason="bad link")),
                                  f'{base_link}8', f'{base_link}9'])
def test_guest_can_add_product_to_basket(browser, link):
    link0 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.add_product_to_cart()
    product_page.product_added_and_basket_equal()  # test added and cart product name
    product_page.price_added_and_basket_equal()  # test price in cart and added is equal
