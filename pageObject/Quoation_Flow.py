from selenium import webdriver
from selenium.webdriver.common.by import By


class Quoation:
    # Web Elements Path Bellow -

    BH_xpath = "(//*[@href='http://vendor.zoomvenues.info/admin/hubs/all'])[1]"
    sign_contract_create_xpath = "(//*[@class='nav-icon fas fa-file text-warning FileText'])[1]"
    commission_rate_txtbox_xpath = "(//*[@name='commision_rate'])[1]"
    save_xpath = "(//input[@value='Save'])[43]"
    submit_xpath = "(//*[@class='btn btn-primary'])[1]"
    contract_pdf_xpath = "(//*[@class='text-dark nav-icon fas fa-print PrintText'])[1]"


    def __init__(self,driver):
        self.driver = driver

    def click_BH(self):
        self.driver.find_element(By.XPATH,self.BH_xpath).click()

    def click_sign_contract_create(self):
        self.driver.find_element(By.XPATH,self.sign_contract_create_xpath).click()

    def enter_commission_rate(self,commission_rate):
        self.driver.find_element(By.XPATH,self.commission_rate_txtbox_xpath).send_keys(commission_rate)

    def click_save(self):
        self.driver.find_element(By.XPATH,self.save_xpath).click()

    def click_BH_submit(self):
        self.driver.find_element(By.XPATH,self.submit_xpath).click()

    def click_contract_pdf_view(self):
        self.driver.find_element(By.XPATH,self.contract_pdf_xpath).click()

