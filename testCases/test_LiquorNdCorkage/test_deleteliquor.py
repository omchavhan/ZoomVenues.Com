import time

from pageObject.VendorModule.VendorLogin_Page import VendorPage
from pageObject.LiquorNdCorkage.CreateLiquorPakage_Module import LiquorPage
from pageObject.LiquorNdCorkage.DeleteLiquor import DeleteLiquor
from utilites.customeLogger import LogGen
from utilites.readProperties import ReadConfig
from utilites.readProperties_liquerNcorkage import ReadConfig_liquor_corkage


class Test_deleteliquor:
    base_URL = ReadConfig.getApplicationURL()
    userid = ReadConfig.getUserMail_V()
    password = ReadConfig.getPassword_V()
    liquor_name = ReadConfig_liquor_corkage.getLiquorName()
    hours = ReadConfig_liquor_corkage.getHours()
    price = ReadConfig_liquor_corkage.getPrice()
    detials = ReadConfig_liquor_corkage.getDetials()

    logger = LogGen.loggen()


    def test_deleteliquor(self,setup):
        self.logger.info("................ Liquor Page Test ...............")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.logger.info("................ Vendor SignIn ...............")
        self.vl = VendorPage(self.driver)
        self.vl.Click_signup(self.userid,self.password)
        self.lm = LiquorPage(self.driver)
        self.logger.info("................ Click Liquor List ...............")
        self.lm.click_Liquor_List()
        self.ld = DeleteLiquor(self.driver)
        self.ld.click_Edit_list()
        self.logger.info("................ Click Delete ...............")
        for delete in range(0,3):
            self.ld.click_Liquor_Delete()
        self.driver.quit()





