import time

from pageObject.VendorModule.VendorLogin_Page import VendorPage
from pageObject.LiquorNdCorkage.CreateLiquorPakage_Module import LiquorPage
from pageObject.LiquorNdCorkage.SelectLiquorDetail import SelectLiquorDetail
from pageObject.LiquorNdCorkage.EditLiquorPackage_Module import EditLiquorPackages
from pageObject.LiquorNdCorkage.DeleteLiquor import DeleteLiquor
from utilites.customeLogger import LogGen
from utilites.readProperties import ReadConfig
from utilites.readProperties_liquerNcorkage import ReadConfig_liquor_corkage


class Test_LiquorFlow:
    base_URL = ReadConfig.getApplicationURL()
    userid = ReadConfig.getUserMail_V()
    password = ReadConfig.getPassword_V()
    #Select Liquor Detials ---
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
            self.driver.save_screenshot("C:\\Users\\GiTESH SONAR\\PycharmProjects\\ZoomVenues.Com\\ScreenShots\\test_AdminpageTitle-29-09.png")
            self.driver.close()
            assert False


    def test_CreateLiquorPackage(self,setup):
        self.logger.info("................ Liquor Page Test ...............")
        self.driver = setup
        act_title = self.driver.title

        if act_title == "🧨 Trying to get property 'data' of non-object" or act_title != "🧨 Trying to get property 'data' of non-object":
            self.driver.refresh()
            time.sleep(2)
            self.driver.get(self.base_URL)
            self.logger.info("................ Vendor SignIn ...............")
            self.vl = VendorPage(self.driver)
            self.vl.Click_signup(self.userid, self.password)
            self.lm = LiquorPage(self.driver)
            self.logger.info("................ Click Liquor List ...............")
            self.lm.click_Liquor_List()
            time.sleep(2)
            self.logger.info("................ Click Add New ...............")
            self.lm.click_Add()
            time.sleep(2)
            self.lm.enter_Liquor_PackageName(self.liquor_name)
            time.sleep(2)
            self.lm.enter_hours(self.hours)
            time.sleep(2)
            self.lm.package_price(self.price)
            time.sleep(2)
            self.lm.click_frequenly()
            time.sleep(2)
            self.lm.click_status()
            time.sleep(2)
            self.logger.info("................ Create Liquor Package ...............")
            self.lm.click_create_package()
            time.sleep(2)
            self.lm.click_Liquor_List()
            time.sleep(2)
            self.driver.quit()
            self.logger.info("................ End Create Liquor Package Test ...............")



    def test_SelectliquorDetail(self,setup):
        self.logger.info("................ Liquor Page Test ...............")
        self.driver = setup
        self.driver.get(self.base_URL)
        act_title = self.driver.title
        if act_title == "🧨 Trying to get property 'data' of non-object":
            self.driver.refresh()
            self.logger.info("................ Vendor SignIn ...............")
            self.vl = VendorPage(self.driver)
            self.vl.Click_signup(self.userid, self.password)
            self.lm = LiquorPage(self.driver)
            self.logger.info("................ Click Liquor List ...............")
            self.lm.click_Liquor_List()
            time.sleep(2)
            self.ld = EditLiquorPackages(self.driver)
            self.ld.click_edit()
            time.sleep(2)
            self.logger.info("................ Select Liquores Items..............")
            self.sl = SelectLiquorDetail(self.driver)
            for select in range(0, 3):
                self.sl.select_liquor_type()
                time.sleep(2)
                self.sl.select_brand()
                time.sleep(2)
                self.sl.Enter_Details(self.detials)
                self.sl.click_Add_liquor()
                time.sleep(2)
            self.driver.quit()
            self.logger.info("................ End Select LIquor Test ...............")


    def test_deleteliquor(self,setup):
        self.logger.info("................ Liquor Page Test ...............")
        self.driver = setup
        act_title = self.driver.title

        if act_title == "🧨 Trying to get property 'data' of non-object" or act_title != "🧨 Trying to get property 'data' of non-object":
            self.driver.refresh()
            self.driver.get(self.base_URL)
            self.logger.info("................ Vendor SignIn ...............")
            self.vl = VendorPage(self.driver)
            self.vl.Click_signup(self.userid, self.password)
            self.lm = LiquorPage(self.driver)
            self.logger.info("................ Click Liquor List ...............")
            self.lm.click_Liquor_List()
            self.ld = DeleteLiquor(self.driver)
            self.ld.click_Edit_list()
            self.logger.info("................ Click Delete ...............")
            for delete in range(0, 3):
                self.ld.click_Liquor_Delete()
            self.driver.quit()
            self.logger.info("................ End Delete LIquor Test ...............")

