import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Below are the xpaths for the Web Elements.
driver = webdriver.Chrome(executable_path="/chromedriver.exe")
login_link_loc = "Sign in"
user_id_loc = "//input[@id='ap_email']"
continue_button_loc = "//input[@id='continue']"
password_loc = "//input[@id='ap_password']"
login_button_loc = "//input[@id='signInSubmit']"
search_textbox_loc = "//input[@id='twotabsearchtextbox']"
search_bar_loc = "//input[@id='nav-search-submit-button']"
product_loc = "//div[@data-component-type='sp-sponsored-result']//span[@class='a-size-medium a-color-base a-text-normal'][contains(text(),'New Apple Watch Series 6 (GPS + Cellular, 44mm) - ')]"
buy_product_loc = "//input[@id='buy-now-button']"
address_loc = "/html/body/div[5]/div[2]/div[1]/form/div/div[1]/div[2]/span/a"

def enter_username(username):
    user = driver.find_element_by_xpath(user_id_loc)
    user.send_keys(username)

def click_continue():
    continue_button = driver.find_element_by_xpath(continue_button_loc)
    continue_button.click()

def enter_password(password):
    password_in = driver.find_element_by_xpath(password_loc)
    password_in.send_keys(password)

def click_login():
    login = driver.find_element_by_xpath(login_button_loc)
    login.click()

def search_product(product):
    search_textbox = driver.find_element_by_xpath(search_textbox_loc)
    search_textbox.send_keys(product)

def search_button_click():
    search_button = driver.find_element_by_xpath(search_bar_loc)
    search_button.click()

def select_product():
    product = driver.find_element_by_xpath(product_loc)
    product.click()

def test_buy_product():

    BASE_URL = "https://www.amazon.in/"
    driver.get(BASE_URL)
    driver.maximize_window()
    parent = driver.current_window_handle

    # signin-in to Amazon account
    sign_in_button = driver.find_element_by_link_text(login_link_loc)
    sign_in_button.click()
    enter_username("919158333486")
    click_continue()
    enter_password("omworld")
    click_login()
    time.sleep(5)
    search_product("apple watch 6")
    search_button_click()
    select_product()
    time.sleep(3)

    child = driver.window_handles
    for handle in child:
        if handle != parent:
            driver.switch_to.window(handle)
            buy = driver.find_element_by_xpath(buy_product_loc).click()
            address = driver.find_element_by_xpath(address_loc).click()
            time.sleep(5)
            break
    time.sleep(6)






