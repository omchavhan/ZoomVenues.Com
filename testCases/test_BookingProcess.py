from pageObject.VendorLogin_Page import VendorPage
from  pageObject.AdminLogin import AdminPage
from pageObject.SocialVenues_EnquiryBanquets import EnquryBanquets
from pageObject.AdminVenuesEnquiry_Page import AVenuesEnquiry
from pageObject.VendorVenuesEnquiry_Page import VVenuesEnquiry
from utilites.readProperties import ReadConfig
from utilites.customeLogger import LogGen
from utilites.readProperties_Admin import ReadConfigg
from pageObject.SocialVenues_LeadBanquets import SocialVenues
from pageObject.BookingProcess_page import Booking
import time



class Test_006_enquiryBanquests:
    base_URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserMail()
    password1 = ReadConfig.getPassword()
    userid = ReadConfig.getUserMail_V()
    password = ReadConfig.getPassword_V()
    Name = ReadConfig.getName()
    Mail = ReadConfig.getMail()
    Phone_no = ReadConfig.getPhoneNo()
    Date = ReadConfig.getDate()
    Time = ReadConfig.getTime()
    No_pople = ReadConfig.getNoPeople()
    finalOffer = ReadConfigg.getFinalOffer()
    termCodition = ReadConfigg.getTermCodi()
    cmdBH = ReadConfigg.getCmdBH()

    logger = LogGen.loggen()


    def test_BookEnquiry(self,setup):
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lb = EnquryBanquets(self.driver)
        self.eb = SocialVenues(self.driver)
        self.eb.select_venue()
        time.sleep(2)
        self.lb.closePopup()
        time.sleep(2)
        self.lb.setEnquiry()
        self.lb.setName(self.Name)
        self.lb.setMail(self.Mail)
        self.lb.setPhoneNo(self.Phone_no)
        self.lb.setEventType()
        self.lb.setDate(self.Date)
        self.lb.setTime(self.Time)
        self.lb.setnoOfpeople(self.No_pople)
        self.lb.setbuget()
        self.lb.setaddReq()
        self.lb.setacc_term()
        self.lb.setSubmit()
        self.driver.quit()

    def test_admin_responce(self,setup):
        self.driver = setup
        self.driver.get(self.base_URL)
        self.al = AdminPage(self.driver)
        self.ev = AVenuesEnquiry(self.driver)
        self.al.Click_venues_signup(self.username,self.password1)
        self.ev.ClickVenuesEnquiry()
        self.ev.ClickNewResp()
        self.ev.selectSettingArrg()
        self.ev.setFinaloffer(self.finalOffer)
        self.ev.setTermCondtion(self.termCodition)
        self.ev.setCmdBH(self.cmdBH)
        self.ev.setStatus()
        self.ev.setSubmit()
        time.sleep(3)
        self.driver.quit()

    def test_vendor_response(self,setup):
        self.driver = setup
        self.driver.get(self.base_URL)
        self.ev = VVenuesEnquiry(self.driver)
        self.al = VendorPage(self.driver)
        self.al.Click_signup(self.userid, self.password)
        self.ev.ClickVenuesEnquiry()
        self.ev.ClickNewResp()
        self.ev.setSubmit()
        self.driver.quit()
