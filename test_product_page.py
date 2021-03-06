import time

import pytest

from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, ProductPageLocators.LINK_MAIN)
    product_page.open()
    product_page.add_product_to_cart()
    product_page.product_added_and_basket_equal()  # test added and cart product name
    product_page.price_added_and_basket_equal()  # test price in cart and added is equal


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.LINK_MAIN)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductPageLocators.LINK_MAIN)
    page.open()
    page.should_not_be_success_message_before_adding_product()


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


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, ProductPageLocators.LINK_MAIN)
    product_page.open()
    product_page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, ProductPageLocators.LINK_MAIN)
    product_page.open()
    product_page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_empty()
    basket_page.basket_message_is_empty()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, ProductPageLocators.LINK_MAIN)
        page.open()
        page.go_to_register_page()

        login_page = LoginPage(browser, browser.current_url)
        login_page.open()
        email = str(time.time()) + "@mail.ru"
        password = "Mister" + str(time.time())
        login_page.register_new_user(email, password)

        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, ProductPageLocators.LINK_MAIN)
        page.open()
        page.should_not_be_success_message_before_adding_product()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, ProductPageLocators.LINK_MAIN)
        product_page.open()
        product_page.add_product_to_cart()
        product_page.product_added_and_basket_equal()  # test added and cart product name
        product_page.price_added_and_basket_equal()  # test price in cart and added is equal
