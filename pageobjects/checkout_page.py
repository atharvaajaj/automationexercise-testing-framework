from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.webdriver_utils import safe_click, wait_for_ads_to_close

class CheckoutPage:
    URL = "https://automationexercise.com/checkout"

    PLACE_ORDER_BUTTON = (By.XPATH, "//a[contains(text(),'Place Order')]")
    NAME_INPUT = (By.NAME, "name_on_card")
    CARD_NUMBER_INPUT = (By.NAME, "card_number")
    CVC_INPUT = (By.NAME, "cvc")
    EXPIRY_MONTH_INPUT = (By.NAME, "expiry_month")
    EXPIRY_YEAR_INPUT = (By.NAME, "expiry_year")
    PAY_BUTTON = (By.ID, "submit")

    ORDER_SUCCESS_TEXT = (By.XPATH, "//p[contains(text(),'Congratulations! Your order has been confirmed!')]")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def place_order(self, name_on_card, card_number, cvc, expiry_month, expiry_year):
        wait_for_ads_to_close(self.driver)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PLACE_ORDER_BUTTON)
        )
        safe_click(self.driver, self.driver.find_element(*self.PLACE_ORDER_BUTTON))

        self.driver.find_element(*self.NAME_INPUT).send_keys(name_on_card)
        self.driver.find_element(*self.CARD_NUMBER_INPUT).send_keys(card_number)
        self.driver.find_element(*self.CVC_INPUT).send_keys(cvc)
        self.driver.find_element(*self.EXPIRY_MONTH_INPUT).send_keys(expiry_month)
        self.driver.find_element(*self.EXPIRY_YEAR_INPUT).send_keys(expiry_year)

        safe_click(self.driver, self.driver.find_element(*self.PAY_BUTTON))

    def is_order_successful(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.ORDER_SUCCESS_TEXT)
            )
            return True
        except:
            return False

