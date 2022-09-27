import time

from pageObject.Booking_Process.ConformVenue import ConformVenuesEnq
from pageObject.Admin_Modul.AdminLogin import AdminPage
from utilites.readProperties_Admin import ReadConfigg
from utilites.customeLogger import LogGen




class Test_ConformVenues:
    base_URL = ReadConfigg.getApplicationurl()
    Userid = ReadConfigg.getUserMail()
    Password = ReadConfigg.getPassword()
    finaloffer = ReadConfigg.getFinalOffer()
    termacondtion = ReadConfigg.getTermCodi()
    BHOfferPrice = ReadConfigg.getBHOfferPrice()
    ZV2offer = ReadConfigg.getZv2comission()

    logger = LogGen.loggen()


    def test_conformvenues(self,setup):
        self.driver = setup
        errorid_title = self.driver.title
        if errorid_title == "🧨 Trying to get property 'data' of non-object":
            self.driver.refresh()
        else:
            self.driver.get(self.base_URL)
            self.al = AdminPage(self.driver)
            self.al.Click_venues_signup(self.Userid, self.Password)
            self.cv = ConformVenuesEnq(self.driver)
            self.cv.click_venuesenquiry()
            self.cv.click_edit_a()
            self.cv.select_arrgment()
            self.cv.enter_finaloffer(self.finaloffer)
            self.cv.enter_termcodition(self.termacondtion)
            self.cv.enter_bhofferprice(self.BHOfferPrice)
            self.cv.enter_zv2markupcom(self.ZV2offer)
            self.cv.select_status()
            self.cv.click_save()
            time.sleep(3)
            self.driver.quit()




