import allure

from toshl_finance_demo_test.components import confirmation_dialog
from toshl_finance_demo_test.components import right_panel
from toshl_finance_demo_test.components import transaction_details
from toshl_finance_demo_test.components import transaction_dialog
from toshl_finance_demo_test.data import category, tag
from toshl_finance_demo_test.data.transaction import EntryType
from toshl_finance_demo_test.pages.web import expenses_page
from toshl_finance_demo_test.utils import api


@allure.feature('Entries')
@allure.story('Expense')
@allure.label('microservice', 'Entry')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'web')
@allure.label('layer', 'web')
class TestExpense:
    @allure.title('Add expense')
    @allure.severity('blocker')
    def test_add_successfully_without_tag(self, browser_login, remove_all_entries):
        with allure.step("Open expenses page"):
            expenses_page.open_or_refresh()

        amount = '110'

        with allure.step("Add expense"):
            right_panel.click_add_button()
            transaction_dialog.set_amount(amount)
            transaction_dialog.set_category(category.education.name)
            transaction_dialog.click_save()

        with allure.step("Verify expense presents on the right panel"):
            right_panel.record_should_present(category.education.name, amount)

    @allure.title('Edit amount')
    @allure.severity('critical')
    def test_edit_amount(self, session, browser_login, remove_all_entries):
        initial_amount = '120'
        new_amount = '210'

        api.add_entry(session, EntryType.EXPENSE, category.charity.id, int(initial_amount))

        with allure.step("Open expenses page"):
            expenses_page.open_or_refresh()

        with allure.step("Edit expense amount"):
            right_panel.click_expense(initial_amount)
            transaction_details.click_edit_button()
            transaction_dialog.set_amount(new_amount)
            transaction_dialog.click_save()

        with allure.step("Verify expense has new amount in details"):
            transaction_details.should_have_amount(new_amount)

    @allure.title('Edit category')
    @allure.severity('normal')
    def test_edit_category(self, session, browser_login, remove_all_entries):
        amount = '130'
        api.add_entry(session, EntryType.EXPENSE, category.charity.id, int(amount))

        with allure.step("Open expenses page"):
            expenses_page.open_or_refresh()

        with allure.step("Edit expense category"):
            right_panel.click_expense(amount)
            transaction_details.click_edit_button()
            transaction_dialog.set_category(category.education.name)
            transaction_dialog.click_save()

        with allure.step("Verify expense has new category in details"):
            transaction_details.should_have_category(category.education.name)

    @allure.title('Add tag')
    @allure.severity('normal')
    def test_add_tag(self, session, browser_login, remove_all_entries):
        amount = '130'
        api.add_entry(session, EntryType.EXPENSE, category.education.id, int(amount))

        with allure.step("Open expenses page"):
            expenses_page.open_or_refresh()

        with allure.step("Add tag to the expense"):
            right_panel.click_expense(amount)
            transaction_details.click_edit_button()
            transaction_dialog.set_tag(tag.books.name)
            transaction_dialog.click_save()

        with allure.step("Verify the tag presents in expense details"):
            transaction_details.should_have_tag(tag.books.name)

    @allure.title('Remove tag')
    @allure.severity('normal')
    def test_remove_tag(self, session, browser_login, remove_all_entries):
        amount = '130'
        api.add_entry(session, EntryType.EXPENSE, category.education.id, int(amount), tag_ids=[tag.books.id])

        with allure.step("Open expenses page"):
            expenses_page.open_or_refresh()

        with allure.step("Remove tag from the expense"):
            right_panel.click_expense(amount)
            transaction_details.click_edit_button()
            transaction_dialog.remove_tag(tag.books.name)
            transaction_dialog.click_save()

        with allure.step("Verify expense presents on the right panel"):
            transaction_details.should_not_have_tags()

    @allure.title('Duplicate')
    @allure.severity('minor')
    def test_duplicate(self, session, browser_login, remove_all_entries):
        amount = '130'
        api.add_entry(session, EntryType.EXPENSE, category.education.id, int(amount))

        with allure.step("Open expenses page"):
            expenses_page.open_or_refresh()

        with allure.step("Duplicate the expense"):
            right_panel.click_expense(amount)
            transaction_details.click_duplicate_button()
            transaction_dialog.click_save()

        with allure.step("Verify expense is listed twice"):
            right_panel.should_have_records_count(2)

    @allure.title('Delete')
    @allure.severity('critical')
    def test_delete(self, session, browser_login, remove_all_entries):
        amount = '130'
        api.add_entry(session, EntryType.EXPENSE, category.education.id, int(amount))

        with allure.step("Open expenses page"):
            expenses_page.open_or_refresh()

        with allure.step("Delete expense"):
            right_panel.click_expense(amount)
            transaction_details.click_delete_button()
            confirmation_dialog.confirm_delete()

        with allure.step("Verify the list of expenses is empty"):
            right_panel.should_have_records_count(0)
