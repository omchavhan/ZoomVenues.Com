from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class VVenuesEnquiry:
    click_VenuesEnquiry_xpath = "//*[@href='http://vendor.zoomvenues.info/admin/enquiries/venues']"
    click_NewResponse_xpath = "(//*[@class='nav-icon fas fa-edit EditText'])[1]"
    status_css = "#zv_bh_enq_status"
    submit_xpath = "//*[@class='btn btn-primary mr-2']"

    def __init__(self,driver):
        self.driver = driver

    def ClickVenuesEnquiry(self):
        clickVE = self.driver.find_element(By.XPATH,self.click_VenuesEnquiry_xpath).click()
        # clickVE.self.driver.save_screenshot("C:\\Users\\GiTESH SONAR\\PycharmProjects\\GoogleAuto\\ScreenShots\\" + "clickVE.png")
        # clickVE.click()

    def ClickNewResp(self):
        self.driver.find_element(By.XPATH,self.click_NewResponse_xpath)
        self.driver.save_screenshot("C:\\Users\\GiTESH SONAR\\PycharmProjects\\GoogleAuto\\ScreenShots\\" + "newresp.png")
        self.driver.find_element(By.XPATH, self.click_NewResponse_xpath).click()

    def setSubmit(self):
        self.driver.find_element(By.XPATH,self.submit_xpath).click()

