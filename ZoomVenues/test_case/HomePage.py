


# -------------------------------------------------------------------------------
# driver.get("https://zoomvenues.info")
# driver.maximize_window()
# driver.implicitly_wait(20)
# parent_page = driver.current_window_handle
# venues_signup = driver.find_element_by_xpath("//*[@id='main']/header/div[2]/a").click()
# child_page = driver.window_handles
# for handle in child_page:
#     if handle != parent_page:
#         driver.switch_to.window(handle)
#         close_screen = driver.find_element_by_xpath("//a[@href='#close-modal']").click()
#         mail_id = driver.find_element_by_css_selector("#user")
#         # mail_id.send_keys("ombhagyeshchavhan1@gmail.com")
#         mail_id.send_keys("hisham.kassem@crowneplazadubai.com")
#         time.sleep(2)
#         password = driver.find_element_by_css_selector("#password")
#         password.send_keys("12345678")
#         time.sleep(2)
#         login = driver.find_element_by_css_selector("#form-submit").click()
#
# time.sleep(3)
# driver.implicitly_wait(20)
# click_userlist = driver.find_element_by_xpath("(//*[@class='nav-link'])[7]").click()
# time.sleep(3)
#
# driver.implicitly_wait(20)
# click_add_user = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/newuser/create']")
# driver.execute_script("arguments[0].click();", click_add_user)
# time.sleep(2)
# click_f_name = driver.find_element_by_xpath("//*[@name='first_name']")
# click_f_name.send_keys("om")
# click_l_name = driver.find_element_by_css_selector("#last_name")
# click_l_name.send_keys("chavan")
# time.sleep(2)
# click_contact = driver.find_element_by_css_selector("#AE").click()
# pin_code_india = driver.find_element_by_xpath("(//span[@class='iti__country-name'][contains(text(),'India (भारत)')])[1]").click()
# contact = driver.find_element_by_xpath("//*[@name='contact_number']")
# contact.send_keys("9158333486")
# time.sleep(1)
# click_mail = driver.find_element_by_xpath("(//input[@id='email'])[1]")
# click_mail.send_keys("omworld01@gmail.com")
# click_pwd = driver.find_element_by_css_selector("#password")
# click_pwd.send_keys("1234567890")
# click_comb_pwd = driver.find_element_by_css_selector("#confirm_password")
# click_comb_pwd.send_keys("1234567890")
# click_user_role = driver.find_element_by_xpath("//*[@name='user_role_id']")
# dropdown_user_role = Select(click_user_role)
# dropdown_user_role.select_by_index(1)
# click_status = driver.find_element_by_css_selector("select[name='user_status']")
# print(click_status.text)
# dropdown_status = Select(click_status)
# dropdown_status.select_by_index(1)
# time.sleep(2)
# click_venues = driver.find_element_by_name("venues[]").text
# print(click_venues)


# -------------------------------------------------------------------------------------------


import time

from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/chromedriver.exe")
zoomvenues_url = "https://zoomvenues.info/"
groww = "https://groww.in/"


# driver.implicitly_wait(20)
# driver.maximize_window()
# driver.get("https://demo.automationtesting.in/Datepicker.html")
#
# caleder_click = driver.find_element_by_css_selector(".imgdp").click()
# next = driver.find_elements_by_link_text("Next")
# for x in next:
#     print(x.text)







from selenium.webdriver import ActionChains

