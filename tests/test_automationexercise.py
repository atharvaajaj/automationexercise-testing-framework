import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pageobjects.home_page import HomePage
from pageobjects.search_page import SearchPage

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestAutomationExercise:

    def test_open_homepage(self):
        homepage = HomePage(self.driver)
        homepage.open()
        assert "Automation Exercise" in self.driver.title

    def test_navigate_products(self):
        homepage = HomePage(self.driver)
        homepage.open()
        homepage.go_to_products()
        assert "Products" in self.driver.title

    def test_search_product(self):
        search_page = SearchPage(self.driver)  # Use SearchPage object!
        search_page.open()
        search_page.search("Blue Top")
        assert search_page.get_search_results_count() > 0

