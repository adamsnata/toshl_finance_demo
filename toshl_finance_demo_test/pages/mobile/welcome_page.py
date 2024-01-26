from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


def click_login_link():
    browser.element((AppiumBy.ID, "btnLogin")).click()
