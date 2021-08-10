from .pages.basket_page import BasketPage
from .pages.locators import BasePageLocators
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        link2 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
        page = MainPage(browser, link)  # init Page Object, with init BasePage(browser, url)
        page.open()  # as browser.get(url) open page
        page.should_be_login_link()  # check login link
        page.go_to_login_page()  # find css selector and click, go to login page

        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.is_element_present(*BasePageLocators.CART_LINK)
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_empty()
    basket_page.basket_message_is_empty()

# pytest -v --tb=line --language=en test_main_page.py
