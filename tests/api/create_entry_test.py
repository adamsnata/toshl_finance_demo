from datetime import datetime
import allure
import requests

from config import config
from toshl_finance_demo_test.data import category
from toshl_finance_demo_test.utils.api_utils import reqres_session


@allure.feature('Entry API')
@allure.story('Create entry')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'API')
@allure.label('layer', 'API')
class TestCreateEntry:
    @allure.title('Create income entry')
    @allure.severity('blocker')
    # def test_create_income_success(self, session, remove_all_entries):
    def test_create_income_success(self, session):
        with allure.step("Create entry"):
            resp = reqres_session.post(url=f'/api/entries',
                                params={"immediate_update": "true"},
                                json={"amount": 120,
                                      "date": datetime.now().strftime("%Y-%m-%d"),
                                      "currency":
                                          {"code": "GEL"
                                           },
                                      "account": "4346873",
                                      "category": category.grants.id,
                                      "tags": []})

        with allure.step("Validate response status"):
            assert resp.status_code == requests.codes.created

        with allure.step("Validate response content is empty"):
            assert resp.content.decode() == ''
