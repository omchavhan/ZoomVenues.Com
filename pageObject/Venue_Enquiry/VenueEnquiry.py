from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class venue_enquiry:

    # Bellow Element Path -----------
    SocialVenues_linktext = "Social Venues"
    Banquets_xpath = "//*[@href='https://zoomvenues.info/event-venue/banquets']"
    close_MakeEnquiry_xpath = "(//*[@class='fal fa-times'])[13]"
    Click_Pytest3_Venue_linktext = "PyTest - 3"

    def __init__(self,driver):
        self.driver = driver

    def click_social_venues(self):
        socialvenues = self.driver.find_elements(By.LINK_TEXT,self.Click_Pytest3_Venue_linktext)
        for x in socialvenues:
            print(x.text)
            if (x.text[3] == 'Social Venues'):
                x.click()
                break

        Action = ActionChains(self.driver)
        Action.move_to_element(socialvenues).perform()
        Banquets = self.driver.find_element(By.XPATH,self.Banquets_xpath).click()
        close_MakeEnquiry = self.driver.find_element(By.XPATH,self.close_MakeEnquiry_xpath).click()

    def Click_Venue(self):
        venue_name = self.driver.find_elements(By.LINK_TEXT,self.Click_Pytest3_Venue_linktext)
        for x in venue_name:
            print(x.text)
            if (x.text[3] == 'PyTest - 3'):
                x.click()
                break

