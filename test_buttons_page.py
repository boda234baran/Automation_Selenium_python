from .pages.main_page import MainPage
from .pages.buttons_page import Buttons
from .credentials import link


def test_click_all_buttons_in_buttons(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_buttons()
    buttons_page = Buttons(browser, browser.current_url)
    buttons_page.click_buttons()

