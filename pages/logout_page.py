from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class LogoutPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 13)
        self.menu = (By.ID, 'react-burger-menu-btn')
        self.logout = (By.CSS_SELECTOR, '[data-test="logout-sidebar-link"]')
        self.checkuiout = (By.CLASS_NAME, "login_logo")

    def outweb(self):
        self.wait.until(EC.visibility_of_element_located(self.menu)).click()
        self.wait.until(EC.visibility_of_element_located(self.logout)).click()
        
    def check(self):
       ui = self.wait.until(EC.visibility_of_element_located (self.checkuiout))
       return ui.text
