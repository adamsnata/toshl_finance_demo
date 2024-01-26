from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, Element, be
from selenium.webdriver import ActionChains


def click_add_expense_button():
    add_expense_button_rect = browser.element((AppiumBy.ID, 'addItemButton')).locate().rect
    # The button itself has an indent from the left border of the element
    # 75 is selected is a constant which should suit most environments
    x = 75 - add_expense_button_rect['width'] / 2
    y = add_expense_button_rect['height'] / 2 - 1

    add_button = browser.element((AppiumBy.ID, 'addItemButton')).locate()
    ActionChains(browser.driver).move_to_element_with_offset(add_button, x, y).click().perform()


def enter_amount(amount: int):
    for digit in str(amount):
        browser.element((AppiumBy.ID, f'keypad_{digit}')).click()


def submit_amount():
    browser.element((AppiumBy.ID, 'keypad_next')).click()


def enter_category(category_name: str):
    browser.element((AppiumBy.XPATH, f'//android.widget.TextView[@text="{category_name}"]')).click()


def submit_expense():
    browser.element((AppiumBy.ID, 'ivConfirm')).click()


def get_expenses():
    return browser.all((AppiumBy.CLASS_NAME, 'android.widget.TableRow'))


def should_have_expenses_count(count):
    get_expenses().should(have.size(count))


def expense_should_have_category(expense: Element, category_name: str):
    expense.element((AppiumBy.ID, 'tvCategory')).should(have.text(category_name))


def expense_should_have_amount(expense: Element, amount: int):
    expense.element((AppiumBy.ID, 'tvAmount')).should(have.text(f'GEL{amount}.00'))


def open_side_menu():
    browser.element((AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Menu']")).click()


def user_should_be_logged_in(username: str):
    (browser.element((AppiumBy.XPATH, f'//android.widget.TextView[@resource-id="com.thirdframestudios.'
                                      f'android.expensoor:id/tvLeftNavItemTitle" '
                                      f'and @text="{username}"]'))
     .should(be.present))
