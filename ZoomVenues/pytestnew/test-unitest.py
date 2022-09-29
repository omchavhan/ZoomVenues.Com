from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Bellow all path of web elements -
# driver = webdriver.Chrome(executable_path="C:\\Users\\GiTESH SONAR\\PycharmProjects\\GoogleAuto\\chromedriver.exe")
#
#
#
#
# def test_web():
#     BASE_URL = "https://www.yatra.com/"
#     driver.get(BASE_URL)
#     driver.maximize_window()
#     driver.quit()
#

from selenium import webdriver
import pytest


@pytest.fixture
def input_value():
   input = 39
   return input
