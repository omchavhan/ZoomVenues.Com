import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


#Below All Xpath of Web element -

driver = webdriver.Chrome(executable_path="/chromedriver.exe")
Hotels_loc = "//*[@id='myTopnav']/div[1]/ul/li[2]/a"
Hotels_city_loc = "/html/body/div[2]/div/div[4]/div/form/div/input[3]"
Check_in_loc = "//span[@id='txtcimy']"
Check_in_date_loc = "22"
Select_adult_no_loc = "//a[@id='Adults_room_1_1_plus']"
Select_child_no_loc = "//a[@id='Children_room_1_1_plus']"
Room_Adult_Done_loc = "//a[normalize-space()='Done']"
Search_loc = "//input[@value='Search']"

def Hotels_click():
    hotels = driver.find_element_by_xpath(Hotels_loc)
    driver.execute_script("arguments[0].click();",hotels)


def Hotel_Locotion():
    # hotel_loc = driver.find_element_by_xpath(Hotels_city_loc)
    # hotel_loc.click()
    # time.sleep(3)
    # hotel_loc.send_keys("Pune")
    # time.sleep(3)
    # hotel_loc.send_keys(Keys.ENTER)

    driver.implicitly_wait(10)
    hotel_loc = driver.find_element_by_xpath(Hotels_city_loc)
    hotel_loc.send_keys("Pune")
    hotel_loc.send_keys(Keys.ENTER)

def Check_In_Date():
    # check_in_txtbox = driver.find_element_by_xpath(Check_in_loc)
    # check_in_txtbox.click()
    # time.sleep(3)
    # check_in_date = driver.find_element_by_link_text(Check_in_date_loc)
    # check_in_date.click()
    # time.sleep(3)
    driver.implicitly_wait(20)
    check_in = driver.find_element_by_xpath("/span[@id='txtcimy']")
    check_in.click()
    check_in_date = driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div[1]/table/tbody/tr[4]/td[6]/a")
    check_in_date.click()

def Check_Out_Date():
    check_in_txtbox = driver.find_element_by_link_text("26")
    check_in_txtbox.click()
    time.sleep(3)

def Room_Guest_Click():
    adult = driver.find_element_by_xpath(Select_adult_no_loc)
    adult.click()
    time.sleep(3)
    child = driver.find_element_by_xpath(Select_child_no_loc)
    child.click()
    time.sleep(3)
    Done = driver.find_element_by_xpath(Room_Adult_Done_loc)
    Done.click()

def Search_btn_click():
    search = driver.find_element_by_xpath(Search_loc)
    search.click()


def test_EsayMyTrip():
    BASE_URL = "https://www.easemytrip.com/"
    driver.get(BASE_URL)
    driver.implicitly_wait(20)
    driver.maximize_window()
    Hotels_click()
    # Hotel_Locotion()
    # time.sleep(3)
    Check_In_Date()
    # Check_Out_Date()
    # Room_Guest_Click()
    # Search_btn_click()
