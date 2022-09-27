import time

from pageObject.Login_Modul.LoginPage import LoginPage
from utilites.readProperties import ReadConfig
from utilites.customeLogger import LogGen


class Test_001_login:

    base_URL = ReadConfig.getApplicationURL()
    userid = ReadConfig.getUserMail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    # @pytest.mark.regression
    # @pytest.mark.sanity
    def test_homePageTitle(self,setup):
        self.logger.info("*****************Test_001_login******************")
        self.logger.info("**************Verify HomePage Title******************")
        self.driver = setup
        self.driver.get(self.base_URL)
        act_title = self.driver.title

        if act_title == "Best venues in Dubai - zoomvenues.info":
            self.logger.info("**************Home Page title Test are Passed******************")
            self.driver.close()
            assert True

        else:
            self.logger.error("**************Home Page title Test are Fail******************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            self.driver.close()
            assert False

    # @pytest.mark.sanity
    def test_loginPage(self,setup):
        self.logger.info("**************Verifing LogIn Test******************")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lp = LoginPage(self.driver)
        self.lp.clickSignIn()
        self.lp.setUserName(self.userid)
        self.lp.setPassword(self.password)
        self.lp.setLogin()

        time.sleep(3)
        act_title = self.driver.title

        if act_title == "zoomvenues.info":

            self.logger.info("**************LogIn Test Passed******************")
            self.driver.close()
            assert True
        else:
            # self.driver.close()
            self.logger.error("**************LogIn Test Login Link Failed******************")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_logins1.png")
            self.driver.close()
            assert False

