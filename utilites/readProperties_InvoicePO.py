import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\ergit\\PycharmProjects\\ZoomVenues.Com\\Configuration\\config.ini")


class ReadConfig_I:

    @staticmethod
    def getbase_URL():
        invoice_date = config.get('Invoice Detials', 'base_url')
        return invoice_date

    @staticmethod
    def getInvoice_Date():
        invoice_date = config.get('Invoice Detials', 'invoice_date')
        return invoice_date

    @staticmethod
    def getInvoice_Number():
        invoice_number = config.get('Invoice Detials', 'invoice_number')
        return invoice_number

    @staticmethod
    def getBooking_ID():
        booking_id = config.get('Invoice Detials', 'booking_id')
        return booking_id

    @staticmethod
    def getPayment_Mode():
        payment_mode = config.get('Invoice Detials', 'payment_mode')
        return payment_mode


    @staticmethod
    def getDescriptiomn():
        description = config.get('Invoice Detials', 'description')
        return description


    @staticmethod
    def getPrice():
        price = config.get('Invoice Detials', 'price')
        return price

    @staticmethod
    def getTotal_amt1():
        total_amt1 = config.get('Invoice Detials', 'total_amt1')
        return total_amt1

    @staticmethod
    def getTotal_paid_amt():
        total_paid_amt = config.get('Invoice Detials', 'total_paid_amt')
        return total_paid_amt

    @staticmethod
    def getPay_due_date():
        pay_due_date = config.get('Invoice Detials', 'pay_due_date')
        return pay_due_date

    @staticmethod
    def getPay_due():
        pay_due = config.get('Invoice Detials', 'pay_due')
        return pay_due

    @staticmethod
    def geTotal_amt2():
        total_amt2 = config.get('Invoice Detials', 'total_amt2')
        return total_amt2






