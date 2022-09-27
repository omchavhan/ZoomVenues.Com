from pageObject.Admin_Modul.AdminBusinessHubs_page import BusinesHubs
from utilites.readProperties_Admin import ReadConfigg
from utilites.customeLogger import LogGen
from pageObject.Admin_Modul.AdminLogin import AdminPage





class Test_AdminBhubs:
    base_URL = ReadConfigg.getApplicationURL()
    username = ReadConfigg.getUserMail()
    password = ReadConfigg.getPassword()
    BHname2 = ReadConfigg.getBHname()
    JobTitle = ReadConfigg.getJobTitle()
    Fname = ReadConfigg.getFname()
    Lname = ReadConfigg.getLname()
    Mail = ReadConfigg.getMail()
    MobNo = ReadConfigg.getMobNo()
    CEOName = ReadConfigg.getCEOName()
    CEOMail = ReadConfigg.getCEOMail()
    CAFOName = ReadConfigg.getCAFOName()
    CAFOMail = ReadConfigg.getCAFOMail()
    Upload = ReadConfigg.getUpload()


    logger = LogGen.loggen()



    def test_008_BusinessHubs(self,setup):
        self.driver= setup
        self.driver.get(self.base_URL)
        self.lp = AdminPage(self.driver)
        self.lp.Click_venues_signup(self.username, self.password)

        self.ab = BusinesHubs(self.driver)
        self.ab.clickBH()
        self.ab.clickEdit()
        self.ab.setBHnm(self.BHname2)
        self.ab.setBHnm(self.JobTitle)
        self.ab.setBHnm(self.Fname)
        self.ab.setBHnm(self.Lname)
        self.ab.setBHnm(self.Mail)
        self.ab.setBHnm(self.MobNo)
        self.ab.setBHnm(self.CEOName)
        self.ab.setBHnm(self.CEOMail)
        self.ab.setBHnm(self.CAFOName)
        self.ab.setBHnm(self.CAFOMail)
        # self.ab.setBHnm(self.Upload)