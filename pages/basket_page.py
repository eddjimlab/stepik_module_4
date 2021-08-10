from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.CART_TOTAL_PRICE), "Basket should be empty, but it`s not"

    def basket_message_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.CART_EMPTY_MESSAGE), "No message 'Ваша корзина пуста'"
