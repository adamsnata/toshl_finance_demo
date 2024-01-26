from selene import browser, have


def set_amount(value):
    browser.element('.amount-input').set_value(value)


def set_category(value):
    browser.element('#addent_category').type(value).press_enter()


def click_save():
    browser.element('[ng-click="savable && onSaveButtonClick()"]').click()


def set_tag(value):
    browser.element('#addent_tags').type(value).press_enter()


def remove_tag(value):
    browser.element('#addent_tags').click()
    browser.all('.presets-tag').element_by(have.exact_text(value)).click()
