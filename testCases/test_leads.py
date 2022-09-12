import time

from pageObject.LeadsModul import LeadsModul
from utilites.readProperties import ReadConfig
from utilites.customeLogger import LogGen
from pageObject.AdminLogin import AdminPage
from pageObject.SocialVenues_LeadBanquets import SocialVenues

class Test_004_leads:

    base_URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserMail()
    password = ReadConfig.getPassword()
    Name = ReadConfig.getName()
    Mail = ReadConfig.getMail()
    Phone_no = ReadConfig.getPhoneNo()
    Date = ReadConfig.getDate()
    Time = ReadConfig.getTime()

    logger = LogGen.loggen()

    def test_leads(self,setup):
        self.logger.info("---------- Leads Test START ----------")
        self.logger.info("---------- Test_004 Verify ----------")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.lp = AdminPage(self.driver)
        self.sb = SocialVenues(self.driver)
        self.sb.select_venue()
        self.sb.setName(self.Name)
        self.sb.setMail(self.Mail)
        self.sb.setPhoneNo(self.Phone_no)
        self.sb.setEventType()
        self.sb.setDate(self.Date)
        self.sb.setTime(self.Time)
        self.sb.setNoPeople()
        self.sb.setBudget()
        self.sb.setReq()
        self.sb.setTermCondtion()
        self.sb.clickSubmit()
        self.sb.closePopup()
        self.lp.Click_venues_signup(self.username,self.password)
        self.lead = LeadsModul(self.driver)
        self.lead.click_leads()
        self.lead.click_edit()
        self.lead.selectVenueNm()
        self.lead.select_Status()
        time.sleep(5)
        self.lead.setSubmit()
        time.sleep(5)
        self.driver.quit()

