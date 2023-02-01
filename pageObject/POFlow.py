from selenium import webdriver
from selenium.webdriver.common.by import By


class Banquite:
    #Bellow Xpath Element -

    def __init__(self,driver):
        self.driver = driver


    def banqute_name(self,name):
        self.driver.find_element(By.XPATH,self)
        self

