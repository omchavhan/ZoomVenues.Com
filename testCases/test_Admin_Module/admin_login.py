import time

from pageObject.Admin_Modul.AdminLogin import AdminPage
import pytest
from utilites.readProperties import ReadConfig
from utilites.customeLogger import LogGen


class Test_003_adminLogin:
    base_URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserMail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_admin_login_title(self,setup):
        self.logger.info("................ Test_003 adminLogin Start...............")
        self.logger.info("................ Admin Page Login Title ...............")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lp = AdminPage(self.driver)
        admin_title = self.driver.title

        if admin_title =="Best venues in Dubai - zoomvenues.info":
            self.logger.info("................ Admin Page Login Title Pass ...............")
            assert True
            self.driver.close()
        else:
            self.logger.info("................ Admin Page Login Title Fail ...............")
            self.driver.save_screenshot("C:\\Users\\GiTESH SONAR\\PycharmProjects\\GoogleAuto\\ScreenShots\\" + "admin_homepageTitle.png")
            self.driver.close()
            assert False


    @pytest.mark.sanity
    def test_admin_login(self,setup):
        self.logger.info("................ Admin Page Login Test ...............")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lp = AdminPage(self.driver)
        self.lp.Click_venues_signup(self.username,self.password)
        time.sleep(2)

        admin_title = self.driver.title
        if admin_title == "Zoomvenues | Dashboard":
            self.logger.info("................ Admin Page Login TestPass ...............")
            assert True
            # self.driver.close()
        else:
            self.logger.info("................ Admin Page Login Test Fail ...............")
            self.driver.save_screenshot("C:\\Users\\GiTESH SONAR\\PycharmProjects\\GoogleAuto\\ScreenShots\\" + "admin_login_Title.png")
            # self.driver.quit()
            assert False
