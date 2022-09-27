import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\GiTESH SONAR\\PycharmProjects\\ZoomVenues.Com\\Configuration\\config.ini")

class ReadConfigg:
    @staticmethod
    def getApplicationurl():
        base_url = config.get('BusinessHubs info', 'base_url')
        return base_url

    @staticmethod
    def getUserMail():
        userid = config.get('BusinessHubs info', 'userid')
        return userid

    @staticmethod
    def getPassword():
        password = config.get('BusinessHubs info', 'password')
        return password

    @staticmethod
    def getBHname():
        BHname1 = config.get('BusinessHubs info', 'BHname')
        return BHname1

    @staticmethod
    def getJobTitle():
        JobTitle = config.get('BusinessHubs info', 'JobTitle')
        return JobTitle

    @staticmethod
    def getFname():
        Fname = config.get('BusinessHubs info', 'Fname')
        return Fname

    @staticmethod
    def getLname():
        Lname = config.get('BusinessHubs info', 'Lname')
        return Lname

    @staticmethod
    def getMail():
        Mail = config.get('BusinessHubs info', 'Mail')
        return Mail

    @staticmethod
    def getMobNo():
        MobNo = config.get('BusinessHubs info', 'MobNo')
        return MobNo

    @staticmethod
    def getCEOName():
        CEOName = config.get('BusinessHubs info', 'CEOName')
        return CEOName

    @staticmethod
    def getCEOMail():
        CEOMail = config.get('BusinessHubs info', 'CEOMail')
        return CEOMail

    @staticmethod
    def getCAFOName():
        CAFOName = config.get('BusinessHubs info', 'CAFOName')
        return CAFOName

    @staticmethod
    def getCAFOMail():
        CAFOMail = config.get('BusinessHubs info', 'CAFOMail')
        return CAFOMail

    @staticmethod
    def getUpload():
        upload = config.get('BusinessHubs info', 'imgPath')
        return upload

    @staticmethod
    def getFinalOffer():
        finaloffer = config.get('BusinessHubs info', 'final_offer')
        return finaloffer

    @staticmethod
    def getTermCodi():
        termcondi = config.get('BusinessHubs info', 'term_condition')
        return termcondi

    @staticmethod
    def getCmdBH():
        cmdBH = config.get('BusinessHubs info', 'cmdforBH')
        return cmdBH

    @staticmethod
    def getBHOfferPrice():
        bhoffprice = config.get('BusinessHubs info', 'bhoffprice')
        return bhoffprice

    @staticmethod
    def getZv2comission():
        zv2comission = config.get('BusinessHubs info', 'zv2comission')
        return zv2comission











