from .pages.main_page import MainPage
from .pages.login_page import LoginPage



def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    link2 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    page = MainPage(browser, link) # init Page Object, with init BasePage(browser, url)
    page.open() # as browser.get(url) open page
    page.go_to_login_page() # find css selector and click, go to login page
    page.should_be_login_link() # check login link

    login_page = LoginPage(browser, link)
    login_page.should_be_login_page()


# pytest -v --tb=line --language=en test_main_page.py