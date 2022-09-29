import time
import pytest
from selenium import webdriver

# @pytest.mark.skipif()         #-------------- use if condion <,>,=...use
@pytest.mark.smoke
def test_web():
    global options
    options = webdriver.Chrome(executable_path="/chromedriver.exe")
    options.get("http://testautomationpractice.blogspot.com/")
    options.maximize_window()

@pytest.mark.skip             #----------skip the this method
def test_login():
    options.execute_script("window.scrollTo(0,500)")
    time.sleep(3)
    options.switch_to.frame(0)
    options.find_element_by_xpath("//input[@id='RESULT_FileUpload-10']").send_keys("C:\\Users\\GiTESH SONAR\\Desktop\\Automation\\Resume\\ombhagyesh-resume.pdf")
    time.sleep(4)


def test_stop():
    options.quit()



