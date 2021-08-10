from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
    CART_LINK = (By.CSS_SELECTOR, 'a[href$="basket/"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "button[name='login_submit']")
    REGISTER_FORM = (By.CSS_SELECTOR, "button[name='registration_submit']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_INPUT_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators():
    LINK_MAIN = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    LINK_TEST = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_ADDED = (By.CSS_SELECTOR, "#content_inner h1")
    PRODUCT_CART = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    PRICE_ADDED = (By.CSS_SELECTOR, "#content_inner .price_color")
    PRICE_CART = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")


class BasketPageLocators():
    CART_TOTAL_PRICE = (By.CSS_SELECTOR, ".checkout-quantity input[name='form-0-quantity']")
    CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
