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
