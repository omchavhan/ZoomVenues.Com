import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\GiTESH SONAR\\PycharmProjects\\ZoomVenues.Com\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        base_url = config.get('common info', 'base_url')
        return base_url

    @staticmethod
    def getUserMail():
        userid = config.get('common info', 'userid')
        return userid

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getUserMail_V():
        userid = config.get('common info', 'user_vendor')
        return userid

    @staticmethod
    def getPassword_V():
        password = config.get('common info', 'password_vendor')
        return password

    @staticmethod
    def getName():
        name = config.get('common info', 'name')
        return name

    @staticmethod
    def getMail():
        mail = config.get('common info', 'mail')
        return mail

    @staticmethod
    def getPhoneNo():
        phoneno = config.get('common info', 'phone_no')
        return phoneno

    @staticmethod
    def getDate():
        date = config.get('common info', 'date')
        return date

    @staticmethod
    def getTime():
        time = config.get('common info', 'time')
        return time

    @staticmethod
    def getNoPeople():
        no_people = config.get('common info', 'no_people')
        return no_people

    @staticmethod
    def getCardNo():
        card_no = config.get('common info', 'card_no')
        return card_no

    @staticmethod
    def getCardExpDate():
        card_exp_date = config.get('common info', 'card_exp_date')
        return card_exp_date

    @staticmethod
    def getCardCVV():
        card_cvv = config.get('common info', 'card_cvv')
        return card_cvv

    @staticmethod
    def getCmdResp():
        cmd_resp = config.get('common info', 'cmd_resp')
        return cmd_resp


