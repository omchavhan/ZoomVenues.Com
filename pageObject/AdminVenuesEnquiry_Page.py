from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AVenuesEnquiry:
    click_VenuesEnquiry_xpath = "//*[@href='http://vendor.zoomvenues.info/admin/enquiries/venues']"
    click_NewResponse_xpath = "(//*[@class='nav-icon fas fa-edit EditText'])[1]"
    status_css = "#zv_bh_enq_status"
    submit_xpath = "//*[@class='btn btn-primary mr-2']"
    sitting_xpath = "//*[@class='form-check-input arrangements custom-control-input']"
    finalOffer_xpath = "(//div[@aria-label='Rich Text Editor, main'])[1]"
    termCond_xpath = "(//div[@aria-label='Rich Text Editor, main'])[2]"
    cmdForBH_xpath = "(//div[@aria-label='Rich Text Editor, main'])[3]"

    def __init__(self,driver):
        self.driver = driver

    def ClickVenuesEnquiry(self):
        clickVE = self.driver.find_element(By.XPATH,self.click_VenuesEnquiry_xpath).click()
        # clickVE.self.driver.save_screenshot("C:\\Users\\GiTESH SONAR\\PycharmProjects\\GoogleAuto\\ScreenShots\\" + "clickVE.png")
        # clickVE.click()

    def ClickNewResp(self):
        # self.driver.find_element(By.XPATH,self.click_NewResponse_xpath)
        # self.driver.save_screenshot("C:\\Users\\GiTESH SONAR\\PycharmProjects\\GoogleAuto\\ScreenShots\\" + "newresp.png")
        self.driver.find_element(By.XPATH, self.click_NewResponse_xpath).click()

    def selectSettingArrg(self):
        self.driver.find_element(By.XPATH, self.sitting_xpath).click()

    def setFinaloffer(self,finalOffer):
        self.driver.find_element(By.XPATH, self.finalOffer_xpath).send_keys(finalOffer)

    def setTermCondtion(self,termCondition):
        self.driver.find_element(By.XPATH, self.termCond_xpath).send_keys(termCondition)

    def setCmdBH(self,cmdBH):
        self.driver.find_element(By.XPATH, self.cmdForBH_xpath).send_keys(cmdBH)

    def setStatus(self):
        status = self.driver.find_element(By.CSS_SELECTOR,self.status_css)
        dropdown_Status = Select(status)
        dropdown_Status.select_by_index(4)

    def setSubmit(self):
        self.driver.find_element(By.XPATH,self.submit_xpath).click()

