import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pageobjects.checkout_page import CheckoutPage

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestCheckout:

    def test_place_order_success(self):
        checkout_page = CheckoutPage(self.driver)
        checkout_page.open()

        # Use valid dummy payment info (ensure it matches required format)
        checkout_page.place_order(
            name_on_card="Test User",
            card_number="4111111111111111",
            cvc="123",
            expiry_month="12",
            expiry_year="2025"
        )
        assert checkout_page.is_order_successful()
