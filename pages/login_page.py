from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class LoginPage:
    URL = 'https://www.saucedemo.com'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 13)
        self.username = (By.CSS_SELECTOR, '[data-test="username"]')
        self.password = (By.CSS_SELECTOR, '[data-test="password"]')
        self.login_button = (By.CSS_SELECTOR, '[data-test="login-button"]')
        self.logo = (By.CLASS_NAME, 'app_logo')
        self.error_message = (By.CSS_SELECTOR, '[data-test="error"]')

    def open(self):
        self.driver.get(self.URL)

    def login(self, user, pwd):
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(user)
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(pwd)
        self.wait.until(EC.visibility_of_element_located(self.login_button)).click()

    def wait_for_error(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_message)).text

    def get_logo_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.logo)).text

