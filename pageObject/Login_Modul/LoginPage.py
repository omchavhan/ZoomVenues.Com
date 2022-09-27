from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    btn_signin_xpath = "//*[@id='main']/header/div[5]"
    textbox_userid_xapth = "//input[@id='login_email']"
    textbox_password_xapth = "//input[@id='login_password']"
    btn_login_xpath = "//button[@id='login-btn']"
    btn_logout_xpath = "//div[@class='show-reg-form avatar-img']"

    def __init__(self, driver):
        # self.driver = webdriver.Chrome(executable_path="C:\\Users\\GiTESH SONAR\\PycharmProjects\\nopcommerceApp\\chromedriver.exe")
        self.driver = driver


    def clickSignIn(self):
        signin = self.driver.find_element(By.XPATH,self.btn_signin_xpath)
        self.driver.execute_script("arguments[0].click();", signin)

    def setUserName(self,userid):
        self.driver.find_element(By.XPATH,self.textbox_userid_xapth).send_keys(userid)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xapth).send_keys(password)

    def setLogin(self):
        if self.btn_login_xpath == "//button[@id='login-btn']":
            self.driver.save_screenshot(
                "C:\\Users\\GiTESH SONAR\\PycharmProjects\\ZoomVenues.Com\\ScreenShots\\test_logins02.png")
        else:
            self.driver.find_element(By.XPATH, self.btn_login_xpath).click()




    def setLogOut(self):
        logout = self.driver.find_element(By.XPATH, self.btn_logout_xpath)
        self.driver.execute_script("arguments[0].click();", logout)







