from selene import browser, be, have


def open():
    browser.open('/login')


def type_email(email):
    browser.element('[name="email"]').type(email)


def type_password(password):
    browser.element('[name="password"]').type(password)


def should_show_incorrect_email_or_password_error():
    browser.element('[data-show="error.serverPassError"]').should(be.visible)


def should_be_opened():
    browser.should(have.url(browser.config.base_url + '/login/'))


def submit():
    browser.element('[name="submit"]').click()
