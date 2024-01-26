import allure

from config import config
from toshl_finance_demo_test.pages.mobile import welcome_page, login_page, expense_page


@allure.feature('Mobile authorization')
@allure.story('Login with username and password')
@allure.label('microservice', 'MLogin')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'mobile')
@allure.label('layer', 'mobile')
class TestLogin:
    @allure.title('Successful login')
    @allure.severity('blocker')
    def test_successful_login(self, mobile_management):
        with allure.step('Login with username and password'):
            welcome_page.click_login_link()
            login_page.login(config.TEST_USER_EMAIL)

        with allure.step('Verify that user is logged in'):
            expense_page.open_side_menu()
            expense_page.user_should_be_logged_in(config.TEST_USER_NAME)

    @allure.title('Login with incorrect password')
    @allure.severity('normal')
    def test_failed_with_incorrect_password(self, mobile_management):
        with allure.step('Open login page'):
            welcome_page.click_login_link()

        with allure.step('login with incorrect password'):
            login_page.click_login_with_email_button()
            login_page.type_email(config.TEST_USER_EMAIL)
            login_page.type_password('wring_password')
            login_page.submit()

        with allure.step('Verify that error message presents'):
            login_page.incorrect_email_or_password_message_should_present()
