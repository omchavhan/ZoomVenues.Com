from pageObject.VendorModule.VendorLogin_Page import VendorPage
from pageObject.LiquorNdCorkage.Create_CorkagePakage import CokargePage
from pageObject.LiquorNdCorkage.EditCorkagePackage import cokarge_list_page
from pageObject.LiquorNdCorkage.Corkage_SelectItems import Cokarge_SelectItems
from utilites.customeLogger import LogGen
from utilites.readProperties import ReadConfig
from utilites.readProperties_liquerNcorkage import ReadConfig_liquor_corkage


class test_Cokarge_List:
    base_URL = ReadConfig.getApplicationURL()
    userid = ReadConfig.getUserMail_V()
    password = ReadConfig.getPassword_V()
    cokarge_name = ReadConfig_liquor_corkage.getCokarage_Name()
    price = ReadConfig_liquor_corkage.getPrice_cokarage()
    remark = ReadConfig_liquor_corkage.getCokarage_remark()
    Qty = ReadConfig_liquor_corkage.getCokarage_Qty()


    logger = LogGen.loggen()


    def cokarge_list(self,setup):
        self.logger.info("................ Cokarge Page Test ...............")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.logger.info("................ Vendor SignIn ...............")
        self.vl = VendorPage(self.driver)
        self.vl.Click_signup(self.userid,self.password)
        self.logger.info("................ Click Corkage List...............")
        self.cm = CokargePage(self.driver)
        self.cm.click_Cokarge_List()
        self.logger.info("................ Click Edit and Edit Start ...............")
        self.cl = cokarge_list_page(self.driver)
        self.cl.click_edit()
        self.cm.enter_Cokarge_PackageName(self.cokarge_name)
        self.cm.package_cokarge_price(self.price)
        self.cm.click_remark(self.remark)
        self.cm.click_frequenly()
        self.cm.click_status()
        self.cm.click_create_package()
        self.logger.info("................ Select Cokarage..............")
        self.cs = Cokarge_SelectItems(self.driver)
        self.cs.select_type()  # loop use
        self.cs.select_Qunity(self.Qty)
        self.cs.select_unit()
        self.cs.enter_price(self.price)
        self.cs.click_Add_cokarge()
        self.logger.info("................ Delete Item ...............")
        self.cs.click_delete()
        self.logger.info("................ Test End ...............")

