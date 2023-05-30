from selenium import webdriver
import self as self
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
import self as self


# Bellow Web Elements


driver = webdriver.Chrome(executable_path="C:\\Users\\ergit\\PycharmProjects\\ZoomVenues.Com\\Drivers\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="/geckodriver.exe")
zoomvenuesurl = "http://zoomvenues.info/"

driver.get(zoomvenuesurl)


def test_admin_page():
    driver.set_page_load_timeout(10)
    driver.maximize_window()
    driver.get(zoomvenuesurl)