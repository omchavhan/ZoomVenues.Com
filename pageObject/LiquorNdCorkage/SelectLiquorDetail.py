import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SelectLiquorDetail:
    # Element Path - bellow
    click_liquor_xpath = "(//*[@href='http://vendor.zoomvenues.info/admin/liquor/list'])[1]"
    click_add_xpath = "//*[@class='btn btn-outline-primary float-right']"
    enter_liquorPackage_css = "#liquor_package_name"
    enter_houres_xpath = "//*[@id='no_of_hours']"
    enter_price_path = "//*[@id='package_price']"
    click_freq_use_xpath = "(//*[@class='form-check-input'])[1]"
    select_status_xpath = "//select[@name='status']"
    click_create_package_xpath = "//*[@class='btn btn-primary']"
    select_liquortype_xpath = "//*[@name='liquor_type_id']"
    select_brand_xpath = "//*[@class='form-control select2-hidden-accessible']"
    enter_liquordetail__xpath = "//*[@name='details']"
    click_Add_btn_xpath = "//*[@class='btn btn-primary w-100 mt-3']"
    click_delete_xpath = "//*[@class='btn btn-danger deleteRecord']"
    select_other_xpath = "//*[@class='select2-selection__rendered']"





    def __init__(self,driver):
        self.driver = driver

# Select Liquires

    def select_liquor_type(self):
        liquor_type = self.driver.find_element(By.XPATH, self.select_liquortype_xpath)
        dropdown_status = Select(liquor_type)
        dropdown_status.select_by_index(3)



    def select_brand(self):
        liquor_brand = self.driver.find_element(By.XPATH, self.select_brand_xpath)
        dropdown_brand = Select(liquor_brand)
        dropdown_brand.select_by_index(2)


    def select_brand_option(self):
        liquor_type = self.driver.find_element(By.XPATH, self.select_brand_xpath)
        self.driver.execute_script("arguments[0].click();", liquor_type)
        other = self.driver.find_element(By.XPATH, self.select_other_xpath)
        other.send_keys("Macallan Double Cask")
        time.sleep(2)
        other.send_keys(Keys.ENTER)



    def Enter_Details(self,details):
        e_details = self.driver.find_element(By.XPATH, self.enter_liquordetail__xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_liquordetail__xpath).send_keys(details)

    def click_Add_liquor(self):
        self.driver.find_element(By.XPATH, self.click_Add_btn_xpath).click()


    def click_delete(self):
         self.driver.find_element(By.XPATH, self.click_delete_xpath).click()










