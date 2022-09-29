
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

# All Paths of web elements :-

BASE_URl = "https://www.hdfcbank.com/"
NRI_loc = "//*[@id='main']/div[2]/header/div/div/div/div/div[2]/div/div[3]/div/div/div/div/div[1]/div[2]/ul[1]/li[2]/a"
Dropdown_select_proct_type_loc = "Select Product Type"
Search_bar_loc = "//*[@id='custom-search-input']/div/div/div/div/input"
close_serch_bar_loc ="sf-closebutton"
login_btn_loc = "//button[@class='btn btn-primary login-btn hide-in-mobileApp ng-scope']"
personal_login_loc = "//input[@value='6']"
login_loc = "//a[@class='btn-primary login-url']"
pay_loc ="//li[@class='level-1 sub-section-5 dropdown megamenu-fw']//a[@title='Pay']"
electricity_bill_loc = "//body[1]/div[1]/div[1]/div[2]/div[13]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[2]/ul[1]/li[3]/ul[1]/li[1]/a[1]/span[1]"


# Browser notification alert : -
optional = webdriver.ChromeOptions()
optional.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
driver = webdriver.Chrome(executable_path="/chromedriver.exe",
                          chrome_options=optional)

def Droptown_select_type():
    dropdown = driver.find_element_by_link_text(Dropdown_select_proct_type_loc)
    dd = Select(dropdown)
    dd.select_by_visible_text("Cards")

def Click_NRI():
    click_nri = driver.find_element_by_xpath(NRI_loc)
    click_nri.click()

def Click_search_bar():
    serch_bar = driver.find_element_by_xpath(Search_bar_loc).click()
    time.sleep(3)
    close_search = driver.find_element_by_class_name(close_serch_bar_loc).click()

def Click_login_btn():
    login_btn = driver.find_element_by_xpath(login_btn_loc).click()
    time.sleep(3)
    personal_login = driver.find_element_by_xpath(personal_login_loc).click()
    time.sleep(2)
    login = driver.find_element_by_xpath(login_loc).click()

def Click_Pay_bar():
    pay_bar = driver.find_element_by_xpath(pay_loc)
    action = ActionChains(driver)
    action.move_to_element(pay_bar).perform()
    time.sleep(3)
    driver.find_element_by_xpath(electricity_bill_loc).click()


def test_bom_case():
    driver.get(BASE_URl)
    driver.maximize_window()
    Click_Pay_bar()

