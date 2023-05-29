from pageObject.Login_Modul.LoginPage import LoginPage
from pageObject.Search_Bar.Search_Bar import Test_Search_Bar
from utilites.readProperties import ReadConfig
from utilites.customeLogger import LogGen


class Test_search_01:

    base_URL = ReadConfig.getApplicationURL()

    # logger = LogGen.loggen()

    def test_search_bar(self,setup):
        self.driver = setup
        self.driver.get(self.base_URL)
        self.sb = Test_Search_Bar(self.driver)
        self.sb.select_location()
        self.sb.select_event_or_services()

