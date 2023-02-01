import time

from pageObject.DesiForms.LogInFun import LogIn
from utilites.read_Properties_DesiForms import ReadConfig_desi





class Test_Login:
    Base_url = ReadConfig_desi.getBase_Url()
    Mobile_no = ReadConfig_desi.getMobile_No()
    Otp_no = ReadConfig_desi.getOTP_verify_No()
    your_name = ReadConfig_desi.getYour_name()
    area = ReadConfig_desi.getArea()
    sub_area = ReadConfig_desi.getSUb_Area()


    def test_logIn(self,setup):
        self.driver =  setup
        self.driver.get(self.Base_url)

        self.li = LogIn(self.driver)
        self.li.loction_select()
        time.sleep(2)
        self.li.click_signIn()
        time.sleep(2)
        self.li.enter_mobile_no(self.Mobile_no)
        time.sleep(2)
        self.li.click_logIn()
        time.sleep(2)
        self.li.enter_otp(self.Otp_no)
        time.sleep(2)
        self.li.click_otp_verification()
        time.sleep(2)
        self.li.enter_your_name(self.your_name)
        time.sleep(2)
        self.li.select_gender()
        time.sleep(2)
        self.li.select_find_us()
        time.sleep(2)
        self.li.select_area(self.area)
        time.sleep(2)
        self.li.select_SuBarea(self.sub_area)
        time.sleep(2)
        self.li.click_register()
