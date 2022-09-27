import time

from pageObject.VendorModule.VendorLogin_Page import VendorPage
from pageObject.LiquorNdCorkage.CreateLiquorPakage_Module import LiquorPage
from pageObject.LiquorNdCorkage.SelectLiquorDetail import SelectLiquorDetail
from pageObject.LiquorNdCorkage.EditLiquorPackage_Module import EditLiquorPackages
from utilites.customeLogger import LogGen
from utilites.readProperties import ReadConfig
from utilites.readProperties_liquerNcorkage import ReadConfig_liquor_corkage


class Test_SelectliquorDetail:
    base_URL = ReadConfig.getApplicationURL()
    userid = ReadConfig.getUserMail_V()
    password = ReadConfig.getPassword_V()
    liquor_name = ReadConfig_liquor_corkage.getLiquorName()
    hours = ReadConfig_liquor_corkage.getHours()
    price = ReadConfig_liquor_corkage.getPrice()
    detials = ReadConfig_liquor_corkage.getDetials()

    logger = LogGen.loggen()


    def test_SelectliquorDetail(self,setup):
        self.logger.info("................ Liquor Page Test ...............")
        self.driver = setup
        self.driver.get(self.base_URL)
        act_title = self.driver.title
        if act_title == "🧨 Trying to get property 'data' of non-object":
            self.driver.refresh()

        else:
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
            for select in range(0,3):
                self.sl.select_liquor_type()
                time.sleep(2)
                self.sl.select_brand()
                time.sleep(2)
                self.sl.Enter_Details(self.detials)
                self.sl.click_Add_liquor()
                time.sleep(2)
            self.driver.quit()
            self.logger.info("................ Test End ...............")


