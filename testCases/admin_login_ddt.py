from pageObject.AdminLogin import AdminPage
import pytest
from utilites.readProperties import ReadConfig
from utilites.customeLogger import LogGen
from utilites import XLUnites


class Test_003_adminLogin_ddt:
    base_URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserMail()
    password = ReadConfig.getPassword()
    path = "/TestData/AdminLoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_admin_login(self,setup):
        self.logger.info("................ Admin Page Login Test ...............")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lp = AdminPage(self.driver)
        self.lp.Click_venues_signup(self.username,self.password)


    def test_admin_login_ddt(self,setup):
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lp = AdminPage(self.driver)

        self.rows = XLUnites.getRowCount(self.path, 'Sheet1')
        print("Numbers of Rows i a Excel:", self.rows)

        lst_status = []  # Empty List Variable

        for r in range(2, self.rows + 1):
            self.user = XLUnites.readData(self.path, "Sheet1", r, 1)
            self.password1 = XLUnites.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUnites.readData(self.path, "Sheet1", r, 3)

            self.lp.Profile()
            self.lp.LogIn()
            self.lp.Close_vendor_poup()
            self.lp.MailId(self.user)
            self.lp.Password(self.password1)


            act_title = self.driver.title
            exp_title = "Zoomvenues | Dashboard "

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****Passed*******")
                    self.lp.LogOut()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*****Failed********")
                    # self.lp.Profile()
                    self.lp.LogOut()
                    # self.lp.Close_vendor_poup()
                    # self.lp.MailId(self.user)
                    # self.lp.Password(self.password1)
                    # self.lp.LogIn()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****Failed******")
                    lst_status.append("Pass")
                elif self.exp != "Fail":
                    self.logger.info("*****Passed*********")
                    lst_status.append("Pass")
                if self.exp == "Pass":
                    self.logger.info("*****Passed*******")
                    # self.lp.Profile()
                    self.lp.LogOut()
                    # self.lp.Close_vendor_poup()
                    # self.lp.MailId(self.user)
                    # self.lp.Password(self.password1)
                    # self.lp.LogIn()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*****Failed********")
                    # self.lp.Profile()
                    self.lp.LogOut()
                    # self.lp.Close_vendor_poup()
                    # self.lp.MailId(self.user)
                    # self.lp.Password(self.password1)
                    # self.lp.LogIn()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****Failed******")
                    lst_status.append("Pass")
                elif self.exp != "Fail":
                    self.logger.info("*****Passed*********")
                    lst_status.append("Pass")



        if "Fail" not in lst_status:
            self.logger.info("*************Login DDT Test Pass*************")
            self.driver.close()
            assert True

        else:
            self.logger.info("*************Login DDT Test Failed*************")
            self.driver.close()
            assert False

        self.logger.info("*************End of Login DDT Test*******************")
        self.logger.info("**************Completed TC_LoginDDT__002******************")


