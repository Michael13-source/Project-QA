from selenium import webdriver
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage

def test_logout(driver):
    page = LoginPage(driver)
    page.open()
    page.login('standard_user', 'secret_sauce')
    Lpage = LogoutPage(driver)
    Lpage.outweb()