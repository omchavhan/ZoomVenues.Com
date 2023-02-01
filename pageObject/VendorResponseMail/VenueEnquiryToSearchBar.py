from selenium import  webdriver
from selenium.webdriver.common.by import By



class VenuesEnquiry:
    # Elements Path --
    click_CorporateVenues_css = "a[href='#tab-inpt2']"
    click_Loc_css = "body > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)"
    select_loc_xpath = "(//*[@data-value='AJ'])[2]"
    click_venue_css = "body > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > div:nth-child(3) > div:nth-child(2) > span:nth-child(1)"
    select_venues_xpath = "//*[@data-value='conference-rooms']"
    click_Event_xpath = "(//span[@class='current'][normalize-space()='All Event Categories'])[2]"
    select_Event_xpath = "//*[@data-value='conferences']"
    select_search_css = "div[id='tab-inpt2'] button[class='main-search-button color2-bg']"
    close_popup_css = "div[id='venuemodalen2'] div[class='close-reg'] i[class='fal fa-times']"
    select_enquiry_xpath = "//a[normalize-space()='Enquire']"


    def __init__(self,driver):
        self.driver = driver

    def click_CorporateVenues(self):
        self.driver.find_element(By.CSS_SELECTOR,self.click_CorporateVenues_css).click()

    def select_loction(self):
        self.driver.find_element(By.CSS_SELECTOR,self.click_Loc_css).click()
        self.driver.find_element(By.XPATH, self.select_loc_xpath).click()


    def select_venues(self):
        self.driver.find_element(By.CSS_SELECTOR,self.click_venue_css).click()
        self.driver.find_element(By.XPATH, self.select_venues_xpath).click()


    def select_event(self):
        self.driver.find_element(By.XPATHR,self.click_Event_xpath).click()
        self.driver.find_element(By.XPATH, self.select_Event_xpath).click()

    def select_submit(self):
        self.driver.find_element(By.CSS_SELECTOR,self.select_search_css).click()


    def select_close_popup(self):
        self.driver.find_element(By.CSS_SELECTOR,self.close_popup_css).click()

    def select_enquiry(self):
        self.driver.find_element(By.XPATH,self.select_enquiry_xpath).click()







