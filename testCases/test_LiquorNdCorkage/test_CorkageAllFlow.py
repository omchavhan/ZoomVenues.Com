import time

import pytest

from pageObject.VendorModule.VendorLogin_Page import VendorPage
from pageObject.LiquorNdCorkage.Create_CorkagePakage import CreateCokargePage
from pageObject.LiquorNdCorkage.Corkage_SelectItems import Cokarge_SelectItems
from pageObject.LiquorNdCorkage.EditCorkagePackage import Edit_cokarge_list_page
from pageObject.LiquorNdCorkage.Corkage_Delete import Cokarge_DeleteItems
from utilites.customeLogger import LogGen
from utilites.readProperties import ReadConfig
from utilites.readProperties_liquerNcorkage import ReadConfig_liquor_corkage


class Test_EditCokargeModul:
    base_URL = ReadConfig.getApplicationURL()
    userid = ReadConfig.getUserMail_V()
    password = ReadConfig.getPassword_V()
    cokarge_name = ReadConfig_liquor_corkage.getCokarage_Name()
    price = ReadConfig_liquor_corkage.getPrice_cokarage()
    remark = ReadConfig_liquor_corkage.getCokarage_remark()
    Qty = ReadConfig_liquor_corkage.getCokarage_Qty()
    Remark = ReadConfig_liquor_corkage.getCokarage_remark()


    logger = LogGen.loggen()

    @pytest.mark.sanity
    # @pytest.mark.skip
    def test_CokargePageTitle(self,setup):
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

    @pytest.mark.skip
    def test_createcokarge_modul(self,setup):
        self.logger.info("................ Cokarge Page Test ...............")
        self.driver = setup
        act_title = self.driver.title

        if act_title == "🧨 Trying to get property 'data' of non-object" or act_title != "🧨 Trying to get property 'data' of non-object":
            self.driver.refresh()
            self.driver.get(self.base_URL)
            self.logger.info("................ Vendor SignIn ...............")
            self.vl = VendorPage(self.driver)
            self.vl.Click_signup(self.userid, self.password)
            self.logger.info("................ Click Cokarge List ...............")
            self.cm = CreateCokargePage(self.driver)
            self.cm.click_Cokarge_List_T()
            time.sleep(2)
            self.logger.info("................ Click Add New ...............")
            self.cm.click_Add()
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
            self.cm.click_corkagelist()
            self.driver.quit()
            self.logger.info("................ End Test ..............")



    @pytest.mark.sanity
    def test_cokarge_selectItems(self,setup):
        self.logger.info("................ Cokarge Page Test ...............")
        self.driver = setup
        self.driver.get(self.base_URL)
        act_title = self.driver.title

        if act_title == "🧨 Trying to get property 'data' of non-object" or act_title != "🧨 Trying to get property 'data' of non-object":
            self.driver.refresh()
            time.sleep(2)
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

    @pytest.mark.sanity
    # @pytest.mark.skip
    def test_DeletecokargeItems(self,setup):
        self.logger.info("................ Cokarge Page Test ...............")
        self.driver = setup
        act_title = self.driver.title

        if act_title == "🧨 Trying to get property 'data' of non-object" or act_title != "🧨 Trying to get property 'data' of non-object":
            self.driver.refresh()
            time.sleep(2)
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

            self.logger.info("................ Delete Item ...............")
            for delete in range(0, 3):
                self.cd = Cokarge_DeleteItems(self.driver)
                self.cd.click_delete()
                time.sleep(2)

            self.driver.quit()
            self.logger.info("................ End test ...............")



