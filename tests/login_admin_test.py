from pages.Login import Login
from data import config

def test_login_admin(driver):
    login_page = Login(driver)
    if(login_page.isLogin()):
        login_page.signOut()
    login_page.load(config.BASE_URL)
    login_page.enter_username(config.ADMIN_EMAIL)
    login_page.enter_password(config.ADMIN_PASSOWRD)
    login_page.click_btn_login()