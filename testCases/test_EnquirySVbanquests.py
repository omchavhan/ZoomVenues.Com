from pageObject.SocialVenues_EnquiryBanquets import EnquryBanquets
from utilites.readProperties import ReadConfig
from utilites.customeLogger import LogGen
from pageObject.SocialVenues_LeadBanquets import SocialVenues
import time



class Test_006_enquiryBanquests:
    base_URL = ReadConfig.getApplicationURL()
    Name = ReadConfig.getName()
    Mail = ReadConfig.getMail()
    Phone_no = ReadConfig.getPhoneNo()
    Date = ReadConfig.getDate()
    Time = ReadConfig.getTime()
    No_pople = ReadConfig.getNoPeople()

    logger = LogGen.loggen()

    def test_title(self,setup):
        self.logger.info("---------- Test 0005 Start -----")
        self.logger.info("---------- test title -----")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.act_title = self.driver.title

        if self.act_title == "Best venues in Dubai - zoomvenues.info":
            self.logger.info("---------- Verify Title -----")
            self.driver.close()
            assert True
        else:
            self.logger.error("------------ title error -----------")
            self.driver.save_screenshot("C:\\Users\\GiTESH SONAR\\PycharmProjects\\ZoomVenues.Com\\ScreenShots\\" + "home_title123.png")
            # now1 = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            # self.driver.save_screenshot("C:\\Users\\GiTESH SONAR\\PycharmProjects\\ZoomVenues.Com\\ScreenShots-%s.png" % now1)
            self.logger.error("------------ title error -----------")
            self.driver.close()
            assert False

    def test_enqurybanquests(self,setup):
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


        time.sleep(3)
        self.act_title = self.driver.title

        if self.act_title == "Best venues of categories - zoomvenues.info":
            self.logger.info("---------- Verify Title -----")
            self.driver.close()
            assert True
        else:
            self.logger.error("------------ title error -----------")
            self.driver.save_screenshot("C:\\Users\\GiTESH SONAR\\PycharmProjects\\ZoomVenues.Com\\ScreenShots\\" + "home_title1.png")
            # now = self.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            # self.driver.save_screenshot(
            #     "C:\\Users\\GiTESH SONAR\\PycharmProjects\\GoogleAuto\\ScreenShots-%s.png" % now)
            self.logger.error("------------ title error -----------")
            self.driver.close()
            assert False

