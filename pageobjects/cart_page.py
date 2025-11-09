from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.webdriver_utils import safe_click, wait_for_ads_to_close


class CartPage:
    URL = "https://automationexercise.com/view_cart"

    # Elements
    CART_CONTAINER = (By.ID, "cart_info")
    CART_TABLE = (By.ID, "cart_info_table")
    CART_ROWS = (By.CSS_SELECTOR, "#cart_info_table tbody tr")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, ".cart_quantity_delete")
    EMPTY_CART_BANNER = (By.ID, "empty_cart")  # <span id="empty_cart" ...>

    def __init__(self, driver):
        self.driver = driver

    # ---------- Internal helpers ----------

    def _is_visible(self, locator, timeout=0.5):
        try:
            el = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return el.is_displayed()
        except Exception:
            return False

    def _table_is_visible(self):
        return self._is_visible(self.CART_TABLE, timeout=0.5)

    def _empty_banner_is_visible(self):
        return self._is_visible(self.EMPTY_CART_BANNER, timeout=0.5)

    def _wait_until_ready(self, timeout=15):
        """Page is ready when either the empty banner OR the table is visible."""
        wait_for_ads_to_close(self.driver)
        WebDriverWait(self.driver, timeout).until(
            lambda d: self._empty_banner_is_visible() or self._table_is_visible()
        )

    def _current_count(self):
        """Return rows count only if table is visible; else 0."""
        if not self._table_is_visible():
            return 0
        rows = self.driver.find_elements(*self.CART_ROWS)
        # Filter any non-item rows, if any
        rows = [
            r for r in rows
            if r.find_elements(By.CSS_SELECTOR, ".cart_quantity_delete, td.cart_product")
        ]
        return len(rows)

    # ---------- Public API ----------

    def open(self):
        """Open the cart page and wait until either table or empty banner is visible."""
        self.driver.get(self.URL)
        # container present ensures we’re on the correct page
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.CART_CONTAINER)
        )
        self._wait_until_ready()
        print("Cart page opened, URL:", self.driver.current_url)

    def get_cart_items_count(self):
        """Return number of items currently in the cart, robust against empty state."""
        self._wait_until_ready()
        if self._empty_banner_is_visible():
            print("Cart is empty banner visible.")
            return 0
        count = self._current_count()
        print(f"Counted cart items: {count}")
        return count

    def remove_first_item(self):
        """Remove the first item and wait until the cart updates deterministically."""
        self._wait_until_ready()
        initial_count = self.get_cart_items_count()
        if initial_count == 0:
            print("No items to remove.")
            return

        wait_for_ads_to_close(self.driver)
        buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
        if not buttons:
            print("No remove buttons found — cart already empty?")
            return

        print("Removing first item from cart...")
        safe_click(self.driver, buttons[0])
        WebDriverWait(self.driver, 20).until(EC.staleness_of(buttons[0]))

        # Wait until count decreases OR empty banner is shown
        WebDriverWait(self.driver, 20).until(
            lambda d: self._empty_banner_is_visible() or self.get_cart_items_count() < initial_count
        )
        print("Item removed and cart updated.")

    def is_cart_empty(self):
        """Check whether the cart is empty by the banner visibility."""
        try:
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(self.EMPTY_CART_BANNER)
            )
            print("✅ Empty cart message found.")
            return True
        except Exception as e:
            print("❌ Empty cart message not found:", e)
            print(self.driver.page_source)
            return False






