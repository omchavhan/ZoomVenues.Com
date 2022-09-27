import time

from pageObject.VendorModule.VendorLogin_Page import VendorPage
from pageObject.LiquorNdCorkage.Create_CorkagePakage import CreateCokargePage
from pageObject.LiquorNdCorkage.Corkage_SelectItems import Cokarge_SelectItems
from pageObject.LiquorNdCorkage.EditCorkagePackage import Edit_cokarge_list_page
from utilites.customeLogger import LogGen
from utilites.readProperties import ReadConfig
from utilites.readProperties_liquerNcorkage import ReadConfig_liquor_corkage


class Test_CokargeModul:
    base_URL = ReadConfig.getApplicationURL()
    userid = ReadConfig.getUserMail_V()
    password = ReadConfig.getPassword_V()
    cokarge_name = ReadConfig_liquor_corkage.getCokarage_Name()
    price = ReadConfig_liquor_corkage.getPrice_cokarage()
    remark = ReadConfig_liquor_corkage.getCokarage_remark()
    Qty = ReadConfig_liquor_corkage.getCokarage_Qty()


    logger = LogGen.loggen()


    def test_titleCokargePage(self,setup):
        self.logger.info("*****************Test Corkage Page ******************")
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


    def test_cokarge_modul(self,setup):
        self.logger.info("................ Cokarge Page Test ...............")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.logger.info("................ Vendor SignIn ...............")
        self.vl = VendorPage(self.driver)
        self.vl.Click_signup(self.userid,self.password)
        self.logger.info("................ Click Cokarge List ...............")
        self.cm = CreateCokargePage(self.driver)
        self.cm.click_Cokarge_List_T()
        time.sleep(2)
        self.logger.info("................ Click Edit...............")
        self.ce = Edit_cokarge_list_page(self.driver)
        self.ce.click_edit()
        time.sleep(2)
        self.cm.enter_Cokarge_PackageName(self.cokarge_name)
        time.sleep(2)
        self.cm.package_cokarge_price(self.price)
        time.sleep(2)
        self.cm.click_remark(self.remark)
        time.sleep(2)
        self.cm.click_frequenly()
        time.sleep(2)
        self.cm.click_status()
        time.sleep(2)
        self.logger.info("................ Create Cokarge Packge ...............")
        self.cm.click_create_package()
        time.sleep(2)
        self.logger.info("................ Select Cokarage Items ..............")
        self.logger.info("................ Test End ...............")

        self.cs = Cokarge_SelectItems(self.driver)
        self.cs.select_type() # loop use
        time.sleep(2)
        self.cs.enter_Qunity(self.Qty)
        time.sleep(2)
        self.cs.select_unit()
        time.sleep(2)
        self.cs.enter_price(self.price)
        time.sleep(2)
        self.cs.click_Add_cokarge()
        time.sleep(2)
        self.logger.info("................ Delete Item ...............")
        self.cs.click_delete()
        time.sleep(3)
        self.driver.quit()


        # for x in range(1,3):
        #     self.cs.select_type()  # loop use
        #     self.cs.select_Qunity(self.Qty)
        #     self.cs.select_unit()
        #     self.cs.enter_price(self.price)
        #     self.cs.click_Add_cokarge()
        #     self.logger.info("................ Delete Item ...............")
        #     self.cs.click_delete()
        # self.logger.info("................ Test End ...............")




