from selenium.webdriver.common.by import By

class SearchPage:
    URL = "https://automationexercise.com/products"
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".features_items .product-image-wrapper")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def search(self, product_name):
        self.driver.find_element(*self.SEARCH_INPUT).clear()
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(product_name)
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def get_search_results_count(self):
        return len(self.driver.find_elements(*self.SEARCH_RESULTS))

    def is_no_results_message_displayed(self):
        return self.get_search_results_count() == 0





