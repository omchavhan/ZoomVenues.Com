from pageObject.Admin_Modul.AdminLogin import AdminPage
from pageObject.Admin_Modul.AdminVenuesEnquiry_Page import AVenuesEnquiry
from pageObject.Booking_Process.BookingPayment import BookingPayment
from utilites.readProperties import ReadConfig


class Test_bookingpayment:
    base_URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserMail()
    password1 = ReadConfig.getPassword()
    card_no = ReadConfig.getCardNo()
    card_exp_date = ReadConfig.getCardExpDate()
    card_cvv = ReadConfig.getCardCVV()


    def test_booking(self,setup):
        try:
          self.driver = setup
          iderror_title = self.driver.title

          if iderror_title == "🧨 Undefined property: stdClass::$data":
             self.driver.refresh()
          else:
              print("id error")

        finally:
            self.driver.get(self.base_URL)
            self.av = AVenuesEnquiry(self.driver)
            self.al = AdminPage(self.driver)
            self.bm = BookingPayment(self.driver)
            self.al.Click_venues_signup(self.username, self.password1)
            self.av.ClickVenuesEnquiry()
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
            self.driver.quit()

