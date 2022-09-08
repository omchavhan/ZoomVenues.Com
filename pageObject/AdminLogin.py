from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AdminPage:
    venues_signup_xpath = "(//*[@href='http://vendor.zoomvenues.info'])[1]"
    close_venues_create_popup_xpath = "//a[normalize-space()='Close']"
    mail_id_css = "#user"
    password_css = "#password"
    login_css = "#form-submit"
    logout_xpath = "(//*[@class='dropdown-item-title'])[2]"
    profile_xpath = "//*[@class='far fa-user']"


    def __init__(self,driver):
        self.driver = driver

    def Click_venues_signup(self,userid,password1):
        self.driver.implicitly_wait(20)
        parent_page = self.driver.current_window_handle
        admin_signup = self.driver.find_element(By.XPATH,self.venues_signup_xpath).click()
        child_page = self.driver.window_handles
        for handle in child_page:
            if handle != parent_page:
                self.driver.switch_to.window(handle)
                close_screen = self.driver.find_element(By.XPATH,self.close_venues_create_popup_xpath).click()
                mail_id = self.driver.find_element(By.CSS_SELECTOR,self.mail_id_css)
                mail_id.send_keys(userid)
                time.sleep(2)
                password = self.driver.find_element(By.CSS_SELECTOR,self.password_css)
                password.send_keys(password1)
                time.sleep(2)
                login = self.driver.find_element(By.CSS_SELECTOR,self.login_css).click()

    def Profile(self):
        self.driver.find_element(By.XPATH, self.profile_xpath).click()

    def LogOut(self):
       logout =  self.driver.find_element(By.XPATH, self.logout_xpath)
       self.driver.execute_script("arguments[0].click();",logout )

    def Close_vendor_poup(self):
        close_screen = self.driver.find_element(By.XPATH, self.close_venues_create_popup_xpath).click()

    def MailId(self,userid):
        mail_id = self.driver.find_element(By.CSS_SELECTOR, self.mail_id_css)
        mail_id.send_keys(userid)

    def Password(self,passwordd):
        password = self.driver.find_element(By.CSS_SELECTOR, self.password_css)
        password.send_keys(passwordd)

    def LogIn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_css).click()







