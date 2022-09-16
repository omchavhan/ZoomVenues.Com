import time

from pageObject.VendorLogin_Page import VendorPage
import pytest
from utilites.readProperties import ReadConfig
from utilites.customeLogger import LogGen



class Test_003_VendorLogin:
    base_URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserMail_V()
    password = ReadConfig.getPassword_V()

    logger = LogGen.loggen()

    def test_vendor_login_title(self,setup):
        self.logger.info("................ Test_003 vendor Login Start...............")
        self.logger.info("................ vendor Page Login Title ...............")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lp = VendorPage(self.driver)
        vendor_title = self.driver.title

        if vendor_title =="Best venues in Dubai - zoomvenues.info":
            self.logger.info("................ vendor Page Login Title Pass ...............")
            assert True
            self.driver.close()
        else:
            self.logger.info("................ vendor Page Login Title Fail ...............")
            self.driver.save_screenshot("C:\\Users\\GiTESH SONAR\\PycharmProjects\\GoogleAuto\\ScreenShots\\" + "vendor_homepageTitle.png")
            self.driver.close()
            assert False


    @pytest.mark.sanity
    def test_admin_login(self,setup):
        self.logger.info("................ Admin Page Login Test ...............")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lp = VendorPage(self.driver)
        self.lp.Click_signup(self.username,self.password)
        time.sleep(2)


        vendor_title = self.driver.title
        if vendor_title == "Zoomvenues | Dashboard":
            self.logger.info("................ Admin Page Login TestPass ...............")
            assert True
            self.driver.quit()
        else:
            self.logger.info("................ Admin Page Login Test Fail ...............")
            self.driver.save_screenshot("C:\\Users\\GiTESH SONAR\\PycharmProjects\\GoogleAuto\\ScreenShots\\" + "vendor_login_Title.png")
            self.driver.quit()
            assert False
