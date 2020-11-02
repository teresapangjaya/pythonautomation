from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.BaseHelper import BaseHelper
import random

class OrganizationCredentialTypePriceMenu(BaseHelper):
    MENU_ICON = (By.CLASS_NAME , 'fa-sitemap')
    MENU_NAME = (By.XPATH, '//*[contains(@title, \'Manage the Organisation Credential Type Prices\')]')
    MENU_CREATE = (By.XPATH, '//a[contains(text(), \'Create New\')]')
    INPUT_ORGANIZATION = (By.ID, 'OrgId')
    INPUT_CREDENTIAL_TYPE = (By.ID, 'TypeId')
    INPUT_PRICE = (By.ID, 'Price')
    BTN_SUBMIT = (By.CSS_SELECTOR, 'button[type=submit]')

    def load(self):
        (self.driver.find_element(*self.MENU_ICON)).click()
        (self.driver.find_element(*self.MENU_NAME)).click()

    def click_btn_create_new(self):
        btn_create = self.driver.find_element(*self.MENU_CREATE)
        btn_create.click()

    def choose_organization(self, option = ''):
        select_organization = Select(self.driver.find_element(*self.INPUT_ORGANIZATION))
        if(option != ''):
            select_organization.select_by_visible_text(option)
        else:
            self.choose_random_option(select_organization)

    def choose_type(self, option = ''):
        select_type = Select(self.driver.find_element(*self.INPUT_CREDENTIAL_TYPE))
        if(option != ''):
            select_type.select_by_visible_text(option)
        else:
            self.choose_random_option(select_type)

    def enter_price(self, value = ''):
        txt_price = self.driver.find_element(*self.INPUT_PRICE)
        txt_price.clear()
        if(value != ''):
            txt_price.send_keys(value)
        else:
            txt_price.send_keys(random.randint(1, 10))

    def click_btn_submit(self):
        btn_create = self.driver.find_element(*self.BTN_SUBMIT)
        btn_create.click()