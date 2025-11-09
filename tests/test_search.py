import pytest
from pageobjects.search_page import SearchPage

@pytest.mark.usefixtures("setup")
class TestSearch:

    def test_search_valid_product(self):
        search_page = SearchPage(self.driver)
        search_page.open()
        search_page.search("Blue Top")
        assert search_page.get_search_results_count() > 0
        assert not search_page.is_no_results_message_displayed()

    def test_search_invalid_product(self):
        search_page = SearchPage(self.driver)
        search_page.open()
        search_page.search("xyznotaproduct")
        assert search_page.is_no_results_message_displayed()
        assert search_page.get_search_results_count() == 0

