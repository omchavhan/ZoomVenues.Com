import time
from pageObject.VendorModule.VendorLogin_Page import VendorPage
from pageObject.LiquorNdCorkage.CreateLiquorPakage_Module import LiquorPage
from pageObject.LiquorNdCorkage.EditLiquorPackage_Module import EditLiquorPackages
from utilites.customeLogger import LogGen
from utilites.readProperties import ReadConfig
from utilites.readProperties_liquerNcorkage import ReadConfig_liquor_corkage


class Test_EditliquorModul:
    base_URL = ReadConfig.getApplicationURL()
    userid = ReadConfig.getUserMail_V()
    password = ReadConfig.getPassword_V()
    liquor_name = ReadConfig_liquor_corkage.getLiquorName()
    hours = ReadConfig_liquor_corkage.getHours()
    price = ReadConfig_liquor_corkage.getPrice()
    detials = ReadConfig_liquor_corkage.getDetials()

    logger = LogGen.loggen()


    def test_Editliquor_modul(self,setup):
        self.logger.info("................ Liquor Page Test ...............")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.logger.info("................ Vendor SignIn ...............")
        self.vl = VendorPage(self.driver)
        self.vl.Click_signup(self.userid,self.password)
        self.lm = LiquorPage(self.driver)
        self.logger.info("................ Click Liquor List ...............")
        self.lm.click_Liquor_List()
        time.sleep(2)
        self.logger.info("................ Click Add New ...............")
        self.el = EditLiquorPackages(self.driver)
        self.el.click_edit()
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
        time.sleep(3)


        self.logger.info("................ Select Liquores Items..............")
        self.lm.select_liquor_type()
        time.sleep(2)
        self.lm.select_brand()
        time.sleep(2)
        self.lm.Enter_Details(self.detials)
        time.sleep(2)
        self.lm.click_Add_liquor()
        time.sleep(2)
        self.logger.info("................ Delete Item ...............")
        self.lm.click_delete()
        time.sleep(2)
        self.driver.quit()
        self.logger.info("................ Test End ...............")

