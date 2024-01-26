import allure
from toshl_finance_demo_test.pages.mobile import expense_page
from toshl_finance_demo_test.data import category


@allure.feature('Mobile entries')
@allure.story('Expense')
@allure.suite('Add expense')
@allure.label('microservice', 'MEntry')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'mobile')
@allure.label('layer', 'mobile')
class TestExpense:
    @allure.title('Add expense')
    @allure.severity('blocker')
    def test_add_expense_without_tag(self, mobile_management, remove_all_entries, login_with_test_user):
        with allure.step('Click on "Add Expense" button'):
            expense_page.click_add_expense_button()
        with allure.step('Enter amount'):
            amount = 120
            expense_page.enter_amount(amount)
        with allure.step('Submit amount'):
            expense_page.submit_amount()
        with allure.step('Select category'):
            expense_page.enter_category(category.charity.name)
        with allure.step('Submit expense'):
            expense_page.submit_expense()

        with allure.step('Verify that expense is displayed'):
            expense_page.should_have_expenses_count(1)
            expenses = expense_page.get_expenses()
            expense_page.expense_should_have_category(expenses[0], category.charity.name)
            expense_page.expense_should_have_amount(expenses[0], amount)
