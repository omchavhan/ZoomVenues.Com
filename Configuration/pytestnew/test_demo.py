import time
import pytest

from selenium import webdriver

@pytest.fixture
def setup():
    global driver
    driver = webdriver.Chrome(executable_path="/chromedriver.exe")
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    yield
    driver.find_element_by_xpath("//button[contains(text(),'लॉग इन कर')]").submit()
    time.sleep(3)
    driver.quit()

def test_facebooklogin1(setup):
    driver.find_element_by_xpath("//input[@id='email]").send_keys("ombhagyesh")
    driver.find_element_by_xpath("//input[@id='pass']").send_keys("omworld01")

@pytest.mark.xfail
def test_facebooklogin2(setup):
    driver.find_element_by_xpath("//input[@id='email']").send_keys("er.gitesh")
    driver.find_element_by_xpath("//input[@id='pass']").send_keys("parentsl0ve")






