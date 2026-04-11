from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class BeliPage:
    

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 13)
        self.tas = (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
        self.keranjang = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
        self.check = (By.CSS_SELECTOR, '[data-test="checkout"]')
        self.nama_awal = (By.CSS_SELECTOR, '[data-test="firstName"]')
        self.nama_akhir = (By.CSS_SELECTOR, '[data-test="lastName"]')
        self.kode_pos = (By.CSS_SELECTOR, '[data-test="postalCode"]')
        self.cntn = (By.CSS_SELECTOR, '[data-test="continue"]')
        self.finish = (By.CSS_SELECTOR, '[data-test="finish"]')
        self.after_buy = (By.CSS_SELECTOR, '[data-test="back-to-products"]')

    def pickbackpack(self):
        self.wait.until(EC.visibility_of_element_located(self.tas)).click()
        self.wait.until(EC.visibility_of_element_located(self.keranjang)).click()
        self.wait.until(EC.visibility_of_element_located(self.check)).click()

    def prosesbeli(self, usr, passwd, kidipis):
        self.wait.until(EC.visibility_of_element_located(self.nama_awal)).send_keys(usr)
        self.wait.until(EC.visibility_of_element_located(self.nama_akhir)).send_keys(passwd)
        self.wait.until(EC.visibility_of_element_located(self.kode_pos)).send_keys(kidipis)
        self.wait.until(EC.visibility_of_element_located(self.cntn)).click()

    def prosesstep2(self):
        element = self.wait.until(EC.element_to_be_clickable(self.finish))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(EC.visibility_of(element)).click()

    def taphome(self):
        return self.wait.until(EC.visibility_of_element_located(self.after_buy)).click()
        

