from base_test import *
from pages.login_page import *


class TestLogin(BaseTest):

    def test_login_successfully(self):
        login_page = LoginPage(self.driver)
        dashboard_page = login_page.login_correct_credential()
        dashboard_page.is_loaded()

    def test_login_without_username_and_password(self):
        login_page = LoginPage(self.driver)
        login_page.click_login_button()
        login_page.check_error_toast()

    def test_login_with_incorrect_username_and_password(self):
        login_page = LoginPage(self.driver)
        login_page.login_invalid_credential()
        login_page.check_invalid_login_toast()
