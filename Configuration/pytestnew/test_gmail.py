import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Below all Xpoth:
driver = webdriver.Firefox(executable_path="/geckodriver.exe")
Email_loc = "//input[@type='email']"
Next_button_loc = "//span[normalize-space()='Next']"

def Enter_Email_id():
    email_id = driver.find_element_by_xpath(Email_loc)
    email_id.send_keys("omworld01@gmail.com")

def Next_button_click():
    next_button = driver.find_element_by_xpath(Next_button_loc)
    next_button.click()


def test_gmail():
    BASE_URL = driver.get("https://accounts.google.com/")
    Enter_Email_id()
    time.sleep(3)
    Next_button_click()
    time.sleep(3)
