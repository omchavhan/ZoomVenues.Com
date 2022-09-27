from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


class LeadsModul:
    leads_xpath = "(//*[@href='http://vendor.zoomvenues.info/admin/enquiries/leads'])[1]"
    edit_xpath = "(//*[@class='nav-icon fas fa-edit EditText'])[1]"
    status_xpath = "//*[@class='form-control' and @id='status']"
    submit_xpath = "//*[@class='btn btn-success']"
    venueName_xpath = "//*[@class='filter-option-inner-inner']"
    select_venueNm_link =" (20 June 4)20 June 4-venue1"

    def __init__(self,driver):
        self.driver = driver

    def click_leads(self):
        self.driver.find_element(By.XPATH,self.leads_xpath).click()

    def click_edit(self):
        self.driver.find_element(By.XPATH, self.edit_xpath).click()

    def select_Status(self):
        status = self.driver.find_element(By.XPATH,self.status_xpath)
        dropdown_status = Select(status)
        dropdown_status.select_by_index(2)

    def setSubmit(self):
        self.driver.find_element(By.XPATH, self.submit_xpath).click()

    def selectVenueNm(self):
        click_venue_name = self.driver.find_element(By.XPATH,"//select[@id='venues_id']")
        dropdown_venue_name = Select(click_venue_name)
        dropdown_venue_name.select_by_index(6)

    def Logout(self):
        self.driver.find_element(By.CSS_SELECTOR,".nav-link[data-toggle='dropdown']").click()
        self.driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(1) > nav:nth-child(1) > ul:nth-child(3) > div:nth-child(4) > a:nth-child(3) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(1)").click()




