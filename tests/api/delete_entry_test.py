import allure
import requests

from toshl_finance_demo_test.data import category
from toshl_finance_demo_test.data.transaction import EntryType
from toshl_finance_demo_test.utils.api import add_entry, get_all_entries
from toshl_finance_demo_test.utils.api_utils import reqres_session


@allure.feature('Entry API')
@allure.story('Delete entry')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'API')
@allure.label('layer', 'API')
class TestCreateEntry:
    @allure.title('Delete entry successfully')
    @allure.severity('blocker')
    def test_delete_existing_entry(self, session, remove_all_entries):
        with allure.step("Create entry"):
            add_entry(session, EntryType.EXPENSE, category.education.id, 120)
            entries = get_all_entries()

        with allure.step("Delete entry"):
            resp = reqres_session.delete(url=f'/api/entries/{entries[0]["id"]}')

        with allure.step("Validate response status"):
            assert resp.status_code == requests.codes.no_content

        with allure.step("Validate response content is empty"):
            assert resp.content.decode() == ''

    @allure.title('Delete not existing entry')
    @allure.severity('normal')
    def test_delete_not_existing_entry_should_fail(self, session, remove_all_entries):
        not_existing_id = "1"
        with allure.step("Delete entry"):
            resp = reqres_session.delete(url=f'/api/entries/{not_existing_id}')

        with allure.step("Validate response status is 404"):
            assert resp.status_code == requests.codes.not_found

        with allure.step("Validate response content is empty"):
            assert resp.json()['description'] == f'Object with id {not_existing_id} not found.'
