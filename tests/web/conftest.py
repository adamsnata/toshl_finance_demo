import os

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from toshl_finance_demo_test.data.context import Context
from toshl_finance_demo_test.utils import attach, api_utils
from toshl_finance_demo_test.utils.api import get_all_entries
from toshl_finance_demo_test.utils.api_utils import reqres_session


@pytest.fixture(scope="function", autouse=False)
def setup_browser(request):
    if request.config.getoption('--context') == Context.CLOUD:
        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "100.0",
            'selenoid:options': {
                'enableVNC': True,
                'enableVideo': True
            }
        }

        load_dotenv()
        login = os.getenv('SELENOID_LOGIN')
        password = os.getenv('SELENOID_PASSWORD')
        remote_url = os.getenv('SELENOID_REMOTE_URL', 'selenoid.autotests.cloud/wd/hub')
        options.capabilities.update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@{remote_url}",
            options=options
        )
        browser.config.driver = driver

    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://toshl.com'

    yield

    attach.html(browser)
    attach.screenshot(browser)
    attach.video(browser)
    attach.logs(browser)

    browser.quit()


@pytest.fixture(scope="function", autouse=False)
def browser_login(setup_browser, session):
    browser.open('/')
    # auth_cookie = session.cookies.get("tu")
    browser.driver.add_cookie({"name": "tu", "value": api_utils.cookie_tu})


@pytest.fixture(scope="function", autouse=False)
def remove_all_entries():
    entries = get_all_entries()
    for entry in entries:
        reqres_session.delete(url=f'/api/entries/{entry["id"]}')
