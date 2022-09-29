
import logging

class LogGen:
    @staticmethod
    def loggen():
        # getLogger() method takes the test case name as input
        logger = logging.getLogger("ZoomVenues")
        # FileHandler() method takes location and path of log file
        fileHandler = logging.FileHandler("C:\\Users\\GiTESH SONAR\\PycharmProjects\\ZoomVenues.Com\\Logs\\CorkageAllFlow.log")
        # Formatter() method takes care of the log file formatting
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        # addHandler() method takes fileHandler object as parameter
        logger.addHandler(fileHandler)
        # setting the logger level
        logger.setLevel(logging.INFO)
        print("--------------------------------------------------------------------")
        return logger






