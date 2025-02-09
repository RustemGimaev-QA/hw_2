import pytest
from selene import browser, have, be

@pytest.fixture(autouse=True)
def browser_context():
    browser.config.window_height = 1366
    browser.config.window_width = 1024
    browser.open('https://ya.ru')
    yield
    browser.quit()

def test_success_search():
    browser.element('#text').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('core strength is its user-oriented API'))

def test_empty_search():
    browser.element('#text').should(be.blank).type('dlskldskdlk').press_enter()
    browser.element('html').should(have.text('Ничего не нашли'))