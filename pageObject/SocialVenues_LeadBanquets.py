import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SocialVenues:
    socialVenues_Xpath = "//a[@href='#'][normalize-space()='Social Venues']"
    banquets_xpath = "(//a[contains(text(),'Banquets')])[1]"
    your_name_css = "div[id='venuemodalen2'] input[placeholder='Your Name *']"
    mail_id_css = "div[id='venuemodalen2'] input[placeholder='Email Address*']"
    phone_no_css = "div[id='venuemodalen2'] input[placeholder='Phone Number *']"
    select_event_type_css = "div[id='venuemodalen2'] select[name='eventtype']"
    select_date_css = "body > div:nth-child(3) > div:nth-child(13) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > fieldset:nth-child(2) > div:nth-child(6) > input:nth-child(2)"
    time_css = "input[class='timepicker1']"
    no_of_people_css = "div[id='venuemodalen2'] input[placeholder='No of Peoples *']"
    select_budget_css = "div[id='venuemodalen2'] select[class='budget']"
    add_req_css = "div[id='venuemodalen2'] textarea[placeholder='Additional Requirement:']"
    acc_term_condition_css = "body > div:nth-child(3) > div:nth-child(13) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(3) > label:nth-child(1) > input:nth-child(1)"
    submit_css = "body > div:nth-child(3) > div:nth-child(13) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(4) > button:nth-child(1)"
    close_scr_css = "div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']"
    click_zoomvenusLogo_xpath = "//img[@src='http://zoomvenues.info/images/logo.png']"
    close_popup_xpath = "(//*[@class='fal fa-times'])[16]"


    def __init__(self,driver):
        self.driver = driver


    def select_venue(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        social_venues = self.driver.find_element(By.XPATH,self.socialVenues_Xpath)
        action = ActionChains(self.driver)
        action.move_to_element(social_venues).perform()
        banquets_c = self.driver.find_element(By.XPATH,self.banquets_xpath)
        self.driver.execute_script("arguments[0].click();", banquets_c)

    def setName(self,name):
        your_name = self.driver.find_element(By.CSS_SELECTOR,self.your_name_css)
        your_name.send_keys(name)

    def setMail(self,mail):
        mail_id = self.driver.find_element(By.CSS_SELECTOR,self.mail_id_css)
        mail_id.send_keys(mail)

    def setPhoneNo(self,phone):
        phone_no = self.driver.find_element(By.CSS_SELECTOR,self.phone_no_css)
        phone_no.send_keys(phone)

    def setEventType(self):
        select_type = self.driver.find_element(By.CSS_SELECTOR,self.select_event_type_css)
        dropdown = Select(select_type)
        dropdown.select_by_index(1)

    def setDate(self,date_c):
        date = self.driver.find_element(By.CSS_SELECTOR,self.select_date_css)
        date.send_keys(date_c)

    def setTime(self,time_c):
        time = self.driver.find_element(By.CSS_SELECTOR,self.time_css)
        time.send_keys(time_c)

    def setNoPeople(self):
        no_of_people = self.driver.find_element(By.CSS_SELECTOR,self.no_of_people_css)
        no_of_people.send_keys(5)

    def setBudget(self):
        select_budget = self.driver.find_element(By.CSS_SELECTOR,self.select_budget_css)
        dropdown_budget = Select(select_budget)
        dropdown_budget.select_by_value("80 to 150")

    def setReq(self):
        add_req = self.driver.find_element(By.CSS_SELECTOR,self.add_req_css)
        add_req.send_keys("nothing________")

    def setTermCondtion(self):
        acc_term_condition = self.driver.find_element(By.CSS_SELECTOR,self.acc_term_condition_css)
        acc_term_condition.click()

    def clickSubmit(self):
        submit = self.driver.find_element(By.CSS_SELECTOR,self.submit_css).click()

    def closePopup(self):
        self.driver.find_element(By.XPATH, self.close_popup_xpath).click()





