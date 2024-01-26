from selene import browser


def open_or_refresh():
    url = '/app/#/expenses'
    if browser.driver.current_url.endswith(url):
        browser.driver.refresh()
    else:
        browser.open(url)
