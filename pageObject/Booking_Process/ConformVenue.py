from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ConformVenuesEnq:
    click_edit_action_xapth = "(//*[@class='nav-icon fas fa-edit EditText'])[1]"
    select_menu_xpath = "//div[@class='overSelect']"
    select_aaregment_xpath = "(//*[@class='form-check-input arrangements custom-control-input'])[4]"
    enter_finaloffer_css= "body > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(2) > div:nth-child(2) > div:nth-child(9) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1)"
    enter_termcondition_css = "body > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(2) > div:nth-child(2) > div:nth-child(9) > div:nth-child(3) > div:nth-child(1) > div:nth-child(4) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1)"
    enter_bhOfferPrice_xapth = "//*[@class='form-control offerPrice text-left']"
    enter_zv2markupcom_xpath = "//*[@class='form-control  marked text-left']"
    select_status_xpath = "//*[@id='zv_bh_enq_status']"
    click_save_xpath = "//*[@class='btn btn-primary mr-2']"
    click_venuesenquiry_xpath = "(//*[@href='http://vendor.zoomvenues.info/admin/enquiries/venues'])[1]"


    def __init__(self,driver):
        self.driver = driver


    def click_venuesenquiry(self):
        self.driver.find_element(By.XPATH,self.click_venuesenquiry_xpath).click()


    def click_edit_a(self):
        self.driver.find_element(By.XPATH,self.click_edit_action_xapth).click()


    def select_menu(self):
        self.driver.find_element(By.XPATH,self.select_menu_xpath).click()

    def select_arrgment(self):
        self.driver.find_element(By.XPATH,self.select_aaregment_xpath).click()

    def enter_finaloffer(self,final):
        self.driver.find_element(By.CSS_SELECTOR,self.enter_finaloffer_css).send_keys(final)

    def enter_termcodition(self,termcond):
        self.driver.find_element(By.CSS_SELECTOR,self.enter_termcondition_css).send_keys(termcond)

    def enter_bhofferprice(self,bhoffer):
        self.driver.find_element(By.XPATH,self.enter_bhOfferPrice_xapth).send_keys(bhoffer)

    def enter_zv2markupcom(self,zv2markup):
        self.driver.find_element(By.XPATH,self.enter_zv2markupcom_xpath).send_keys(zv2markup)

    def select_status(self):
        status = self.driver.find_element(By.XPATH,self.select_status_xpath)
        dropdown_status = Select(status)
        dropdown_status.select_by_index(4)


    def click_save(self):
        self.driver.find_element(By.XPATH, self.click_save_xpath).click()
