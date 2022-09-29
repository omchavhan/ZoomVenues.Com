import time

from pageObject.VendorModule.VendorLogin_Page import VendorPage
from pageObject.LiquorNdCorkage.CreateLiquorPakage_Module import LiquorPage
from utilites.customeLogger import LogGen
from utilites.readProperties import ReadConfig
from utilites.readProperties_liquerNcorkage import ReadConfig_liquor_corkage


class Test_liquorModul:
    base_URL = ReadConfig.getApplicationURL()
    userid = ReadConfig.getUserMail_V()
    password = ReadConfig.getPassword_V()
    liquor_name = ReadConfig_liquor_corkage.getLiquorName()
    hours = ReadConfig_liquor_corkage.getHours()
    price = ReadConfig_liquor_corkage.getPrice()
    detials = ReadConfig_liquor_corkage.getDetials()

    logger = LogGen.loggen()

    def test_AdminTitle(self,setup):
        self.logger.info("***************** Test_start ******************")
        self.logger.info("**************Verify HomePage Title******************")
        self.driver = setup
        self.driver.get(self.base_URL)
        act_title = self.driver.title

        if act_title == "Zoomvenues | Dashboard ":
            self.driver.close()
            self.logger.info("************** Admin Dashboard Page title Test are Passed ******************")
            assert True
        else:
            self.logger.error("************** Admin Dashboard  Page title Test are Fail ******************")
            self.driver.save_screenshot("C:\\Users\\GiTESH SONAR\\PycharmProjects\\ZoomVenues.Com\\ScreenShots\\test_AdminpageTitle2.png")
            self.driver.close()
            assert False

    def test_liquor_modul(self,setup):
        self.logger.info("................ Liquor Page Test ...............")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.logger.info("................ Vendor SignIn ...............")
        self.vl = VendorPage(self.driver)
        self.vl.Click_signup(self.userid,self.password)
        self.lm = LiquorPage(self.driver)
        self.logger.info("................ Click Liquor List ...............")
        self.lm.click_Liquor_List()
        self.logger.info("................ Click Add New ...............")
        self.lm.click_Add()
        self.lm.enter_Liquor_PackageName(self.liquor_name)
        self.lm.enter_hours(self.hours)
        self.lm.package_price(self.price)
        self.lm.click_frequenly()
        self.lm.click_status()
        self.logger.info("................ Create Liquor Package ...............")
        self.lm.click_create_package()
        self.lm.click_Liquor_List()
        time.sleep(3)


        # self.logger.info("................ Select Liquores Items..............")
        # self.lm.select_liquor_type()
        # self.lm.select_brand()
        # self.lm.Enter_Details(self.detials)
        # self.lm.click_Add_liquor()
        # self.logger.info("................ Delete Item ...............")
        # self.lm.click_delete()
        # self.lm.select_liquor_type2()
        # self.lm.select_brand2()
        # self.lm.Enter_Details(self.detials)
        # self.lm.click_Add_liquor()
        # self.driver.quit()
        # self.logger.info("................ Test End ...............")

