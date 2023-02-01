from pageObject.VendorModule.VendorLogin_Page import VendorPage
from pageObject.Admin_Modul.AdminLogin import AdminPage
from pageObject.Admin_Modul.AdminVenuesEnquiry_Page import AVenuesEnquiry
from pageObject.VendorModule.VendorVenuesEnquiry_Page import VVenuesEnquiry
from pageObject.Booking_Process.BookingPayment import BookingPayment
from pageObject.Booking_Process.VenueBooking import VenuesBooking
from pageObject.Booking_Process.ConformVenue import ConformVenuesEnq
from utilites.readProperties import ReadConfig
from utilites.customeLogger import LogGen
from utilites.readProperties_Admin import ReadConfigg
from pageObject.SocialVenues_LeadBanquets import SocialVenues
import time
import pytest



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
    BHOfferPrice = ReadConfigg.getBHOfferPrice()
    ZV2offer = ReadConfigg.getZv2comission()
    cmdBH = ReadConfigg.getCmdBH()
    card_no = ReadConfig.getCardNo()
    card_exp_date = ReadConfig.getCardExpDate()
    card_cvv = ReadConfig.getCardCVV()

    logger = LogGen.loggen()

    # @pytest.mark.skip
    def test_BookingVenuesEnquiry(self,setup):
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lb = VenuesBooking(self.driver)
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
        time.sleep(4)
        self.driver.quit()

    # @pytest.mark.skip
    def test_ConformEnquiry(self,setup):
        self.driver = setup
        self.driver.get(self.base_URL)
        self.cv = ConformVenuesEnq(self.driver)
        self.al =  AdminPage(self.driver)
        self.al.Click_venues_signup(self.username,self.password1)
        self.cv.click_venuesenquiry()
        self.cv.click_edit_a()
        self.cv.select_arrgment()
        self.cv.enter_finaloffer(self.finalOffer)
        self.cv.enter_termcodition(self.termCodition)
        self.cv.enter_bhofferprice(self.BHOfferPrice)
        self.cv.enter_zv2markupcom(self.ZV2offer)
        self.cv.select_status()
        self.cv.click_save()
        self.driver.quit()

    def test_bookingpayment(self,setup):
        self.driver = setup
        self.driver.get(self.base_URL)
        self.al = AdminPage(self.driver)
        self.ev = AVenuesEnquiry(self.driver)
        self.al.Click_venues_signup(self.username, self.password1)
        self.ev.ClickVenuesEnquiry()
        self.bm = BookingPayment(self.driver)
        self.bm.click_Action_booking()
        self.bm.click_booking()
        self.bm.click_yes()
        self.bm.copy_link()
        self.bm.click_ok()
        self.bm.close_page()
        self.bm.link_open_newTab()
        self.bm.click_payment()
        self.bm.insert_cardNo(self.card_no)
        self.bm.insert_card_exp(self.card_exp_date)
        self.bm.insert_card_CVV(self.card_cvv)
        time.sleep(3)
        self.driver.quit()


