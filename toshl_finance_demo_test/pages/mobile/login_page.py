from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be


def login(user):
    browser.element((AppiumBy.ID, "btnLogin")).click()
    browser.element((AppiumBy.ID, "etEmail")).type(user.email)
    browser.element((AppiumBy.ID, "etPassword")).type(user.password)
    browser.element((AppiumBy.ID, "bLogIn")).click()

    package = browser.driver.current_package
    browser.wait_until((AppiumBy.XPATH, '//android.widget.TextView[@text="I’m syncing..."]'))
    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="I’m syncing..."]')).should(be.not_.present)

    # The application has a bug: after the very first login it shows a gray screen
    # It works properly after restart. So we do the restart.
    browser.driver.terminate_app(package, timeout=3000)
    browser.driver.activate_app(package)
    browser.element((AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Menu']")).should(be.present)


def click_login_with_email_button():
    browser.element((AppiumBy.ID, "btnLogin")).click()


def type_email(email):
    browser.element((AppiumBy.ID, "etEmail")).type(email)


def type_password(password):
    browser.element((AppiumBy.ID, "etPassword")).type(password)


def submit():
    browser.element((AppiumBy.ID, "bLogIn")).click()


def incorrect_email_or_password_message_should_present():
    incorrect_password_message = "The e-mail or password you provided is not correct. Please try again."
    browser.element((AppiumBy.XPATH, f'//*[@text="{incorrect_password_message}"]')).should(be.present)
