import time

from pageObject.BHLeads.BHLead_Modul import BH_Lead
from pageObject.Admin_Modul.AdminLogin import AdminPage
from utilites.readProperties import ReadConfig
class Test_BHLead:
    base_URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserMail()
    password1 = ReadConfig.getPassword()
    cmd_resp = ReadConfig.getCmdResp()


    def test_bhlead(self,setup):
        self.driver = setup
        self.driver.get(self.base_URL)
        self.bhl = BH_Lead(self.driver)
        self.al = AdminPage(self.driver)
        self.al.Click_venues_signup(self.username, self.password1)
        self.bhl.click_BHLead()
        self.bhl.click_Edit()
        self.bhl.setCmdResp(self.cmd_resp)
        self.bhl.setSubmit()
        time.sleep(3)
        self.driver.quit()