from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Cokarge_SelectItems:
    # Element Path - bellow
    select_type_xpath = "//*[@name='liquor_type_id']"
    enter_qty_xpath ="//*[@id='quantity']"
    select_unit_xpath = "//*[@id='unit']"
    enter_price_xpath = "//*[@id='price']"
    enter_remark_xpath = "//*[@id='remark']"
    click_add_btn_xpath = "//*[@id='liquorPackageItem']"
    click_delete_xpath = "(//*[@class='btn btn-danger deleteRecord'])[2]"





    def __init__(self,driver):
        self.driver = driver


    def select_type(self):
        select_type = self.driver.find_element(By.XPATH, self.select_type_xpath)
        dropdown_status = Select(select_type)
        dropdown_status.select_by_index(3)


    def enter_Qunity(self,qty):
        e_qtr = self.driver.find_element(By.XPATH, self.enter_qty_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_qty_xpath).send_keys(qty)


    def select_unit(self):
        select_unit = self.driver.find_element(By.XPATH, self.select_unit_xpath)
        dropdown_unit = Select(select_unit)
        dropdown_unit.select_by_index(3)

    def enter_price(self,price):
        self.driver.find_element(By.XPATH, self.enter_price_xpath).send_keys(price)

    def enter_remark(self,remark):
        e_remark = self.driver.find_element(By.XPATH, self.enter_remark_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_remark_xpath).send_keys(remark)

    def click_Add_cokarge(self):
        self.driver.find_element(By.XPATH, self.click_add_btn_xpath).click()

