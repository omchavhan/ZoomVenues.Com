from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class LiquorPage:
    # Element Path - bellow
    click_liquor_xpath = "(//*[@href='http://vendor.zoomvenues.info/admin/liquor/list'])[1]"
    click_add_xpath = "//*[@class='btn btn-outline-primary float-right']"
    enter_liquorPackage_css = "#liquor_package_name"
    enter_houres_xpath = "(//*[@class='form-control'])[2]"
    enter_price_path = "(//*[@class='form-control'])[3]"
    click_freq_use_xpath = "(//*[@class='form-check-input'])[1]"
    select_status_xpath = "//select[@name='status']"
    click_create_package_xpath = "//*[@class='btn btn-primary']"
    select_liquortype_xpath = "//*[@name='liquor_type_id']"
    select_brand_xpath = "//*[@id='liquor_brand_id']"
    enter_liquordetail__xpath = "//*[@name='details']"
    click_Add_btn_xpath = "//*[@class='btn btn-primary w-100 mt-3']"
    click_delete_xpath = "//*[@class='btn btn-danger deleteRecord']"
    click_liquorlist_xpath = "(//*[@href='http://vendor.zoomvenues.info/admin/liquor/list'])[2]"





    def __init__(self,driver):
        self.driver = driver


    def click_Liquor_List(self):
        self.driver.find_element(By.XPATH, self.click_liquor_xpath).click()

    def click_Add(self):
        self.driver.find_element(By.XPATH, self.click_add_xpath).click()

    def enter_Liquor_PackageName(self,liquor_packgename):
        l_packagename = self.driver.find_element(By.CSS_SELECTOR, self.enter_liquorPackage_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.enter_liquorPackage_css).send_keys(liquor_packgename)

    def enter_hours(self,hours):
        e_hours = self.driver.find_element(By.XPATH, self.enter_houres_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_houres_xpath).send_keys(hours)

    def package_price(self,pa_price):
        p_price  = self.driver.find_element(By.XPATH, self.enter_price_path).clear()
        self.driver.find_element(By.XPATH, self.enter_price_path).send_keys(pa_price)

    def click_frequenly(self):
        self.driver.find_element(By.XPATH, self.click_freq_use_xpath).click()

    def click_status(self):  # dropdown use active and inactive
        status = self.driver.find_element(By.XPATH, self.select_status_xpath)
        dropdown_status = Select(status)
        dropdown_status.select_by_index(0)

    def click_create_package(self):
        self.driver.find_element(By.XPATH, self.click_create_package_xpath).click()


    def click_List_package(self):
        self.driver.find_element(By.XPATH, self.click_liquorlist_xpath).click()










