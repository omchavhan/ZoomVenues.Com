import time
from pageObject.BHLeads.LeadsModul import LeadsModul
from utilites.readProperties import ReadConfig
from utilites.customeLogger import LogGen
from pageObject.Admin_Modul.AdminLogin import AdminPage
from pageObject.SocialVenues_LeadBanquets import SocialVenues
from utilites import XLUnites

class Test_004_leads:

    base_URL = ReadConfig.getApplicationURL()
    # username = ReadConfig.getUserMail()
    # password = ReadConfig.getPassword()
    # Name = ReadConfig.getName()
    # Mail = ReadConfig.getMail()
    # Phone_no = ReadConfig.getPhoneNo()
    Date = ReadConfig.getDate()
    # Time = ReadConfig.getTime()
    path= "/TestData/LoginData.xlsx"

    logger = LogGen.loggen()

    def test_leads(self,setup):
        self.logger.info("---------- Leads Test START ----------")
        self.logger.info("---------- Test_004 Verify ----------")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


        self.rows = XLUnites.getRowCount(self.path, 'Sheet1')
        print("Numbers of Rows i a Excel:", self.rows)
        # lst_status = []


        for r in range(2, self.rows + 1):
            self.user = XLUnites.readData(self.path, "Sheet1", r, 1)
            self.password1 = XLUnites.readData(self.path, "Sheet1", r, 2)
            self.your_name = XLUnites.readData(self.path, "Sheet1", r, 3)
            self.mailId = XLUnites.readData(self.path, "Sheet1", r, 4)
            self.PhoneNo = XLUnites.readData(self.path, "Sheet1", r, 5)
            # self.date1 = XLUnites.readData(self.path, "Sheet1", r, 6)
            self.time1 = XLUnites.readData(self.path, "Sheet1", r, 7)
            self.addReq = XLUnites.readData(self.path, "Sheet1", r, 8)
            # self.exp = XLUnites.readData(self.path, "Sheet1", r, 9)

            self.lp = AdminPage(self.driver)
            self.sb = SocialVenues(self.driver)
            self.sb.select_venue()
            self.sb.setName(self.your_name)
            self.sb.setMail(self.mailId)
            self.sb.setPhoneNo(self.PhoneNo)
            self.sb.setEventType()
            self.sb.setDate(self.Date)
            self.sb.setTime(self.time1)
            self.sb.setNoPeople()
            self.sb.setBudget()
            self.sb.setReq()
            self.sb.setTermCondtion()
            self.sb.clickSubmit()
            self.sb.closePopup()
            self.lp.Click_venues_signup(self.user, self.password1)
            self.lead = LeadsModul(self.driver)
            self.lead.click_leads()
            self.lead.click_edit()
            self.lead.selectVenueNm()
            self.lead.select_Status()
            time.sleep(5)
            self.lead.setSubmit()
            time.sleep(5)

            # act_title = self.driver.title
            # exp_title = "Zoomvenues | Dashboard "
            #
            # if act_title == exp_title:
            #     if self.exp == "Pass":
            #         self.logger.info("*****Passed*******")
            #         self.lead.Logout()
            #         lst_status.append("Pass")
            #     elif self.exp == "Fail":
            #         self.logger.info("*****Failed********")
            #         self.lead.Logout()
            #         lst_status.append("Fail")
            # elif act_title != exp_title:
            #     if self.exp == "Pass":
            #         self.logger.info("*****Failed******")
            #         lst_status.append("Pass")
            #     elif self.exp != "Fail":
            #         self.logger.info("*****Passed*********")
            #         lst_status.append("Pass")
            #     if self.exp == "Pass":
            #         self.logger.info("*****Passed*******")
            #         self.lead.Logout()
            #         lst_status.append("Pass")
            #     elif self.exp == "Fail":
            #         self.logger.info("*****Failed********")
            #         self.lead.Logout()
            #         lst_status.append("Fail")
            # elif act_title != exp_title:
            #     if self.exp == "Pass":
            #         self.logger.info("*****Failed******")
            #         lst_status.append("Pass")
            #     elif self.exp != "Fail":
            #         self.logger.info("*****Passed*********")
            #         lst_status.append("Pass")
            #
            # if "Fail" not in lst_status:
            #     self.logger.info("*************Login DDT Test Pass*************")
            #     self.driver.close()
            #     assert True
            #
            # else:
            #     self.logger.info("*************Login DDT Test Failed*************")
            #     self.driver.close()
            #     assert False
            #
            # self.logger.info("*************End of Login DDT Test*******************")
            # self.logger.info("**************Completed TC_LoginDDT__002******************")





