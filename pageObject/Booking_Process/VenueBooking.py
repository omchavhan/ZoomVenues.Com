from selenium import webdriver



import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class VenuesBooking:
    select_enqury_xpath = "(//*[@title='Make An Enquiry'])[1]"
    # select_enqury_xpath = "a[onclick="enquireVenueList('591','PyTest - 1','653')"][title='Make An Enquiry"]"
    close_popup_css = "div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']"
    name_css = "div[class='col-md-6 col-xs-12 rightspace'] input[placeholder='Your Name *']"
    mail_css = "div[class='col-md-6 col-xs-12 leftspace'] input[placeholder='Email Address*']"
    date_xpath = "//input[@id='datepicker']"
    phoneno_css = "div[class='iti iti--allow-dropdown iti--separate-dial-code'] input[placeholder='Phone Number *']"
    eventType_css = "form[id='enquiry-form'] select[name='eventtype']"
    time_css = "form[id='enquiry-form'] input[placeholder='Time']"
    noOfpeople_css = "div[class='col-md-6 col-xs-12 rightspace'] input[placeholder='No of Peoples *']"
    selectbugust_xpath = "//form[@id='enquiry-form']//select[@class='budget']"
    add_req_css = "form[id='enquiry-form'] textarea[placeholder='Additional Requirement:']"
    acc_term_css = "body > div:nth-child(3) > div:nth-child(9) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(3) > label:nth-child(1) > input:nth-child(1)"
    submit_xpath = "(//*[@class='btn color2-bg url_btn float-btn btnSubmitEnquiry'])[2]"

    def __init__(self,driver):
        self.driver = driver

    def setEnquiry(self):
        self.driver.find_element(By.XPATH,self.select_enqury_xpath).click()
        time.sleep(2)

    def closePopup(self):
        close_popup = self.driver.find_element(By.CSS_SELECTOR, self.close_popup_css)
        self.driver.execute_script("arguments[0].click();", close_popup)

    def setName(self,name):
        self.driver.find_element(By.CSS_SELECTOR,self.name_css).send_keys(name)

    def setMail(self,mail):
        self.driver.find_element(By.CSS_SELECTOR,self.mail_css).send_keys(mail)

    def setPhoneNo(self,phono_no):
        self.driver.find_element(By.CSS_SELECTOR,self.phoneno_css).send_keys(phono_no)

    def setEventType(self):
        select_type = self.driver.find_element(By.CSS_SELECTOR,self.eventType_css)
        dropdown = Select(select_type)
        dropdown.select_by_index(1)

    def setDate(self,date):
        self.driver.find_element(By.XPATH,self.date_xpath).send_keys(date)

    def setTime(self,time):
        self.driver.find_element(By.CSS_SELECTOR, self.time_css).send_keys(time)

    def setnoOfpeople(self,noOfpeople):
        self.driver.find_element(By.CSS_SELECTOR, self.noOfpeople_css).send_keys(noOfpeople)

    def setbuget(self):
        select_type = self.driver.find_element(By.XPATH, self.selectbugust_xpath)
        dropdown = Select(select_type)
        dropdown.select_by_index(1)

    def setaddReq(self):
        self.driver.find_element(By.CSS_SELECTOR, self.add_req_css).send_keys("nothing.........s")

    def setacc_term(self):
        self.driver.find_element(By.CSS_SELECTOR, self.acc_term_css).click()


    def setSubmit(self):
        self.driver.find_element(By.XPATH, self.submit_xpath).click()


















