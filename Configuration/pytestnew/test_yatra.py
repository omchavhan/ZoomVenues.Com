from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver import ActionChains
import time

##Below are the xpath of web-element.

More_btn_loc= "//span[@class='more-arr']"
Trains_loc = "//span[normalize-space()='Trains']"
Flight_Booking_loc = "//span[@class='demo-icon icon-flights']"
One_way_Booking_loc = "//a[@title='One Way']"
Depart_form_loc = "//input[@id='BE_flight_origin_city']"
Going_to_loc = "//input[@id='BE_flight_arrival_city']"
Departure_Date_loc ="//input[@id='BE_flight_origin_date']"
Depature_Selecte_date_loc = "//input[@id='BE_flight_origin_date']"
Depature_date_loc = "//td[@id='23/07/2021']"
Return_Selected_date_loc = "//input[@id='BE_flight_arrival_date']"
Return_date_loc = "//td[@id='26/07/2021']"
Travellers_loc = "//span[@class='txt-ellipses flight_passengerBox travellerPaxBox']"
Adult_people_select_loc = "//*[@id='BE_flight_passengerBox']/div[1]/div[1]/div/div/span[2]"
Child_Select_loc = "//*[@id='BE_flight_passengerBox']/div[1]/div[2]/div/div/span[2]"
Infant_select_loc = "//*[@id='BE_flight_passengerBox']/div[1]/div[3]/div/div/span[2]"
Travelling_BussinesClass_loc = "//*[@id='flight_class_select_child']/ul/li[3]"
Search_Flight_loc = "//*[@id='BE_flight_flsearch_btn']"
Select_Flight_loc = "//*[@id='fare-PNQDEL6285220210723_GALDOM']/div[2]"
Booking_Now_loc = "//*[@id='Flight-APP']/section/section[3]/div/div[2]/div[2]/button"

@pytest.fixture
def comman():
    global driver
    driver = webdriver.Chrome(executable_path="/chromedriver.exe")
    BASE_URL = "https://www.yatra.com/"
    driver.get(BASE_URL)
    driver.implicitly_wait(20)
    driver.maximize_window()

def test_Flight_Booking(comman):
    flight = driver.find_element_by_xpath("//span[@class='demo-icon icon-flights']")
    flight.click()

def test_One_way_Booking(comman):
    one_way = driver.find_element_by_xpath(One_way_Booking_loc)
    one_way.click()

def Depart_from_Booking():
    Depart_form = driver.find_element_by_xpath(Depart_form_loc)
    Depart_form.click()
    time.sleep(3)
    Depart_form.send_keys("Pune")
    time.sleep(3)
    Depart_form.send_keys(Keys.ENTER)

def Going_to_Booking():
    Going_to = driver.find_element_by_xpath(Going_to_loc)
    Going_to.click()
    time.sleep(3)
    Going_to.send_keys("New Delhi")
    time.sleep(3)
    Going_to.send_keys(Keys.ENTER)

def Departure_date_Booking():
    Depature_Selecte_date = driver.find_element_by_xpath(Depature_Selecte_date_loc)
    Depature_Selecte_date.click()
    time.sleep(2)
    Depature_date = driver.find_element_by_xpath(Depature_date_loc).click()
    time.sleep(2)

def Return_date_Booking():
    Return_date = driver.find_element_by_xpath(Return_Selected_date_loc)
    Return_date.click()
    time.sleep(2)
    Return_date_sel = driver.find_element_by_xpath(Return_date_loc).click()
    time.sleep(2)

# @pytest.mark.traveller
def Travellers_people_Booking():
    Travellers_people = driver.find_element_by_xpath("//*[@id='BE_flight_paxInfoBox']/span").click()
    # time.sleep(2)
    Adult_people_select = driver.find_element_by_xpath(Adult_people_select_loc).click()
    # time.sleep(2)
    Child_select = driver.find_element_by_xpath(Child_Select_loc).click()
    # time.sleep(2)
    Infant_select = driver.find_element_by_xpath(Infant_select_loc).click()

def Selecting_travel_class_Booking():
    Selecting_class = driver.find_element_by_xpath(Travelling_BussinesClass_loc)
    Selecting_class.click()

def Search_Flight_Booking():
    search_flight = driver.find_element_by_xpath(Search_Flight_loc)
    search_flight.click()

# def Select_Flight_Booking():
#     select_flight= driver.find_element_by_xpath(Select_Flight_loc)
#     select_flight.click()

def Book_Now_Booking():
    Book_Now = driver.find_element_by_xpath(Booking_Now_loc)
    Book_Now.click()

def More_Click():
    More_btn = driver.find_element_by_xpath(More_btn_loc)
    Action_more = ActionChains(driver)
    Action_more.move_to_element(More_btn).perform()
    # time.sleep(3)
    Train = driver.find_element_by_xpath(Trains_loc).click()


# def test_Booking():
#     BASE_URL = "https://www.yatra.com/"
#
#     driver.get(BASE_URL)
#     driver.maximize_window()
#     driver.implicitly_wait(20)
#
#     More_Click()
#     driver.back()
#     time.sleep(2)
#     Flight_Booking()
#     One_way_Booking()
#     Depart_from_Booking()
#     time.sleep(3)
#     Going_to_Booking()
#     time.sleep(5)
#     Departure_date_Booking()
#     Return_date_Booking()
#     Travellers_people_Booking()
#     Selecting_travel_class_Booking()
#     Search_Flight_Booking()
#     #Select_Flight_Booking()
#     Book_Now_Booking()



