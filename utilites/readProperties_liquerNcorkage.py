import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\GiTESH SONAR\\PycharmProjects\\ZoomVenues.Com\\Configuration\\config.ini")

class ReadConfig_liquor_corkage:

    @staticmethod
    def getLiquorName():
        LiquorName = config.get('Liquor and Cokarge Info', 'liquor_packgename')
        return LiquorName

    @staticmethod
    def getHours():
        hours = config.get('Liquor and Cokarge Info', 'hours')
        return hours

    @staticmethod
    def getPrice():
        price = config.get('Liquor and Cokarge Info', 'price')
        return price

    @staticmethod
    def getDetials():
        detials = config.get('Liquor and Cokarge Info', 'detials')
        return detials

    @staticmethod
    def getDetials():
        detials = config.get('Liquor and Cokarge Info', 'detials')
        return detials

# Cokarge Info
    @staticmethod
    def getPrice_cokarage():
        price = config.get('Liquor and Cokarge Info', 'cokarage_price')
        return price

    @staticmethod
    def getCokarage_Name():
        cokarage_packgename = config.get('Liquor and Cokarge Info', 'cokarage_packgename')
        return cokarage_packgename

    @staticmethod
    def getCokarage_remark():
        remark = config.get('Liquor and Cokarge Info', 'remark')
        return remark

    @staticmethod
    def getCokarage_Qty():
        Qty = config.get('Liquor and Cokarge Info', 'qunity')
        return Qty

    @staticmethod
    def getRemark():
        remark = config.get('Liquor and Cokarge Info', 'qunity')
        return remark



