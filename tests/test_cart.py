import pytest
from selenium.webdriver.common.by import By
from pageobjects.home_page import HomePage
from pageobjects.cart_page import CartPage
from utils.webdriver_utils import safe_click, wait_for_ads_to_close

@pytest.mark.usefixtures("setup")
class TestCart:

    def test_add_to_cart(self):
        homepage = HomePage(self.driver)
        homepage.open()
        homepage.go_to_products()

        wait_for_ads_to_close(self.driver)

        product = self.driver.find_element(By.CSS_SELECTOR, ".product-image-wrapper")
        add_to_cart_btn = product.find_element(By.CSS_SELECTOR, "a.add-to-cart")
        safe_click(self.driver, add_to_cart_btn)
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

# Wait for the "Added!" modal, then click "View Cart"
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cartModal")))
        self.driver.find_element(By.CSS_SELECTOR, "#cartModal a[href='/view_cart']").click()


        cart_page = CartPage(self.driver)
        cart_page.open()
        cart_items_count = cart_page.get_cart_items_count()

        assert cart_items_count > 0

    def test_remove_from_cart(self):
        cart_page = CartPage(self.driver)
        cart_page.open()

        initial_count = cart_page.get_cart_items_count()
        if initial_count == 0:
            pytest.skip("Cart is empty, skipping removal test")
        cart_page.remove_first_item()

        if initial_count == 1:
            assert cart_page.is_cart_empty()
        else:
            assert cart_page.get_cart_items_count() == initial_count - 1




