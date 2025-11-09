import pytest
from pageobjects.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("atharvajoshi046@gmail.com", "12345678")
        result = login_page.is_login_successful()
        if not result:
            print("Login success check failed. Page source:\n", self.driver.page_source)
        assert result

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("wronguser@example.com", "12345678")
        error_displayed = login_page.is_login_error_displayed()
        if not error_displayed:
            print("Login error message not found. Page source:\n", self.driver.page_source)
        assert error_displayed



