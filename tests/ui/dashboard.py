from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_title(driver):
    page = LoginPage(driver)
    page.open()
    page.login('standard_user', 'secret_sauce')
    Dpage = DashboardPage(driver)
    cek_title = Dpage.get_title_text()
    assert cek_title == 'Products'
    Dpage.open_menu()

