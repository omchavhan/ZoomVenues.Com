import pytest
from pageObject.VendorResponseMail.VenueEnquiryToSearchBar import VenuesEnquiry
from pageObject.VendorResponseMail.VenueEnquiryToSearchBar import VenuesEnquiry
from pageObject.VendorModule.VendorLogin_Page import VendorPage
from pageObject.SocialVenues_EnquiryBanquets import EnquryBanquets
from pageObject.VendorModule.VendorVenuesEnquiry_Page import VVenuesEnquiry
from pageObject.Booking_Process.ConformVenue import ConformVenuesEnq
from utilites.readProperties import ReadConfig
from utilites.readProperties_Admin import ReadConfigg
from utilites.customeLogger import LogGen
import time

class Test_vendorresponsemail:
    base_URL =  ReadConfig.getApplicationURL()
    Password = ReadConfig.getPassword_V()
    Name = ReadConfig.getName()
    Mail = ReadConfig.getMail()
    MailId = ReadConfig.getUserMail_V()
    Phone_no = ReadConfig.getPhoneNo()
    Date = ReadConfig.getDate()
    Time = ReadConfig.getTime()
    No_pople = ReadConfig.getNoPeople()
    finaloffer = ReadConfigg.getFinalOffer()
    termacondtion = ReadConfigg.getTermCodi()
    BHOfferPrice = ReadConfigg.getBHOfferPrice()
    ZV2offer = ReadConfigg.getZv2comission()

    logger = LogGen.loggen()

    @pytest.mark.sanity_VendorResponceMail
    @pytest.mark.skip
    def test_vendor_responsemail(self,setup):
        self.driver = setup
        self.logger.info("------------------- Start Test ----------------")
        self.driver.get(self.base_URL)
        self.v = VenuesEnquiry(self.driver)
        self.v.click_CorporateVenues()
        self.logger.info("------------------- User Search Bar ----------------")
        self.logger.info("------------------- Click CorporateVenues ----------------")
        self.v.select_loction()
        self.logger.info("------------------- select Loction ----------------")
        self.v.select_venues()
        self.logger.info("------------------- Select Venues ----------------")
        # self.v.select_event()
        self.v.select_submit()
        self.logger.info("------------------- Select Submit ----------------")
        self.v.select_close_popup()
        self.logger.info("------------------- Close Popup ----------------")
        self.v.select_enquiry()
        self.logger.info("------------------- Select and Start Enquiry ----------------")

        self.lb = EnquryBanquets(self.driver)
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
        self.logger.info("------------------- Submit Enquiry ----------------")
        time.sleep(4)
        self.driver.quit()

    @pytest.mark.sanity_VendorResponceMail
    # @pytest.mark.skip
    def test_vendorResponse(self,setup):
        self.driver = setup
        self.driver.get(self.base_URL)
        self.vl = VendorPage(self.driver)
        self.vl.Click_signup(self.MailId,self.Password)
        self.rs = VVenuesEnquiry(self.driver)
        self.vv = VenuesEnquiry(self.driver)
        self.logger.info("------------------- Start Venues Response ----------------")
        self.rs.ClickVenuesEnquiry()
        self.logger.info("------------------- Click Enquiry ----------------")
        self.rs.ClickNewResp()
        self.logger.info("------------------- Click New Response ----------------")
        self.cv = ConformVenuesEnq(self.driver)

        # self.cv.select_menu()
        self.cv.select_arrgment()
        self.cv.enter_finaloffer(self.finaloffer)
        self.cv.enter_termcodition(self.termacondtion)
        self.cv.enter_bhofferprice(self.BHOfferPrice)
        self.cv.enter_zv2markupcom(self.ZV2offer)
        self.vv.click_save()
        self.logger.info("------------------- Save Venues ----------------")
        time.sleep(3)
        self.driver.quit()
        self.logger.info("------------------- End Test ----------------")


