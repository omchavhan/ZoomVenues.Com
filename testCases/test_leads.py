from pageObject.LeadsModul import LeadsModul
from utilites.readProperties import ReadConfig
from utilites.customeLogger import LogGen
from pageObject.AdminLogin import AdminPage

class Test_004_leads:

    base_URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserMail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_leads(self,setup):
        self.logger.info("---------- Leads Test START ----------")
        self.logger.info("---------- Test_004 Verify ----------")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.lp = AdminPage(self.driver)
        self.lp.Click_venues_signup(self.username,self.password)
        self.lead = LeadsModul(self.driver)
        self.lead.click_leads()
        self.lead.click_edit()
        self.driver.quit()

