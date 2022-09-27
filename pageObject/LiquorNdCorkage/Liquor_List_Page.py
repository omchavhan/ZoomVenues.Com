from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class liquor_list_page:
    # Element Path - bellow


    def __init__(self,driver):
        self.driver = driver

    def click_edit(self):
        self.driver.find_element(By.XPATH,self.).click()

