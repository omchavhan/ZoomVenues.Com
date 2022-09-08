import time

import selenium.webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#all path of web-elements:-
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

option=Options()
option.add_argument("--disable-notifications--")
driver=selenium.webdriver.Chrome(executable_path="/chromedriver.exe", chrome_options=option)
BASE_URl="https://www.easemytrip.com/"
Aler_URL="https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt"
DropDown_URL="https://www.globalsqa.com/demo-site/select-dropdown-menu/"
Make_mytrip_URL="https://www.makemytrip.com/"





def mouse_over():
    driver.implicitly_wait(10)
    Action = ActionChains(driver)
    more=driver.find_element_by_css_selector("body > div:nth-child(5) > div:nth-child(8) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(10) > a:nth-child(1)")
    Action.move_to_element(more).perform()
    offers= driver.find_element_by_xpath("//div[@id='divnewlogin']//div[@class='emt_nav']//a[2]").click()
    driver.back()

def multi_window_handle():
    driver.implicitly_wait(10)
    Home_Page=driver.current_window_handle
    New_user_offer= driver.find_element_by_css_selector("body > div:nth-child(11) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(6) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)").click()
    New_user_offer_page=driver.window_handles

    for user_page in New_user_offer_page:
        if user_page != Home_Page:
            driver.switch_to.window(user_page)
            booking_fight=driver.find_element_by_link_text("booking flight tickets").click()


    switch_to_home_page=driver.switch_to.window(Home_Page)


def Auto_suggestion_One_way():
    From = driver.find_element_by_css_selector("#FromSector_show")
    From.click()
    From.send_keys("Pune(PNQ)")
    From.send_keys(Keys.ENTER)
    To = driver.find_element_by_css_selector("#Editbox13_show")
    To.click()
    To.send_keys("Mumbai(BOM)")
    To.send_keys(Keys.ENTER)
    Date_from= driver.find_element_by_css_selector("#ddate").click()
    Date_from_select= driver.find_element_by_css_selector("body > form:nth-child(8) > div:nth-child(9) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(7) > ul:nth-child(1) > li:nth-child(5)").click()
    Date_to= driver.find_element_by_css_selector("#rdate").click()
    Date_to_select = driver.find_element_by_css_selector("body > form:nth-child(8) > div:nth-child(9) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(2)").click()
    Search = driver.find_element_by_css_selector("input[onclick='SearchFlightWithArmy();']").click()


def Alert():
    driver.implicitly_wait(10)
    Alert = driver.switch_to.frame("iframeResult")
    Try = driver.find_element_by_xpath("/html/body/button")
    Try.click()
    driver.switch_to.alert.send_keys("om sonar")
    driver.switch_to.alert.accept()


# def DropDown():
#     driver.implicitly_wait(10)
#     City = driver.find_element_by_css_selector("div[class='single_tab_div resp-tab-content resp-tab-content-active'] p select")
#     City.click()
#     dropdown=Select(City)
#     dropdown.select_by_value("AFG")
#
#
# def finds_elements():
#     wait=WebDriverWait(driver,10)
#     login = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='SW']/div[1]/div[1]/ul/li[3]"))).click()
#     driver.implicitly_wait(10)
#     Chater = driver.find_elements_by_link_text("Charter Flights")
#     for x in Chater:
#         print(x.text)
#         if x.text=="Charter Flights":
#             x.click()
#


def test_modules():
    driver.get(BASE_URl)
    driver.maximize_window()
    mouse_over()
    time.sleep(3)
    # driver.quit()