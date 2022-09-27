from pageObject.Admin_Modul.AdminVenuesEnquiry_Page import AVenuesEnquiry
from utilites.readProperties_Admin import ReadConfigg
from utilites.customeLogger import LogGen
from pageObject.Admin_Modul.AdminLogin import AdminPage




class Test_VenuesEnquiry:
    base_URL = ReadConfigg.getApplicationurl()
    userid = ReadConfigg.getUserMail()
    password = ReadConfigg.getPassword()
    finalOffer = ReadConfigg.getFinalOffer()
    termCodition = ReadConfigg.getTermCodi()
    cmdBH = ReadConfigg.getCmdBH()

    logger = LogGen.loggen()

    def test_venuesenquiry(self,setup):
        self.logger.info("--------------------- Test Start Venues Enquiry ------------------")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.ev = AVenuesEnquiry(self.driver)
        self.al = AdminPage(self.driver)
        self.al.Click_venues_signup(self.userid,self.password)
        self.ev.ClickVenuesEnquiry()
        self.ev.ClickNewResp()
        self.ev.selectSettingArrg()
        self.ev.setFinaloffer(self.finalOffer)
        self.ev.setTermCondtion(self.termCodition)
        self.ev.setCmdBHself(self.cmdBH)
        self.ev.setStatus()
        self.ev.setSubmit()
        self.driver.quit()
        self.logger.info("------------------------ End Testing -------------------")