def case():
    driver.maximize_window()

    google_searbar = driver.find_element_by_xpath("//*[@name='q']")
    google_searbar.send_keys("Ind")
    time.sleep(5)
    action_auto = ActionChains(driver)
    action_auto.send_keys(google_searbar, Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()  # only single dowm and click
    # action_auto.send_keys(google_searbar,Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()  # two time down and click



def case2():
    driver.maximize_window()
    que = driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys("Software")
    time.sleep(3)
    que.send_keys(Keys.ARROW_DOWN)
    # que.send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    que.send_keys(Keys.RETURN)


def case3():
    driver.maximize_window()

    driver.get('http://google.com')
    element = driver.find_element_by_link_text('About')
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    time.sleep(10)  # Pause to allow you to inspect the browser.

    driver.quit()

def datapicker():

    driver.maximize_window()
    click_date = driver.find_element_by_xpath("//*[@id='datepicker1']").click()

    i = 0
    while i == 0:
        title1 = driver.find_element_by_xpath("//*[@class='ui-datepicker-month']").text
        title2 = driver.find_element_by_xpath("//*[@class='ui-datepicker-year']").text
        montyear = title1 + " " + title2
        if montyear != "February 2023" or montyear == "February 2023":
            driver.find_element_by_xpath("//*[@class='ui-icon ui-icon-circle-triangle-e']").click()
        else:
            break

    select_date = driver.find_element_by_xpath("//a[normalize-space()='14']").click()



def case4():
    driver.maximize_window()
    venue_type = driver.find_element_by_class_name("form-check-input venueTypes").text
    print(venue_type)


def right_click():
    driver.maximize_window()
    search = driver.find_element_by_css_selector("input[title='Search']")
    action_a = ActionChains(driver)
    action_a.context_click(search).perform()

def keyup_keydown():
    driver.maximize_window()
    user_id = driver.find_element_by_css_selector("#email")
    user_id.send_keys("testing")
    act = ActionChains(driver)
    act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
    act.send_keys(Keys.TAB).perform()
    act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    act.send_keys(Keys.ENTER).perform()


def double_click():
    driver.implicitly_wait(20)
    act = ActionChains(driver)
    alert = driver.find_element_by_xpath("//*[@name='alert']")
    act.double_click(alert).perform()
    time.sleep(2)
    text = driver.switch_to.alert.text
    print(text)


def drag_and_drop():
    driver.implicitly_wait(20)
    # letter_A = driver.find_element_by_xpath("//*[@id='sortable']//li[text()='A']")
    # letter_C = driver.find_element_by_xpath("//*[@id='sortable']//li[text()='C']")
    # act = ActionChains(driver)
    # # act.click_and_hold(letter_A).move_to_element(letter_C).click().perform()
    # act.drag_and_drop(letter_A,letter_C).perform()

    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame']"))
    ele1 = driver.find_element_by_id("draggable")
    ele2 = driver.find_element_by_id("droppable")
    ActionChains(driver).drag_and_drop(ele1, ele2).perform()


def screen_shot():
    driver.implicitly_wait(20)
    day = driver.find_element_by_xpath("//*[@id='df']")



def test_case():
    # driver.get("https://demo.automationtesting.in/Datepicker.html")
    # driver.get("https://www.google.com/")
    # driver.get("http://vendor.zoomvenues.info/admin/venues/edit/44")
    # driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
    # driver.get("https://jqueryui.com/droppable/")
    driver.get("https://www.facebook.com/r.php?locale=mr_IN&display=page")
    driver.maximize_window()
    # case()
    # case3()
    # datapicker()
    # case4()
    # keyup_keydown()
    # right_click()
    # double_click()
    # drag_and_drop()
    screen_shot()
#----------------------------  Alert popup with ok button -----------------
# driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
# driver.implicitly_wait(20)
# act = ActionChains(driver)
# alert = driver.find_element_by_xpath("//*[@name='alert']")
# act.double_click(alert).perform()
# time.sleep(2)
# text = driver.switch_to.alert.text
# print(text)
# driver.switch_to.alert.accept()

#----------------------------  Alert popup with accept or dismiss -----------------
# driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
# driver.maximize_window()
# driver.implicitly_wait(20)
#
# alert2 = driver.find_element_by_css_selector("[value='Confirmation Box']").click()
# time.sleep(2)
# driver.switch_to.alert.dismiss()