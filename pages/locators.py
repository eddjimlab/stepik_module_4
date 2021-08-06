from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "button[name='login_submit']")
    REGISTER_FORM = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_ADDED = (By.CSS_SELECTOR, "#content_inner h1")
    PRODUCT_CART = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    PRICE_ADDED = (By.CSS_SELECTOR, "#content_inner .price_color")
    PRICE_CART = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")
