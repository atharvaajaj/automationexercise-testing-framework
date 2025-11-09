import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pageobjects.signup_page import SignupPage

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestSignup:

    def test_valid_signup(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()
        signup_page.signup("Test User", "testuser123@example.com")
        # Add assertions or waits for successful signup

    def test_signup_existing_email(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()
        signup_page.signup("Test User", "existingemail@example.com")
        # Add assertions to check error message for existing email
