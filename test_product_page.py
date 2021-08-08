import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


# base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"


# @pytest.mark.parametrize('link', [f'{base_link}0', f'{base_link}1', f'{base_link}2', f'{base_link}3', f'{base_link}4',
#                                   f'{base_link}5', f'{base_link}6',
#                                   pytest.param(f'{base_link}7', marks=pytest.mark.xfail(reason="bad link")),
#                                   f'{base_link}8', f'{base_link}9'])
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, ProductPageLocators.LINK_MAIN)
    product_page.open()
    product_page.add_product_to_cart()
    product_page.product_added_and_basket_equal()  # test added and cart product name
    product_page.price_added_and_basket_equal()  # test price in cart and added is equal


@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.LINK_MAIN)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductPageLocators.LINK_MAIN)
    page.open()
    page.should_not_be_success_message_before_adding_product()


@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.LINK_MAIN)
    page.open()
    page.add_product_to_cart()
    page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, ProductPageLocators.LINK_MAIN)
    product_page.open()
    product_page.go_to_login_page()
