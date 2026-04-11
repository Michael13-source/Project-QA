import json
import pytest
from pages.login_page import LoginPage

def ambildatauser():
    with open('data/user.json') as file:
        return json.load(file)

@pytest.mark.parametrize('data_user', ambildatauser())

def test_login_variasi(driver, data_user):
    lgn_page = LoginPage(driver)
    lgn_page.open()
    lgn_page.login(data_user['username'], data_user['password'])
    if data_user['kategori'] == 'sukses':
        assert 'inventory.html' in driver.current_url
        ceklogo = lgn_page.get_logo_text()
        assert "Swag Labs" in ceklogo


   


