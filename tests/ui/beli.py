from selenium import webdriver
from pages.login_page import LoginPage
from pages.beli_page import BeliPage

def test_bli(driver):
    page = LoginPage(driver)
    page.open()
    page.login('standard_user', 'secret_sauce')
    bpage = BeliPage(driver)
    bpage.pickbackpack()
    bpage.prosesbeli('ananda', 'MLG772', '68471')
    bpage.prosesstep2()
    bpage.taphome()