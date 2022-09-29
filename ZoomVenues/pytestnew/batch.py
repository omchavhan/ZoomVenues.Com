from selenium import webdriver
import pytest


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def Fb_Sign_Up():
    global driver
    option = Options()
    option.add_argument("--disable-notifications--")
    driver = webdriver.Chrome(executable_path="/chromedriver.exe", chrome_options=option)
    driver.implicitly_wait(10)
    driver.get("https://www.amazon.in/")
    Action = ActionChains(driver)
    click = driver.find_element_by_css_selector("span[class='nav-line-2 ']")
    Action.move_to_element(click).perform()
    sign_in_btn = driver.find_element_by_xpath("//*[@id='nav-flyout-ya-signin']/a/span")
    sign_in_btn.click()


# def test_sign_click(Fb_Sign_Up):
#     driver.implicitly_wait(10)
#     Action = ActionChains(driver)
#     click = driver.find_element_by_css_selector("span[class='nav-line-2 ']")
#     Action.move_to_element(click).perform()
#     sign_in_btn = driver.find_element_by_xpath("//*[@id='nav-flyout-ya-signin']/a/span")
#     sign_in_btn.click()

@pytest.mark.skip
def test_sign_in_Id(Fb_Sign_Up):
    driver.implicitly_wait(10)
    # wait = WebDriverWait(driver, 10)
    # id = wait.until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, '#ap_email')))
    id= driver.find_element_by_css_selector("#ap_email")
    id.send_keys("919158333486")

@pytest.mark.skip
def test_continue_btn_click(Fb_Sign_Up):
    driver.implicitly_wait(10)
    btn_click = driver.find_element_by_xpath("//input[@id='continue']")
    btn_click.click()

def test_close(Fb_Sign_Up):
    driver.quit()