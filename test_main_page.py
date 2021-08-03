from .pages.main_page import MainPage



def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # init Page Object, with init BasePage(browser, url)
    page.open() # as browser.get(url) open page
    page.go_to_login_page() # find css selector and click, go to login page
    page.should_be_login_link() # check login link


# pytest -v --tb=line --language=en test_main_page.py