from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class DashboardPage:
    URL = 'https://www.saucedemo.com/inventory.html'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 13)
        self.title = (By.CSS_SELECTOR, '[data-test="title"]')
        self.cart_icon = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
        self.menu_button = (By.ID, 'react-burger-menu-btn')


    def is_loaded(self):
        return self.wait.until(EC.visibility_of_element_located(self.title))

    def get_title_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.title)).text

    def open_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.menu_button)).click()