from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException  
from pages.BaseHelper import BaseHelper

class Login(BaseHelper):
    INPUT_USERNAME = (By.ID, 'Email')
    INPUT_PASSWORD = (By.ID, 'Password')
    BTN_SUBMIT = (By.CSS_SELECTOR, 'button[type=submit]')
    PROFILE_LINK = (By.CLASS_NAME, 'profile-info')
    SIGN_OUT = (By.XPATH, '//a[contains(text(), \'Sign Out\')]')
    def enter_username(self, username):
        txt_username = self.driver.find_element(*self.INPUT_USERNAME)
        txt_username.clear()
        txt_username.send_keys(username)

    def enter_password(self, password):
        txt_password = self.driver.find_element(*self.INPUT_PASSWORD)
        txt_password.clear()
        txt_password.send_keys(password)

    def click_btn_login(self):
        btn_login = self.driver.find_element(*self.BTN_SUBMIT)
        btn_login.click()

    def isLogin(self):
        try:
            self.driver.find_element(*self.PROFILE_LINK)
        except NoSuchElementException:
            return False
        return True
    
    def signOut(self):
        self.driver.find_element(*self.PROFILE_LINK).click()
        self.driver.find_element(*self.SIGN_OUT).click()