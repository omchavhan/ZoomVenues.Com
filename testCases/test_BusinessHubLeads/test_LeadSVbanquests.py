import time

from pageObject.SocialVenues_LeadBanquets import SocialVenues
from utilites.readProperties import ReadConfig
from utilites.customeLogger import LogGen
from datetime import datetime

class Test_005_banquests:
    base_URL = ReadConfig.getApplicationURL()
    Name = ReadConfig.getName()
    Mail = ReadConfig.getMail()
    Phone_no = ReadConfig.getPhoneNo()
    Date = ReadConfig.getDate()
    Time = ReadConfig.getTime()

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

    def test_banquests(self,setup):
        self.logger.info("----------- start test banquests --------")
        self.driver = setup
        self.driver.get(self.base_URL)
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
            # self.driver.save_screenshot("C:\\Users\\GiTESH SONAR\\PycharmProjects\\GoogleAuto\\ScreenShots-%s.png" % now)
            self.logger.error("------------ title error -----------")
            self.driver.close()
            assert False




