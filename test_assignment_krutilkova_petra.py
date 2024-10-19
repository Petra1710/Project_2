import pytest

def test_banner(page):
    page.goto("https://www.prf.upol.cz/")
    div_banner_class = "navbar-brand"
    div_banner = page.locator(f"div.{div_banner_class}")
    assert div_banner.is_visible() == True

def test_cookie_bar(page):
    page.goto("https://www.prf.upol.cz/")
    cookie_bar_id = "tx_cookies"
    cookie_bar = page.locator(f"div#{cookie_bar_id}")
    assert cookie_bar.is_visible() == True

def test_click_cookies(page):
    page.goto("https://www.prf.upol.cz/")
    button_agree_value = "Povolit vše"
    button_agree = page.locator(f"input[value='{button_agree_value}']")
    button_agree.click()
    assert button_agree.is_visible() == False

def test_text_input(page):
    page.goto("https://www.prf.upol.cz/")
    button_class_search = "nav__search-btn"
    text_input_id = "nav__search-input"

    button_search = page.locator(f"a[class='{button_class_search}']")
    button_search.click()    # This click opens a text input
    text_input = page.locator(f"input[id='{text_input_id}']")
    text_input.fill("Harmonogram")
    assert text_input.is_visible() == True    # Before clicking the search button the elements are present
    assert button_search.is_visible() == True
    button_search.click()
    assert button_search.is_visible() == False    # After clicking the search button the page redirects to a different one
    assert text_input.is_visible() == False
    