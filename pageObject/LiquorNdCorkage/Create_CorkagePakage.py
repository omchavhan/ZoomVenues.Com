from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CreateCokargePage:
    # Element Path - bellow
    click_corkageList_xpath = "(//*[@href='http://vendor.zoomvenues.info/admin/corkage/list'])[1]"
    click_add_xpath = "//*[@class='btn btn-outline-primary float-right']"
    enter_corkagePackagenm_xpath = "//*[@name='corkage_package_name']"
    enter_price_path = "//*[@name='package_price']"
    enter_remark_xpath = "//*[@name='remark']"
    click_freq_use_xpath = "(//*[@class='form-check-input'])[1]"
    select_status_xpath = "//select[@name='status']"
    click_create_package_xpath = "//*[@class='btn btn-primary']"
    click_corkage_list_xpath = "(//*[@href='http://vendor.zoomvenues.info/admin/corkage/list'])[2]"



    def __init__(self,driver):
        self.driver = driver


    def click_Cokarge_List_T(self):
        self.driver.find_element(By.XPATH, self.click_corkageList_xpath).click()

    def click_Add(self):
        self.driver.find_element(By.XPATH, self.click_add_xpath).click()

    def enter_Cokarge_PackageName(self,Cokarge_packgename):
        corkage_Pname = self.driver.find_element(By.XPATH, self.enter_corkagePackagenm_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_corkagePackagenm_xpath).send_keys(Cokarge_packgename)

    def package_cokarge_price(self,co_price):
        e_price = self.driver.find_element(By.XPATH, self.enter_price_path).clear()
        self.driver.find_element(By.XPATH, self.enter_price_path).send_keys(co_price)

    def click_remark(self,remark):
        c_remark = self.driver.find_element(By.XPATH, self.enter_remark_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_remark_xpath).send_keys(remark)

    def click_frequenly(self):
        self.driver.find_element(By.XPATH, self.click_freq_use_xpath).click()

    def click_status(self):  # dropdown use active and inactive
        status = self.driver.find_element(By.XPATH, self.select_status_xpath)
        dropdown_status = Select(status)
        dropdown_status.select_by_index(0)

    def click_create_package(self):
        self.driver.find_element(By.XPATH, self.click_create_package_xpath).click()


    def click_corkagelist(self):
        self.driver.find_element(By.XPATH, self.click_corkageList_xpath).click()




