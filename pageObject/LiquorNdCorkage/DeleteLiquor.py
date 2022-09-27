from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DeleteLiquor:
    # Element Path - bellow
    click_delete_xpath = "//*[@id='userTable']/tbody/tr[1]/td[5]/button"
    click_editlist_xpath = "//*[@href='http://vendor.zoomvenues.info/admin/liquor/edit-package/15']"







    def __init__(self,driver):
        self.driver = driver

    def click_Edit_list(self):
        self.driver.find_element(By.XPATH, self.click_editlist_xpath).click()

    def click_Liquor_Delete(self):
        self.driver.find_element(By.XPATH, self.click_delete_xpath).click()










