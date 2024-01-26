import allure
import pytest
import requests

from config import config
from toshl_finance_demo_test.data.context import Context
from toshl_finance_demo_test.utils import api_utils
from toshl_finance_demo_test.utils.api import get_all_entries
from toshl_finance_demo_test.utils.api_utils import reqres_session




def pytest_addoption(parser):
    parser.addoption(
        '--context',
        type=Context,
        choices=list(Context),
        default=Context.CLOUD,
        help='Run tests locally or in cloud services'
    )


@pytest.fixture(scope="function", autouse=False)
def session():
    with allure.step("Login to Toshl Finance"):

        print('Ich bin da')
        # s = requests.Session()
        # s.hooks['response'] += [attach_request_and_response_data, log_request_and_response_data_to_console]
        request = reqres_session.post(url='/oauth2/login',
               data={"email": config.TEST_USER_EMAIL,
                     "password": config.TEST_USER_PASSWORD})

        api_utils.cookie_tu = request.cookies['tu']
        # api_utils.cookies = request.cookies
    return request


@pytest.fixture(scope="function", autouse=False)
def remove_all_entries():
    print('Ich bin da remove_all_entries')
    with allure.step("Remove all entries from test account"):
        entries = get_all_entries()
        for entry in entries:
            reqres_session.delete(url=f'/api/entries/{entry["id"]}')
