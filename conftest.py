import pytest
from selene import browser

@pytest.fixture(autouse=True)
def browser_screen_resolution():
    browser.config.window_height = 1024
    browser.config.window_width = 1500

@pytest.fixture()
def open_browser(browser_screen_resolution):
    browser.open('https://duckduckgo.com/')
    yield
    browser.quit()