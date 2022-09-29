import traceback

from selenium import webdriver
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

Base_URL="https://practice.automationbro.com/"
driver = selenium.webdriver.Chrome(executable_path="/chromedriver.exe")
def test_exceptions():
    driver.get(Base_URL)
    driver.maximize_window()
    driver.implicitly_wait(10)
    serch_suit()
    MyAccound_click()
    Shop_click()


def serch_suit():
    driver.implicitly_wait(10)
    serch_logo = driver.find_element_by_xpath("//*[@id='primary-menu']/li[8]/a/i")
    serch_logo.click()
    serchr_bar = driver.find_element_by_xpath("//*[@id='primary-menu']/li[8]/form/label/input")
    serchr_bar.send_keys("keybord")
    serchr_bar.send_keys(Keys.ENTER)

def MyAccound_click():
    driver.implicitly_wait(10)
    try:
        myaccount = driver.find_element_by_css_selector("li[id='menu-item-61'] a")
        assert myaccount.text == "My account"
        myaccount.click()
    except NoSuchElementException:
        print(traceback.format_exc())

def Shop_click():
    shop = driver.find_element_by_css_selector("li[id='menu-item-567'] a")
    # assert "Shop" in shop.text
    assert shop.text == "Shop"
    shop.click()
