from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.webdriver_utils import safe_click, wait_for_ads_to_close

class HomePage:
    URL = "https://automationexercise.com/"
    PRODUCTS_LINK = (By.XPATH, "//a[contains(text(),'Products')]")
    SIGNUP_LOGIN_LINK = (By.LINK_TEXT, "Signup / Login")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def go_to_products(self):
        wait_for_ads_to_close(self.driver)
        elem = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PRODUCTS_LINK)
        )
        safe_click(self.driver, elem)

    def go_to_signup_login(self):
        wait_for_ads_to_close(self.driver)
        elem = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SIGNUP_LOGIN_LINK)
        )
        safe_click(self.driver, elem)

