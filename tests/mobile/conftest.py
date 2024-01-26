import allure
import allure_commons
import pytest
from _pytest.stash import StashKey
from appium import webdriver
from selene import browser, support

from config import config
from toshl_finance_demo_test.data.context import Context

from toshl_finance_demo_test.pages.mobile import welcome_page, login_page
from toshl_finance_demo_test.utils import attach
from .config import load_config

config_key = StashKey()


def pytest_configure(config):
    context = config.getoption('--context')
    config.stash[config_key] = load_config(context)


@pytest.fixture(scope='function', autouse=True)
def mobile_management(pytestconfig):
    config = pytestconfig.stash[config_key]

    browser.config.timeout = config.timeout

    with allure.step('Init app session'):
        browser.config.driver = webdriver.Remote(
            config.remote_url,
            options=config.to_driver_options()
        )

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    attach.screenshot(browser)
    attach.screen_xml_dump(browser)
    session_id = browser.driver.session_id

    with allure.step('Tear down app sessioncwith id' + session_id):
        browser.quit()

    if pytestconfig.getoption('--context') == Context.CLOUD:
        attach.bstack_video(session_id, config.options.bs_username, config.options.bs_password)


@pytest.fixture(scope='function', autouse=False)
def login_with_test_user():
    welcome_page.click_login_link()
    login_page.login(config.TEST_USER_NAME)
