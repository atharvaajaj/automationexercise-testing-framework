from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.webdriver_utils import wait_for_ads_to_close


class LoginPage:
    URL = "https://automationexercise.com/login"

    # Robust form locators (prefer data-qa, fallback to form-scoped name)
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email'], form[action*='login'] input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-password'], form[action*='login'] input[name='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")

    # Messages
    SUCCESS_MESSAGE = (By.XPATH, "//li/a[contains(., 'Logged in as')]")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(., 'Your email or password is incorrect')]")

    # Header state
    HEADER_LOGGED_IN_AS = (By.XPATH, "//li/a[contains(., 'Logged in as')]")
    HEADER_LOGOUT = (By.XPATH, "//a[@href='/logout']")
    HEADER_LOGIN_LINK = (By.XPATH, "//a[@href='/login']")

    def __init__(self, driver):
        self.driver = driver

    # ---------- helpers ----------

    def _page_ready(self, timeout=12):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
        except Exception:
            pass  # don't be strict here

    def _is_logged_in(self):
        try:
            return bool(
                self.driver.find_elements(*self.HEADER_LOGGED_IN_AS) or
                self.driver.find_elements(*self.HEADER_LOGOUT)
            )
        except Exception:
            return False

    def _force_logout(self):
        """Best-effort logout: header link -> fallback to /logout."""
        try:
            els = self.driver.find_elements(*self.HEADER_LOGOUT)
            if els:
                try:
                    els[0].click()
                except Exception:
                    self.driver.execute_script("arguments[0].click();", els[0])
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.HEADER_LOGIN_LINK)
                )
                return
        except Exception:
            pass
        self.driver.get("https://automationexercise.com/logout")
        self._page_ready(6)

    # ---------- public API ----------

    def open(self):
        """Navigate to /login in a way that survives overlays + existing sessions."""
        # Ensure logged-out state first (prevents /login redirect/absence)
        self.driver.get("https://automationexercise.com/")
        wait_for_ads_to_close(self.driver)
        self._page_ready(6)
        if self._is_logged_in():
            self._force_logout()
            wait_for_ads_to_close(self.driver)

        # Try direct URL
        self.driver.get(self.URL)
        wait_for_ads_to_close(self.driver)
        self._page_ready(10)
        if "/login" in (self.driver.current_url or ""):
            print("Login page opened (direct), URL:", self.driver.current_url)
            return

        # Fallback 1: header link, with JS-click backup
        try:
            wait_for_ads_to_close(self.driver)
            link = WebDriverWait(self.driver, 12).until(
                EC.element_to_be_clickable(self.HEADER_LOGIN_LINK)
            )
            try:
                link.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", link)
            wait_for_ads_to_close(self.driver)
            self._page_ready(10)
            if "/login" in (self.driver.current_url or ""):
                print("Login page opened (via header link), URL:", self.driver.current_url)
                return
        except Exception as e:
            print("Header link fallback failed:", e)

        # Fallback 2: hard JS redirect (works even if click blocked)
        self.driver.execute_script("window.location = arguments[0];", self.URL)
        wait_for_ads_to_close(self.driver)
        self._page_ready(12)
        print("Login page opened (via JS redirect), URL:", self.driver.current_url)

    def login(self, email, password):
        """Attempt to log in with the provided credentials."""
        wait_for_ads_to_close(self.driver)

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        email_field = self.driver.find_element(*self.EMAIL_INPUT)
        email_field.clear()
        email_field.send_keys(email)

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        password_field = self.driver.find_element(*self.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        print(f"Login attempted with email: {email}")

    def is_login_successful(self):
        """True if the 'Logged in as' header shows up."""
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
            )
            print("✅ Login successful message found.")
            return True
        except Exception as e:
            print("❌ Login success check failed:", e)
            print(self.driver.page_source)
            return False

    def is_login_error_displayed(self):
        """True if the invalid-login error banner appears."""
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            print("✅ Login error message found.")
            return True
        except Exception as e:
            print("❌ Login error message not found:", e)
            print(self.driver.page_source)
            return False






