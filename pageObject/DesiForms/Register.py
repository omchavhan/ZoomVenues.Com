from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



class LogIn:
    # Bellow Web Elements Path
    location_select_xpath = "//td[normalize-space()='Pune']"
    click_signin_xpath = "//a[normalize-space()='Sign In']"
    enter_mobile_no_css = "#form-username"
    click_login_xpath = "//button[normalize-space()='Login']"
    enter_otp_css = "input[placeholder='OTP']"
    click_verify_otp_xpath = "//button[normalize-space()='VERIFY OTP']"
    enter_your_name_xpath = "//input[@placeholder='Your Name *']"
    select_gender_xpath = "//select[@formcontrolname='Gender']"
    select_find_us_xpath = "//select[@formcontrolname='Source']"
    enter_area_xpath = "//input[@placeholder='Select Area *']"
    enter_subarea_xpath = "//input[@placeholder='Sub Area (Optional)']"
    click_register_xpath = "//button[normalize-space()='REGISTER']"



    def __init__(self,driver):
        self.driver = driver


    def loction_select(self):
        self.driver.find_element(By.XPATH,self.location_select_xpath).click()

    def click_signIn(self):
        self.driver.find_element(By.XPATH, self.click_signin_xpath).click()

    def enter_mobile_no(self,mobile_no):
        self.driver.find_element(By.CSS_SELECTOR, self.enter_mobile_no_css).send_keys(mobile_no)

    def click_logIn(self):
        self.driver.find_element(By.XPATH, self.click_login_xpath).click()

    def enter_otp(self,otp_no):
        self.driver.find_element(By.CSS_SELECTOR, self.enter_otp_css).send_keys(otp_no)

    def click_otp_verification(self):
        self.driver.find_element(By.XPATH, self.click_verify_otp_xpath).click()


    def enter_your_name(self,your_name):
        self.driver.find_element(By.XPATH, self.enter_your_name_xpath).send_keys(your_name)

    def select_gender(self):
        s_gender = self.driver.find_element(By.XPATH, self.select_gender_xpath)
        dropdown_gender = Select(s_gender)
        dropdown_gender.select_by_index(1)

    def select_find_us(self):
        find_us = self.driver.find_element(By.XPATH, self.select_find_us_xpath)
        dropdown_find_us = Select(find_us)
        dropdown_find_us.select_by_index(4)

    def select_area(self,area):
        self.driver.find_element(By.XPATH, self.enter_area_xpath).send_keys(area)


    def select_SuBarea(self,subarea):
        self.driver.find_element(By.XPATH, self.enter_subarea_xpath).send_keys(subarea)


    def click_register(self):
        self.driver.find_element(By.XPATH, self.click_register_xpath).click()










