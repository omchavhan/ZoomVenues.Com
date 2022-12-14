from selenium import webdriver
import pytest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     return driver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
       driver = webdriver.Chrome(executable_path="C:\\Users\\GiTESH SONAR\\PycharmProjects\\ZoomVenues.Com\\chromedriver.exe")
       driver.maximize_window()
       driver.implicitly_wait(4)
       print("Launching Chrome Browser.....")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:\\Users\\GiTESH SONAR\\PycharmProjects\\ZoomVenues.Com\\geckodriver.exe")
        driver.maximize_window()
        print("Launching Firefox Browser.....")
    else:
        driver = webdriver.Ie(executable_path="C:\\Users\\GiTESH SONAR\\PycharmProjects\\ZoomVenues.Com\\IEDriverServer.exe")    # Default browser run( not select any browser then)
    return driver

def pytest_addoption(parser):   #This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):   #This will return the browser value to setup methos
    return request.config.getoption("--browser")


################### Pytest Report #######################

# It is hook for Adding Environmet info to HTML.
def pytest_configure(config):
    config._metadata['Project Name'] = 'Zoomvenues.com'
    config._metadata['Model Name'] = 'Corkage Flow'
    config._metadata['Tester'] = 'Ombhagyesh Chavan'


#It is hook for delet/Modify Enviroment info to HTML Report

def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)
