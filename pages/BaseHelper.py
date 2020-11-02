from selenium import webdriver
import random

class BaseHelper:
    def __init__(self, driver):
        self.driver = driver
    def load(self, url):
        self.driver.get(url)
    def choose_random_option(self, select_element):
        select_element.select_by_index(random.randint(0, (len((select_element).options) - 1)))