from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Cokarge_DeleteItems:
    # Element Path - bellow

    click_delete_xpath = "(//*[@class='btn btn-danger deleteRecord'])[2]"





    def __init__(self,driver):
        self.driver = driver


    def click_delete(self):
        self.driver.find_element(By.XPATH, self.click_delete_xpath).click()
