from selene import browser, have

def test_browser_duckduckgo(open_browser):
    browser.element('#searchbox_input').type('алмаFRTS').press_enter()
    browser.element('html').should(have.text('По запросу алмаFRTS результаты не найдены.'))