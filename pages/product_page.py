from .base_page import BasePage
from .locators import ProductPageLocators
import time


class PageObject(BasePage):
    def add_product_to_cart(self):
        cart_element= self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
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



