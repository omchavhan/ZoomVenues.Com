from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class EditLiquorPackages:
    # Element Path - bellow
    click_edit_xpath = "(//*[@class='nav-icon fas fa-edit'])[1]"



    def __init__(self,driver):
        self.driver = driver

    def click_edit(self):
        self.driver.find_element(By.XPATH,self.click_edit_xpath).click()




