# https://github.com/pavanoltraining/nopCommerceProject


import time

import pytest

from pageObject.LoginPage import LoginPage
from utilites.readProperties import ReadConfig
from utilites.customeLogger import LogGen
from utilites import XLUnites


class Test_001_login:

    base_URL = ReadConfig.getApplicationURL()
    path = "C:\\Users\\GiTESH SONAR\\PycharmProjects\\ZoomVenues.Com\\TestData\\LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login_ddt(self, setup):
        self.logger.info("*************Test_002_DDT_login*******************")
        self.logger.info("**************Verifing LogIn DDT Test******************")
        self.driver = setup
        self.driver.get(self.base_URL)

        self.lp = LoginPage(self.driver)

        self.rows = XLUnites.getRowCount(self.path, 'Sheet1')
        print("Numbers of Rows i a Excel:", self.rows)

        lst_status = []  # Empty List Variable

        for r in range(2, self.rows + 1):
            self.user = XLUnites.readData(self.path, "Sheet1", r, 1)
            self.password1 = XLUnites.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUnites.readData(self.path, "Sheet1", r, 3)

            self.lp.clickSignIn()
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password1)
            self.lp.setLogin()
            time.sleep(5)

            # time.sleep(2)

            act_title = self.driver.title
            exp_title = "zoomvenues.info"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****Passed*******")
                    self.lp.setLogOut()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*****Failed********")
                    self.lp.setLogOut()
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
                    self.lp.setLogOut()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*****Failed********")
                    self.lp.setLogOut()
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








