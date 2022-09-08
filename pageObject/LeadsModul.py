from selenium.webdriver.common.by import By
import time


class LeadsModul:
    leads_xpath = "(//*[@href='http://vendor.zoomvenues.info/admin/enquiries/leads'])[1]"
    edit_xpath = "//*[@href='http://vendor.zoomvenues.info/admin/enquiries/editleads-new/607']"

    def __init__(self,driver):
        self.driver = driver

    def click_leads(self):
        self.driver.find_element(By.XPATH,self.leads_xpath).click()

    def click_edit(self):
        self.driver.find_element(By.XPATH, self.edit_xpath).click()

