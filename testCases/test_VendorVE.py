from pageObject.AdminVenuesEnquiry_Page import AVenuesEnquiry
from utilites.readProperties import ReadConfig
from utilites.customeLogger import LogGen
from pageObject.VendorLogin_Page import VendorPage




class Test_VenuesEnquiry:
    base_URL = ReadConfig.getApplicationURL()
    userid = ReadConfig.getUserMail_V()
    password = ReadConfig.getPassword_V()

    logger = LogGen.loggen()

    def test_venuesenquiry(self,setup):
        self.logger.info("--------------------- Test Start Venues Enquiry ------------------")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.ev = AVenuesEnquiry(self.driver)
        self.al = VendorPage(self.driver)
        self.al.Click_signup(self.userid,self.password)
        self.ev.ClickVenuesEnquiry()
        self.ev.ClickNewResp()
        self.driver.quit()
        self.logger.info("------------------------ End Testing -------------------")




