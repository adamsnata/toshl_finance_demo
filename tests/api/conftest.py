import allure
import pytest

from config import config
from toshl_finance_demo_test.utils.api import get_all_entries
from toshl_finance_demo_test.utils.api_utils import reqres_session


@pytest.fixture(scope="function", autouse=False)
def remove_all_entries():
    with allure.step("Remove all entries from test account"):
        entries = get_all_entries()
        for entry in entries:
            reqres_session.delete(url=f'/api/entries/{entry["id"]}')
