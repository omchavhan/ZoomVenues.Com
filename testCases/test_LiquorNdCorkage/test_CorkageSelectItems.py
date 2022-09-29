import time

from pageObject.VendorModule.VendorLogin_Page import VendorPage
from pageObject.LiquorNdCorkage.Create_CorkagePakage import CreateCokargePage
from pageObject.LiquorNdCorkage.Corkage_SelectItems import Cokarge_SelectItems
from pageObject.LiquorNdCorkage.EditCorkagePackage import Edit_cokarge_list_page
from utilites.customeLogger import LogGen
from utilites.readProperties import ReadConfig
from utilites.readProperties_liquerNcorkage import ReadConfig_liquor_corkage






class Test_CokargeSelectItems:
    base_URL = ReadConfig.getApplicationURL()
    userid = ReadConfig.getUserMail_V()
    password = ReadConfig.getPassword_V()
    price = ReadConfig_liquor_corkage.getPrice_cokarage()
    Qty = ReadConfig_liquor_corkage.getCokarage_Qty()
    Remark = ReadConfig_liquor_corkage.getCokarage_remark()

    logger = LogGen.loggen()




    def test_cokarge_selectItems(self,setup):
        self.logger.info("................ Cokarge Page Test ...............")
        self.driver = setup
        self.driver.get(self.base_URL)
        act_title = self.driver.title

        if act_title == "🧨 Trying to get property 'data' of non-object":
            self.driver.refresh()
            time.sleep(2)
        else:
            self.logger.info("................ Cokarge Page Test ...............")
            self.driver = setup
            self.driver.get(self.base_URL)
            self.logger.info("................ Vendor SignIn ...............")
            self.vl = VendorPage(self.driver)
            self.vl.Click_signup(self.userid, self.password)
            self.logger.info("................ Click Cokarge List ...............")
            self.cm = CreateCokargePage(self.driver)
            self.cm.click_Cokarge_List_T()
            time.sleep(2)
            self.logger.info("................ Click Edit...............")
            self.ce = Edit_cokarge_list_page(self.driver)
            self.ce.click_edit()
            time.sleep(2)
            self.logger.info("................ Select Corkage...............")
            for select1 in range(0, 4):
                self.cs = Cokarge_SelectItems(self.driver)
                time.sleep(2)
                self.cs.select_type()  # loop use
                time.sleep(2)
                self.cs.enter_Qunity(self.Qty)
                time.sleep(2)
                self.cs.select_unit()
                time.sleep(2)
                self.cs.enter_price(self.price)
                time.sleep(2)
                self.cs.enter_remark(self.Remark)
                self.cs.click_Add_cokarge()
                print("Corkage Select ...")
            self.driver.quit()
            self.logger.info("................ End Test...............")



