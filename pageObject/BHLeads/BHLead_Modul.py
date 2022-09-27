from selenium import webdriver
from selenium.webdriver.common.by import By


class BH_Lead:
    click_bh_lead_xpath = "//*[@href='http://vendor.zoomvenues.info/admin/hub/leads']"
    cmd_resp_css = "textarea[placeholder='Place some text here']"
    submit_xpath = "//*[@class='btn btn-primary']"
    click_Edit_xpath = "(//*[@class='nav-icon fas fa-edit EditText'])[1]"


    def __init__(self,driver):
        self.driver = driver

    def click_BHLead(self):
        self.driver.find_element(By.XPATH, self.click_bh_lead_xpath).click()

    def click_Edit(self):
        self.driver.find_element(By.XPATH, self.click_Edit_xpath).click()


    def setCmdResp(self,cmdresp):
        self.driver.find_element(By.CSS_SELECTOR, self.cmd_resp_css).send_keys(cmdresp)
        self.driver.save_screenshot("C:\\Users\\GiTESH SONAR\\PycharmProjects\\ZoomVenues.Com\\ScreenShots" + "CmDResp.png")


    def setSubmit(self):
        self.driver.find_element(By.XPATH,self.submit_xpath).click()