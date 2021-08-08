from .base_page import BasePage
from .locators import ProductPageLocators
import pytest


class PageObject(BasePage):
    def add_product_to_cart(self):
        cart_element = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        cart_element.click()
        self.solve_quiz_and_get_code()

    def product_added_and_basket_equal(self):
        added_product = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED).text
        cart_product = self.browser.find_element(*ProductPageLocators.PRODUCT_CART).text
        assert cart_product == added_product, "Product in cart is not equal to added"

    def price_added_and_basket_equal(self):
        price_added = self.browser.find_element(*ProductPageLocators.PRICE_ADDED).text
        cart_price = self.browser.find_element(*ProductPageLocators.PRICE_CART).text
        assert price_added == cart_price, "Price in cart is not equal to added"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message after adding " \
                                                                                  "product is presented, " \
                                                                                  "but not should be "

    def should_not_be_success_message_before_adding_product(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message before adding " \
                                                                                  "product is presented, " \
                                                                                  "but not should be "

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message should disappear, but is " \
                                                                          "present "
