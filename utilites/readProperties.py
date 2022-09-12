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


