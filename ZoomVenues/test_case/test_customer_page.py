import time
from telnetlib import EC
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import pytest


# Web Elements Path -
from selenium.webdriver.support.wait import WebDriverWait




driver = webdriver.Chrome(executable_path="C:\\Users\\GiTESH SONAR\\PycharmProjects\\ZoomVenues.Com\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="/geckodriver.exe")
zoomvenuesurl = "https://zoomvenues.info/"
event_venues_css = "body > div:nth-child(3) > header:nth-child(1) > div:nth-child(12) > nav:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)"
banquets_xpath = "//*[@id='main']/header/div[9]/nav/ul/li[1]/ul/li[1]/a"
your_name_css = "div[id='venuemodalen2'] input[placeholder='Your Name *']"
mail_id_css = "div[id='venuemodalen2'] input[placeholder='Email Address*']"
phone_no_css = "div[id='venuemodalen2'] input[placeholder='Phone Number *']"
select_event_type_css = "div[id='venuemodalen2'] select[name='eventtype']"
select_date_css = "body > div:nth-child(3) > div:nth-child(13) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > fieldset:nth-child(2) > div:nth-child(6) > input:nth-child(2)"
time_css= "input[class='timepicker1']"
no_of_people_css = "div[id='venuemodalen2'] input[placeholder='No of Peoples *']"
select_budget_css = "div[id='venuemodalen2'] select[class='budget']"
add_req_css = "div[id='venuemodalen2'] textarea[placeholder='Additional Requirement:']"
acc_term_condition_css = "body > div:nth-child(3) > div:nth-child(13) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(3) > label:nth-child(1) > input:nth-child(1)"
submit_css = "body > div:nth-child(3) > div:nth-child(13) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(4) > button:nth-child(1)"
sign_in_xpath = "//*[@id='main']/header/div[5]"
register_btn_css = ".registerLink"
f_name_css = "#register_first_name"
l_name_css = "#register_last_name"
mobile_reg_css = "#register_mobile_no"
email_id_css = "#register_email"
conf_password_id = "register_confirm_password"
password_id = "register_password"
register_acc_xpath = "//*[@id='register-btn']"
log_in_xpath = "//button[@id='login-btn']"
# acc_condition_css = "body > div:nth-child(3) > div:nth-child(13) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(3) > label:nth-child(1) > span:nth-child(3) > a:nth-child(1)"


@pytest.mark.parametrize("fname,lname,emailid,mob_reg,pass_reg,con_reg",[("om"),("chavhan"),("omworld01"),("9158333486"),("omworld01"),("omworld01@")])
def sign_in(fname,lname,emailid,mob_reg,pass_reg,con_reg):
    driver.implicitly_wait(20)
    sign_in_link = driver.find_element_by_xpath(sign_in_xpath).click()
    register_link = driver.find_element_by_css_selector(register_btn_css).click()
    f_name = driver.find_element_by_css_selector(f_name_css)
    f_name.send_keys(fname)
    l_name = driver.find_element_by_css_selector(l_name_css)
    l_name.send_keys(lname)
    email_id = driver.find_element_by_css_selector(email_id_css)
    email_id.send_keys(emailid)
    mobile_reg = driver.find_element_by_css_selector(mobile_reg_css)
    mobile_reg.send_keys(mob_reg)
    password_reg = driver.find_element_by_id(password_id)
    password_reg.send_keys(pass_reg)
    conf_password = driver.find_element_by_id(conf_password_id)
    conf_password.send_keys(con_reg)
    register_acc = driver.find_element_by_xpath(register_acc_xpath).click()

def login():
    driver.implicitly_wait(20)
    sign_in_link = driver.find_element_by_xpath(sign_in_xpath).click()
    register_link = driver.find_element_by_css_selector(register_btn_css).click()
    login_link = driver.find_element_by_css_selector(".loginLink").click()
    login_id = driver.find_element_by_css_selector("#login_email")
    login_id.send_keys("omworld01@gmail.com")
    login_pass = driver.find_element_by_css_selector("#login_password")
    login_pass.send_keys("omworld01")
    rem_me = driver.find_element_by_css_selector("#check-a3").click()
    log_in = driver.find_element_by_xpath(log_in_xpath).click()
    home_page1 = driver.find_element_by_xpath("//img[@src='http://zoomvenues.info/images/logo.png']").click()


# ------ Event Follow-------------
@pytest.fixture
def make_enquiry():
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("om chavhan")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("9158333486")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("05-07-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("2:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("nothing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()
    zoomvenues = driver.find_element_by_xpath("//img[@src='http://zoomvenues.info/images/logo.png']").click()


def event_venues_Banquets_test(make_enquiry):
    driver.implicitly_wait(20)
    event_venues = driver.find_element_by_xpath("//a[normalize-space()='Event Venues']")
    action = ActionChains(driver)
    action.move_to_element(event_venues).perform()
    banquets_c = driver.find_element_by_xpath("(//a[contains(text(),'Banquets')])[1]")
    driver.execute_script("arguments[0].click();", banquets_c)
    time.sleep(3)

def event_venues_Party_Halls_test():
    driver.implicitly_wait(20)
    event_venues = driver.find_element_by_xpath("//a[normalize-space()='Event Venues']")
    action = ActionChains(driver)
    action.move_to_element(event_venues).perform()
    party_halls = driver.find_element_by_xpath("//*[@id='main']/header/div[9]/nav/ul/li[1]/ul/li[2]/a")
    driver.execute_script("arguments[0].click();", party_halls)
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("om chavhan 11")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("1234567890")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("01-08-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("3:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("testing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()


def event_venues_Convention_Centre_test():
    driver.implicitly_wait(20)
    event_venues = driver.find_element_by_xpath("//a[normalize-space()='Event Venues']")
    action = ActionChains(driver)
    action.move_to_element(event_venues).perform()
    Convention_Centre = driver.find_element_by_xpath("//a[normalize-space()='Convention Centre']")
    driver.execute_script("arguments[0].click();", Convention_Centre)
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("om chavhan 2A")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("9158333486")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("03-09-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("2:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("nothing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()


def event_venues_Farm_Houses_test():
    driver.implicitly_wait(20)
    event_venues = driver.find_element_by_xpath("//a[normalize-space()='Event Venues']")
    action = ActionChains(driver)
    action.move_to_element(event_venues).perform()
    Farm_Houses = driver.find_element_by_xpath("//a[normalize-space()='Farm Houses']")
    driver.execute_script("arguments[0].click();", Farm_Houses)
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("om chavhan")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("9158333486")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("05-07-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("2:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("nothing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()




def event_venues_Roof_Tops_test():
    driver.implicitly_wait(20)
    event_venues = driver.find_element_by_xpath("//a[normalize-space()='Event Venues']")
    action = ActionChains(driver)
    action.move_to_element(event_venues).perform()
    Roof_Tops = driver.find_element_by_xpath("//a[normalize-space()='Roof Tops']")
    driver.execute_script("arguments[0].click();", Roof_Tops)
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("om chavhan")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("9158333486")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("05-07-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("2:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("nothing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()


def event_venues_Auditoriums_test():
    driver.implicitly_wait(20)
    event_venues = driver.find_element_by_xpath("//a[normalize-space()='Event Venues']")
    action = ActionChains(driver)
    action.move_to_element(event_venues).perform()
    Auditoriums= driver.find_element_by_xpath("//a[normalize-space()='Auditoriums']")
    driver.execute_script("arguments[0].click();", Auditoriums)
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("om chavhan")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("9158333486")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("05-07-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("2:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("nothing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()


def event_venues_Yacht_test():
    driver.implicitly_wait(20)
    event_venues = driver.find_element_by_xpath("//a[normalize-space()='Event Venues']")
    action = ActionChains(driver)
    action.move_to_element(event_venues).perform()
    Yacht= driver.find_element_by_xpath("//a[normalize-space()='Yacht']")
    driver.execute_script("arguments[0].click();", Yacht)
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("om chavhan")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("9158333486")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("04-08-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("2:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("nothing testing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()



def event_venues_Palace_test():
    driver.implicitly_wait(20)
    event_venues = driver.find_element_by_xpath("//a[normalize-space()='Event Venues']")
    action = ActionChains(driver)
    action.move_to_element(event_venues).perform()
    Palace= driver.find_element_by_xpath("//a[normalize-space()='Palace']")
    driver.execute_script("arguments[0].click();", Palace)
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("om chavhan")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("9158333486")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("05-07-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("2:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("nothing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()



def event_venues_Sports_Complex_test():
    driver.implicitly_wait(20)
    event_venues = driver.find_element_by_xpath("//a[normalize-space()='Event Venues']")
    action = ActionChains(driver)
    action.move_to_element(event_venues).perform()
    Sports_Complex = driver.find_element_by_xpath("//a[normalize-space()='Sports Complex']")
    driver.execute_script("arguments[0].click();", Sports_Complex)
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("om chavhan")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("9158333486")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("05-07-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("2:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("nothing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()


def event_venues_Open_air_places_test():
    driver.implicitly_wait(20)
    event_venues = driver.find_element_by_xpath("//a[normalize-space()='Event Venues']")
    action = ActionChains(driver)
    action.move_to_element(event_venues).perform()
    Open_air_places  = driver.find_element_by_xpath("//a[normalize-space()='Open air places']")
    driver.execute_script("arguments[0].click();", Open_air_places)
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("om chavhan")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("9158333486")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("05-07-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("2:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("nothing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()


# ------ work_venues Follow-------------

def work_venues_and_business_cent_test():
    driver.implicitly_wait(20)
    work_venues = driver.find_element_by_css_selector("body > div:nth-child(3) > header:nth-child(1) > div:nth-child(12) > nav:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)")
    action = ActionChains(driver)
    action.move_to_element(work_venues).perform()
    business_center = driver.find_element_by_xpath("//a[contains(text(),'Business Centres')]").click()
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("om chavhan")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("9158333486")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("09-07-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("2:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("nothing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Jihaan - Shangri-La Hotel Dubai']"))).click()



def work_venues_and_co_work_desk_test():
    driver.implicitly_wait(20)
    work_venues = driver.find_element_by_css_selector("body > div:nth-child(3) > header:nth-child(1) > div:nth-child(12) > nav:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)")
    action = ActionChains(driver)
    action.move_to_element(work_venues).perform()
    co_work_desk = driver.find_element_by_xpath("//a[contains(text(),'Co-Work Desks')]").click()
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("om chavhan")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("9158333486")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("05-07-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("2:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("nothing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()


def work_venues_and_Conference_Rooms_test():
    driver.implicitly_wait(20)
    work_venues = driver.find_element_by_css_selector("body > div:nth-child(3) > header:nth-child(1) > div:nth-child(12) > nav:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)")
    action = ActionChains(driver)
    action.move_to_element(work_venues).perform()
    Conference_Rooms = driver.find_element_by_xpath("//a[contains(text(),'Conference Rooms')]").click()
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("om chavhan")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("9158333486")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("05-07-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("2:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("nothing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()

def work_venues_and_Meeting_Rooms_test():
    driver.implicitly_wait(20)
    work_venues = driver.find_element_by_css_selector("body > div:nth-child(3) > header:nth-child(1) > div:nth-child(12) > nav:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)")
    action = ActionChains(driver)
    action.move_to_element(work_venues).perform()
    Meeting_Rooms = driver.find_element_by_xpath("//a[contains(text(),'Meeting Rooms')]").click()
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("om chavhan")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("9158333486")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("05-07-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("2:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("nothing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()



def work_venues_and_Study_Rooms_test():
    driver.implicitly_wait(20)
    work_venues = driver.find_element_by_css_selector("body > div:nth-child(3) > header:nth-child(1) > div:nth-child(12) > nav:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)")
    action = ActionChains(driver)
    action.move_to_element(work_venues).perform()
    Study_Rooms = driver.find_element_by_xpath("//a[contains(text(),'Meeting Rooms')]").click()
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("om chavhan")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("9158333486")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("05-07-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("2:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("nothing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()


def work_venues_and_Uni_halls_test():
    driver.implicitly_wait(20)
    work_venues = driver.find_element_by_css_selector("body > div:nth-child(3) > header:nth-child(1) > div:nth-child(12) > nav:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)")
    action = ActionChains(driver)
    action.move_to_element(work_venues).perform()
    Uni_halls = driver.find_element_by_xpath("//a[normalize-space()='Uni Halls']").click()
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("om chavhan")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("9158333486")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("05-07-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("2:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("nothing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()


def work_venues_and_Seminar_auditoriums_test():
    driver.implicitly_wait(20)
    work_venues = driver.find_element_by_css_selector("body > div:nth-child(3) > header:nth-child(1) > div:nth-child(12) > nav:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)")
    action = ActionChains(driver)
    action.move_to_element(work_venues).perform()
    Seminar_auditoriums = driver.find_element_by_xpath("//a[normalize-space()='Seminar Auditoriums']").click()
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("om chavhan")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("9158333486")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("05-07-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("2:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("nothing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()



# ------- Services follow ----------

def services_and_Event_Management():
    driver.implicitly_wait(20)
    services = driver.find_element_by_xpath("//a[@href='#'][normalize-space()='Services']")
    action = ActionChains(driver)
    action.move_to_element(services).perform()
    Event_Management = driver.find_element_by_xpath("//*[@id='main']/header/div[9]/nav/ul/li[3]/ul/li[1]/ul/li[1]/a").click()
    parent_page = driver.current_window_handle
    select_product1 = driver.find_element_by_xpath("//*[@id='lisfw']/div[1]/div[1]/article/div[1]/a").click()
    # time.sleep(5)
    child_page = driver.window_handles
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
    driver.switch_to.window(parent_page)
    select_product2 = driver.find_element_by_xpath("//*[@id='lisfw']/div[1]/div[2]/article/div[1]/a").click()
    child_page = driver.window_handles
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
    driver.switch_to.window(parent_page)
    select_product3 = driver.find_element_by_xpath("//*[@id='lisfw']/div[1]/div[3]/article/div[1]/a").click()


def services_and_Equiptment_Supplier():
    driver.implicitly_wait(20)
    services = driver.find_element_by_xpath("//a[@href='#'][normalize-space()='Services']")
    action = ActionChains(driver)
    action.move_to_element(services).perform()
    Equiptment_Supplier = driver.find_element_by_xpath("//*[@id='main']/header/div[9]/nav/ul/li[3]/ul/li[1]/ul/li[3]/a").click()
    select_product = driver.find_element_by_xpath("//a[@class='geodir-category-img-wrap fl-wrap']").click()

def services_and_Event_staff():
    driver.implicitly_wait(20)
    services = driver.find_element_by_xpath("//a[@href='#'][normalize-space()='Services']")
    action = ActionChains(driver)
    action.move_to_element(services).perform()
    Event_staff = driver.find_element_by_xpath("//*[@id='main']/header/div[9]/nav/ul/li[3]/ul/li[2]/ul/li[2]/a").click()
    select_product = driver.find_element_by_xpath("//*[@id='lisfw']/div[1]/div/article/div[1]/a").click()

def services_and_Photograpy_Videograpy():
    driver.implicitly_wait(20)
    services = driver.find_element_by_xpath("//a[@href='#'][normalize-space()='Services']")
    action = ActionChains(driver)
    action.move_to_element(services).perform()
    Photograpy_Videograpy = driver.find_element_by_xpath("//*[@id='main']/header/div[9]/nav/ul/li[3]/ul/li[3]/ul/li[1]/a")
    driver.execute_script("arguments[0].click();", Photograpy_Videograpy)
    select_product = driver.find_element_by_xpath("//*[@id='lisfw']/div[1]/div/article/div[1]/a").click()

def services_and_Event_Artists():
    driver.implicitly_wait(20)
    services = driver.find_element_by_xpath("//a[@href='#'][normalize-space()='Services']")
    action = ActionChains(driver)
    action.move_to_element(services).perform()
    Event_Artistsy = driver.find_element_by_xpath("//*[@id='main']/header/div[9]/nav/ul/li[3]/ul/li[3]/ul/li[3]/a").click()
    parent_page = driver.current_window_handle
    select_product1 = driver.find_element_by_xpath("//*[@id='lisfw']/div[1]/div[1]/article/div[1]/a").click()
    child_page  = driver.window_handles
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            # time.sleep(10)
    driver.switch_to.window(parent_page)
    select_product2 = driver.find_element_by_xpath("//*[@id='lisfw']/div[1]/div[2]/article/div[1]/a").click()


def services_and_Birthday_Specialist():
    driver.implicitly_wait(20)
    services = driver.find_element_by_xpath("//a[@href='#'][normalize-space()='Services']")
    action = ActionChains(driver)
    action.move_to_element(services).perform()
    Birthday_Specialist = driver.find_element_by_xpath("//*[@id='main']/header/div[9]/nav/ul/li[3]/ul/li[3]/ul/li[4]/a").click()
    select_product = driver.find_element_by_xpath("//*[@id='lisfw']/div[1]/div/article/div[1]/a").click()

def services_and_Catering_Service():
    driver.implicitly_wait(20)
    services = driver.find_element_by_xpath("//a[@href='#'][normalize-space()='Services']")
    action = ActionChains(driver)
    action.move_to_element(services).perform()
    Catering_Service = driver.find_element_by_xpath("//*[@id='main']/header/div[9]/nav/ul/li[3]/ul/li[4]/ul/li[2]/a").click()
    select_product = driver.find_element_by_xpath("//*[@id='lisfw']/div[1]/div/article/div[1]/a").click()

def services_and_Flowers_and_Decor():
    driver.implicitly_wait(20)
    services = driver.find_element_by_xpath("//a[@href='#'][normalize-space()='Services']")
    action = ActionChains(driver)
    action.move_to_element(services).perform()
    Flowers_and_Decor = driver.find_element_by_xpath("//*[@id='main']/header/div[9]/nav/ul/li[3]/ul/li[4]/ul/li[3]/a").click()
    # time.sleep(5)
    select_product = driver.find_element_by_xpath("//*[@id='lisfw']/div[1]/div/article/div[1]/a").click()


def packages_Event():
    driver.implicitly_wait(20)
    packages = driver.find_element_by_xpath("//*[@id='main']/header/div[9]/nav/ul/li[4]/a[1]")
    action = ActionChains(driver)
    action.move_to_element(packages).perform()
    Event_packages = driver.find_element_by_xpath("//*[@id='main']/header/div[9]/nav/ul/li[4]/ul/li[1]/a")
    driver.execute_script("arguments[0].click();", Event_packages)
    select_photo= driver.find_element_by_xpath("//*[@id='lisfw']/div[1]/div/article/div[1]/a").click()
    driver.back()
    select_text_link1 = driver.find_element_by_xpath("//a[@href='http://zoomvenues.info/packages/event/test-package']").click()

def packages_Work():
    driver.implicitly_wait(20)
    packages = driver.find_element_by_xpath("//*[@id='main']/header/div[9]/nav/ul/li[4]/a[1]")
    action = ActionChains(driver)
    action.move_to_element(packages).perform()
    Work_packages = driver.find_element_by_xpath("//*[@id='main']/header/div[9]/nav/ul/li[4]/ul/li[2]/a[2]").click()
    select_photo = driver.find_element_by_xpath("//*[@id='lisfw']/div[1]/div[1]/article/div[1]/a").click()
    select_text_link = driver.find_element_by_xpath("//a[@href='http://zoomvenues.info/packages/work/work-desk-package']").click()


# -------------  web site logo module are check ----------

def ZoomVenues_logo():
    logo_zoomvenues = driver.find_element_by_xpath("//*[@id='main']/header/a[1]/img").click()


def Blogs_share_mail():
    driver.implicitly_wait(20)
    parent_page = driver.current_window_handle
    print(parent_page)
    blogs = driver.find_element_by_xpath("//*[@id='main']/header/div[6]/a").click()
    child_page = driver.window_handles
    print(child_page)
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            more_share = driver.find_element_by_xpath("//*[@id='at4-share']/a[5]/span[2]").click()
            search_services = driver.find_element_by_xpath("//*[@id='at-expanded-menu-service-filter']")
            search_services.send_keys("gmail")
            maile_share = driver.find_element_by_xpath("//*[name()='path' and contains(@d,'M7.225 8h-')]").click()


def Blog_social_app_btn():
    driver.implicitly_wait(20)

    parent_page = driver.current_window_handle
    print(parent_page)
    blogs = driver.find_element_by_xpath("//*[@id='main']/header/div[6]/a").click()
    child_page = driver.window_handles
    print(child_page)
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            fb_btn = driver.find_element_by_xpath("//*[@id='at4-share']/a[1]").click()
            # time.sleep(3)
            driver.back()
            tw_btn = driver.find_element_by_xpath("//a[2]//span[2]//*[name()='svg']").click()
            # time.sleep(3)
            driver.back()
            link_line_btn = driver.find_element_by_xpath("//a[3]//span[2]//*[name()='svg']").click()
            # time.sleep(3)
            # Pinterest_bt = driver.find_element_by_xpath("//a[4]//span[2]//*[name()='svg']").click()
            # time.sleep(4)
    driver.switch_to.window(parent_page)
    blogs = driver.find_element_by_xpath("//*[@id='main']/header/div[6]/a").click()

    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)

            more_share = driver.find_element_by_xpath("//*[@id='at4-share']/a[5]/span[2]").click()
            search_services = driver.find_element_by_xpath("//*[@id='at-expanded-menu-service-filter']")
            search_services.send_keys("gmail")
            maile_share = driver.find_element_by_xpath("//*[name()='path' and contains(@d,'M7.225 8h-')]").click()


def admin_btn():
    driver.implicitly_wait(20)
    parent_page = driver.current_window_handle
    print(parent_page)
    admin = driver.find_element_by_xpath("//*[@id='main']/header/div[2]/a").click()
    child_page = driver.window_handles
    print(child_page)
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            pro_info_form_close = driver.find_element_by_xpath("//*[@id='ex1']/a").click()


def call_btn():
    driver.implicitly_wait(20)
    call = driver.find_element_by_xpath("//a[@class='bh-w-button--round bh-w-button bh-w-button-call bh-widget-page__button-main']")
    driver.execute_script("arguments[0].click();", call)


def whatsapp_btn():
    driver.implicitly_wait(20)
    whatsapp = driver.find_element_by_xpath("//a[@class='q8c6tt-0 jWcIXO']").click()

# ---------------  event venues search bar ---------------------

def event_venues_search_bar():
    driver.implicitly_wait(20)
    home_page1 = driver.find_element_by_xpath("//img[@src='http://zoomvenues.info/images/logo.png']").click()
    # home_page2 = driver.find_element_by_css_selector(".logo-holder > img:nth-child(1)").click()
    driver.execute_script("window.scrollTo(0,300)")
    location = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/section[2]/div/div/div/div[1]/div/div[1]/div/form/div[1]/div")
    driver.execute_script("arguments[0].click();",location)
    select_loc = driver.find_element_by_xpath("//div[@class='nice-select chosen-select open']//li[@class='option'][normalize-space()='Abu Dhabi']").click()
    venue = driver.find_element_by_xpath("(//div[@class='nice-select chosen-select'])[2]").click()
    select_event = driver.find_element_by_xpath("(//li[contains(text(),'Banquets')])[1]").click()
    categries = driver.find_element_by_xpath("(//div[@class='nice-select chosen-select'])[3]").click()
    select_categries = driver.find_element_by_xpath("//li[contains(text(),'Wedding')]").click()
    search = driver.find_element_by_xpath("//*[@id='search-result_event']/button").click()
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("omsonar")
    # driver.execute_script("document.querySelector(your_name_css).value=('om soanr')")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("9158333486")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("05-07-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("2:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("nothing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()
    home_page1 = driver.find_element_by_xpath("//img[@src='http://zoomvenues.info/images/logo.png']").click()

# def event_venues_search_bar2():
#     driver.implicitly_wait(20)
#     loc = driver.find_element_by_xpath("(//div[@class='nice-select chosen-select'])[1]").click()
#     search = driver.find_element_by_xpath("//div[@class='nice-select chosen-select open']//input[@placeholder='Search...']")
#     search.send_keys("Abu Dhabi")
#     select_loc = driver.find_element_by_xpath("//div[@class='nice-select chosen-select open']//span[@class='current'][normalize-space()='Dubai']").click()
#     time.sleep(5)



def click_Banquets():
    driver.implicitly_wait(20)
    home_page = driver.find_element_by_xpath("//img[@src='http://zoomvenues.info/images/logo.png']").click()
    driver.execute_script("window.scrollTo(0,300)")
    parent_page = driver.current_window_handle
    select_banquet = driver.find_element_by_xpath("//div[@id='tab-inpt1']//li[1]//a[1]").click()
    child_page =driver.window_handles
    for  handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            your_name = driver.find_element_by_css_selector(your_name_css)
            your_name.send_keys("om chavhan")
            mail_id = driver.find_element_by_css_selector(mail_id_css)
            mail_id.send_keys("omworld01@gmail.com")
            phone_no = driver.find_element_by_css_selector(phone_no_css)
            phone_no.send_keys("9158333486")
            select_type = driver.find_element_by_css_selector(select_event_type_css)
            dropdown = Select(select_type)
            dropdown.select_by_index(1)
            date = driver.find_element_by_css_selector(select_date_css)
            date.send_keys("05-07-2022")
            time = driver.find_element_by_css_selector(time_css)
            time.send_keys("2:30PM")
            no_of_people = driver.find_element_by_css_selector(no_of_people_css)
            no_of_people.send_keys(5)
            select_budget = driver.find_element_by_css_selector(select_budget_css)
            dropdown_budget = Select(select_budget)
            dropdown_budget.select_by_value("80 to 150")
            add_req = driver.find_element_by_css_selector(add_req_css)
            add_req.send_keys("nothing________")
            acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
            acc_term_condition.click()
            submit = driver.find_element_by_css_selector(submit_css).click()
            close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()
    # driver.switch_to.window(parent_page)
    # logo_zoomvenues = driver.find_element_by_xpath("//*[@id='main']/header/a[1]/img").click()



def click_Party_Halls():
    driver.implicitly_wait(20)
    home_page = driver.find_element_by_xpath("//img[@src='http://zoomvenues.info/images/logo.png']").click()
    driver.execute_script("window.scrollTo(0,300)")
    parent_page = driver.current_window_handle
    select_Party_Halls = driver.find_element_by_css_selector("div[id='tab-inpt1'] li:nth-child(1) a:nth-child(1)").click()
    child_page = driver.window_handles
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            your_name = driver.find_element_by_css_selector(your_name_css)
            your_name.send_keys("omsonar")
            # driver.execute_script("document.querySelector(your_name_css).value=('om soanr')")
            mail_id = driver.find_element_by_css_selector(mail_id_css)
            mail_id.send_keys("omworld01@gmail.com")
            phone_no = driver.find_element_by_css_selector(phone_no_css)
            phone_no.send_keys("9158333486")
            select_type = driver.find_element_by_css_selector(select_event_type_css)
            dropdown = Select(select_type)
            dropdown.select_by_index(1)
            date = driver.find_element_by_css_selector(select_date_css)
            date.send_keys("05-07-2022")
            time = driver.find_element_by_css_selector(time_css)
            time.send_keys("2:30PM")
            no_of_people = driver.find_element_by_css_selector(no_of_people_css)
            no_of_people.send_keys(5)
            select_budget = driver.find_element_by_css_selector(select_budget_css)
            dropdown_budget = Select(select_budget)
            dropdown_budget.select_by_value("80 to 150")
            add_req = driver.find_element_by_css_selector(add_req_css)
            add_req.send_keys("nothing________")
            acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
            acc_term_condition.click()
            submit = driver.find_element_by_css_selector(submit_css).click()
            close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()
            driver.switch_to.window(parent_page)
    # driver.switch_to.window(parent_page)
    # logo_zoomvenues = driver.find_element_by_xpath("//*[@id='main']/header/a[1]/img").click()


def click_Yacht():
    driver.implicitly_wait(20)
    home_page = driver.find_element_by_xpath("//img[@src='http://zoomvenues.info/images/logo.png']").click()
    driver.execute_script("window.scrollTo(0,300)")
    parent_page = driver.current_window_handle
    select_yacht = driver.find_element_by_css_selector("body > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(3) > a:nth-child(1)").click()
    child_page =driver.window_handles
    for  handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            your_name = driver.find_element_by_css_selector(your_name_css)
            your_name.send_keys("om chavhan")
            mail_id = driver.find_element_by_css_selector(mail_id_css)
            mail_id.send_keys("omworld01@gmail.com")
            phone_no = driver.find_element_by_css_selector(phone_no_css)
            phone_no.send_keys("9158333486")
            select_type = driver.find_element_by_css_selector(select_event_type_css)
            dropdown = Select(select_type)
            dropdown.select_by_index(1)
            date = driver.find_element_by_css_selector(select_date_css)
            date.send_keys("05-07-2022")
            time = driver.find_element_by_css_selector(time_css)
            time.send_keys("2:30PM")
            no_of_people = driver.find_element_by_css_selector(no_of_people_css)
            no_of_people.send_keys(5)
            select_budget = driver.find_element_by_css_selector(select_budget_css)
            dropdown_budget = Select(select_budget)
            dropdown_budget.select_by_value("80 to 150")
            add_req = driver.find_element_by_css_selector(add_req_css)
            add_req.send_keys("nothing________")
            acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
            acc_term_condition.click()
            submit = driver.find_element_by_css_selector(submit_css).click()
            close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()
    # driver.switch_to.window(parent_page)
    # logo_zoomvenues = driver.find_element_by_xpath("//*[@id='main']/header/a[1]/img").click()



def click_Wedding():
    driver.implicitly_wait(20)
    home_page = driver.find_element_by_xpath("//img[@src='http://zoomvenues.info/images/logo.png']").click()
    driver.execute_script("window.scrollTo(0,300)")
    parent_page = driver.current_window_handle
    select_wedding = driver.find_element_by_xpath("//img[@src='http://zoomvenues.info/images/wedding.png']").click()
    child_page =driver.window_handles
    for  handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            time.send_keys(3)
            your_name = driver.find_element_by_css_selector(your_name_css)
            your_name.send_keys("om chavhan")
            mail_id = driver.find_element_by_css_selector(mail_id_css)
            mail_id.send_keys("omworld01@gmail.com")
            phone_no = driver.find_element_by_css_selector(phone_no_css)
            phone_no.send_keys("9158333486")
            select_type = driver.find_element_by_css_selector(select_event_type_css)
            dropdown = Select(select_type)
            dropdown.select_by_index(1)
            date = driver.find_element_by_css_selector(select_date_css)
            date.send_keys("05-07-2022")
            time = driver.find_element_by_css_selector(time_css)
            time.send_keys("2:30PM")
            no_of_people = driver.find_element_by_css_selector(no_of_people_css)
            no_of_people.send_keys(5)
            select_budget = driver.find_element_by_css_selector(select_budget_css)
            dropdown_budget = Select(select_budget)
            dropdown_budget.select_by_value("80 to 150")
            add_req = driver.find_element_by_css_selector(add_req_css)
            add_req.send_keys("nothing________")
            acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
            acc_term_condition.click()
            submit = driver.find_element_by_css_selector(submit_css).click()
            close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()
    # driver.switch_to.window(parent_page)
    # logo_zoomvenues = driver.find_element_by_xpath("//*[@id='main']/header/a[1]/img").click()


def click_Birthday():
    driver.implicitly_wait(20)
    home_page = driver.find_element_by_xpath("//img[@src='http://zoomvenues.info/images/logo.png']").click()
    driver.execute_script("window.scrollTo(0,300)")
    parent_page = driver.current_window_handle
    select_wedding = driver.find_element_by_xpath("//a[@href='https://zoomvenues.info/event-venue/search?event_type=birthday']").click()
    child_page = driver.window_handles
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            your_name = driver.find_element_by_css_selector(your_name_css)
            your_name.send_keys("om chavhan")
            mail_id = driver.find_element_by_css_selector(mail_id_css)
            mail_id.send_keys("omworld01@gmail.com")
            phone_no = driver.find_element_by_css_selector(phone_no_css)
            phone_no.send_keys("9158333486")
            select_type = driver.find_element_by_css_selector(select_event_type_css)
            dropdown = Select(select_type)
            dropdown.select_by_index(1)
            date = driver.find_element_by_css_selector(select_date_css)
            date.send_keys("05-07-2022")
            time = driver.find_element_by_css_selector(time_css)
            time.send_keys("2:30PM")
            no_of_people = driver.find_element_by_css_selector(no_of_people_css)
            no_of_people.send_keys(5)
            select_budget = driver.find_element_by_css_selector(select_budget_css)
            dropdown_budget = Select(select_budget)
            dropdown_budget.select_by_value("80 to 150")
            add_req = driver.find_element_by_css_selector(add_req_css)
            add_req.send_keys("nothing________")
            acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
            acc_term_condition.click()
            submit = driver.find_element_by_css_selector(submit_css).click()
            close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()
    # driver.switch_to.window(parent_page)



def work_venues_search_bar():
    driver.implicitly_wait(20)
    driver.execute_script("window.scrollTo(0,300)")
    click_work_venues = driver.find_element_by_css_selector("a[href='#tab-inpt2']")
    driver.execute_script("arguments[0].click();",click_work_venues)
    search_click = driver.find_element_by_css_selector("body > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > div:nth-child(2)")
    driver.execute_script("arguments[0].click();",search_click)
    select_loc = driver.find_element_by_xpath("//div[@class='nice-select chosen-select open']//li[@class='option'][normalize-space()='Ajman']").click()
    click_select_venues = driver.find_element_by_xpath("(//div[@class='nice-select chosen-select'])[5]")
    driver.execute_script("arguments[0].click();", click_select_venues)
    select_venues = driver.find_element_by_xpath("//li[contains(text(),'Conference Rooms')]").click()
    click_categories = driver.find_element_by_xpath("(//span[@class='current'][normalize-space()='All Event Categories'])[2]").click()
    # select_categories1 = driver.find_element_by_xpath("//li[normalize-space()='Exhibition']").click()
    select_categories2 = driver.find_element_by_xpath("//li[normalize-space()='Trainings']").click()
    search_btn = driver.find_element_by_xpath("(//button[@class='main-search-button color2-bg'][normalize-space()='Search'])[2]").click()
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("omsonar")
    # driver.execute_script("document.querySelector(your_name_css).value=('om soanr')")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("9158333486")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("05-07-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("2:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("nothing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()
    home_page2 = driver.find_element_by_xpath("//img[@src='https://zoomvenues.info/images/logo.png']").click()

def click_study_rooms():
    driver.implicitly_wait(20)
    driver.execute_script("window.scrollTo(0,300)")
    click_work_venues = driver.find_element_by_css_selector("a[href='#tab-inpt2']")
    driver.execute_script("arguments[0].click();", click_work_venues)
    parent_page = driver.current_window_handle
    select_study_rooms = driver.find_element_by_xpath("//img[@src='https://zoomvenues.info/images/Study-Rooms.png']")
    driver.execute_script("arguments[0].click();",select_study_rooms)
    child_page = driver.window_handles
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            your_name = driver.find_element_by_css_selector(your_name_css)
            your_name.send_keys("om chavhan")
            mail_id = driver.find_element_by_css_selector(mail_id_css)
            mail_id.send_keys("omworld01@gmail.com")
            phone_no = driver.find_element_by_css_selector(phone_no_css)
            phone_no.send_keys("9158333486")
            select_type = driver.find_element_by_css_selector(select_event_type_css)
            dropdown = Select(select_type)
            dropdown.select_by_index(1)
            date = driver.find_element_by_css_selector(select_date_css)
            date.send_keys("05-07-2022")
            time = driver.find_element_by_css_selector(time_css)
            time.send_keys("2:30PM")
            no_of_people = driver.find_element_by_css_selector(no_of_people_css)
            no_of_people.send_keys(5)
            select_budget = driver.find_element_by_css_selector(select_budget_css)
            dropdown_budget = Select(select_budget)
            dropdown_budget.select_by_value("80 to 150")
            add_req = driver.find_element_by_css_selector(add_req_css)
            add_req.send_keys("nothing________")
            acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
            acc_term_condition.click()
            submit = driver.find_element_by_css_selector(submit_css).click()
            close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()
            home_page2 = driver.find_element_by_xpath("//img[@src='https://zoomvenues.info/images/logo.png']").click()

def click_meeting_rooms():
    driver.implicitly_wait(20)
    driver.execute_script("window.scrollTo(0,300)")
    click_work_venues = driver.find_element_by_css_selector("a[href='#tab-inpt2']")
    driver.execute_script("arguments[0].click();", click_work_venues)
    parent_page = driver.current_window_handle
    select_meeting_rooms = driver.find_element_by_xpath("//img[@src='https://zoomvenues.info/images/meeting-room.png']")
    driver.execute_script("arguments[0].click();", select_meeting_rooms)
    child_page = driver.window_handles
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            your_name = driver.find_element_by_css_selector(your_name_css)
            your_name.send_keys("om chavhan")
            mail_id = driver.find_element_by_css_selector(mail_id_css)
            mail_id.send_keys("omworld01@gmail.com")
            phone_no = driver.find_element_by_css_selector(phone_no_css)
            phone_no.send_keys("9158333486")
            select_type = driver.find_element_by_css_selector(select_event_type_css)
            dropdown = Select(select_type)
            dropdown.select_by_index(1)
            date = driver.find_element_by_css_selector(select_date_css)
            date.send_keys("05-07-2022")
            time = driver.find_element_by_css_selector(time_css)
            time.send_keys("2:30PM")
            no_of_people = driver.find_element_by_css_selector(no_of_people_css)
            no_of_people.send_keys(5)
            select_budget = driver.find_element_by_css_selector(select_budget_css)
            dropdown_budget = Select(select_budget)
            dropdown_budget.select_by_value("80 to 150")
            add_req = driver.find_element_by_css_selector(add_req_css)
            add_req.send_keys("nothing________")
            acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
            acc_term_condition.click()
            submit = driver.find_element_by_css_selector(submit_css).click()
            close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()
            home_page2 = driver.find_element_by_xpath("//img[@src='https://zoomvenues.info/images/logo.png']").click()


def click_Conference_Rooms():
    driver.implicitly_wait(20)
    driver.execute_script("window.scrollTo(0,300)")
    click_work_venues = driver.find_element_by_css_selector("a[href='#tab-inpt2']")
    driver.execute_script("arguments[0].click();", click_work_venues)
    parent_page = driver.current_window_handle
    select_Conference_Rooms = driver.find_element_by_xpath("//img[@title='Conference Rooms']")
    driver.execute_script("arguments[0].click();", select_Conference_Rooms)
    child_page = driver.window_handles
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            your_name = driver.find_element_by_css_selector(your_name_css)
            your_name.send_keys("om chavhan")
            mail_id = driver.find_element_by_css_selector(mail_id_css)
            mail_id.send_keys("omworld01@gmail.com")
            phone_no = driver.find_element_by_css_selector(phone_no_css)
            phone_no.send_keys("9158333486")
            select_type = driver.find_element_by_css_selector(select_event_type_css)
            dropdown = Select(select_type)
            dropdown.select_by_index(1)
            date = driver.find_element_by_css_selector(select_date_css)
            date.send_keys("05-07-2022")
            time = driver.find_element_by_css_selector(time_css)
            time.send_keys("2:30PM")
            no_of_people = driver.find_element_by_css_selector(no_of_people_css)
            no_of_people.send_keys(5)
            select_budget = driver.find_element_by_css_selector(select_budget_css)
            dropdown_budget = Select(select_budget)
            dropdown_budget.select_by_value("80 to 150")
            add_req = driver.find_element_by_css_selector(add_req_css)
            add_req.send_keys("nothing________")
            acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
            acc_term_condition.click()
            submit = driver.find_element_by_css_selector(submit_css).click()
            close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()
            home_page2 = driver.find_element_by_xpath("//img[@src='https://zoomvenues.info/images/logo.png']").click()

def click_CoWork_Desks():
    driver.implicitly_wait(20)
    driver.execute_script("window.scrollTo(0,300)")
    click_work_venues = driver.find_element_by_css_selector("a[href='#tab-inpt2']")
    driver.execute_script("arguments[0].click();", click_work_venues)
    parent_page = driver.current_window_handle
    select_CoWork_Desks = driver.find_element_by_xpath("//img[@title='Co-Work Desks']")
    driver.execute_script("arguments[0].click();", select_CoWork_Desks)
    child_page = driver.window_handles
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            your_name = driver.find_element_by_css_selector(your_name_css)
            your_name.send_keys("om chavhan")
            mail_id = driver.find_element_by_css_selector(mail_id_css)
            mail_id.send_keys("omworld01@gmail.com")
            phone_no = driver.find_element_by_css_selector(phone_no_css)
            phone_no.send_keys("9158333486")
            select_type = driver.find_element_by_css_selector(select_event_type_css)
            dropdown = Select(select_type)
            dropdown.select_by_index(1)
            date = driver.find_element_by_css_selector(select_date_css)
            date.send_keys("05-07-2022")
            time = driver.find_element_by_css_selector(time_css)
            time.send_keys("2:30PM")
            no_of_people = driver.find_element_by_css_selector(no_of_people_css)
            no_of_people.send_keys(5)
            select_budget = driver.find_element_by_css_selector(select_budget_css)
            dropdown_budget = Select(select_budget)
            dropdown_budget.select_by_value("80 to 150")
            add_req = driver.find_element_by_css_selector(add_req_css)
            add_req.send_keys("nothing________")
            acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
            acc_term_condition.click()
            submit = driver.find_element_by_css_selector(submit_css).click()
            close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()
            home_page2 = driver.find_element_by_xpath("//img[@src='https://zoomvenues.info/images/logo.png']").click()

def click_Business_Centres():
    driver.implicitly_wait(20)
    driver.execute_script("window.scrollTo(0,300)")
    click_work_venues = driver.find_element_by_css_selector("a[href='#tab-inpt2']")
    driver.execute_script("arguments[0].click();", click_work_venues)
    parent_page = driver.current_window_handle
    select_Business_Centres = driver.find_element_by_xpath("//img[@title='Business Centres']")
    driver.execute_script("arguments[0].click();", select_Business_Centres)
    child_page = driver.window_handles
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            your_name = driver.find_element_by_css_selector(your_name_css)
            your_name.send_keys("om chavhan")
            mail_id = driver.find_element_by_css_selector(mail_id_css)
            mail_id.send_keys("omworld01@gmail.com")
            phone_no = driver.find_element_by_css_selector(phone_no_css)
            phone_no.send_keys("9158333486")
            select_type = driver.find_element_by_css_selector(select_event_type_css)
            dropdown = Select(select_type)
            dropdown.select_by_index(1)
            date = driver.find_element_by_css_selector(select_date_css)
            date.send_keys("05-07-2022")
            time = driver.find_element_by_css_selector(time_css)
            time.send_keys("2:30PM")
            no_of_people = driver.find_element_by_css_selector(no_of_people_css)
            no_of_people.send_keys(5)
            select_budget = driver.find_element_by_css_selector(select_budget_css)
            dropdown_budget = Select(select_budget)
            dropdown_budget.select_by_value("80 to 150")
            add_req = driver.find_element_by_css_selector(add_req_css)
            add_req.send_keys("nothing________")
            acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
            acc_term_condition.click()
            submit = driver.find_element_by_css_selector(submit_css).click()
            close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()
            home_page2 = driver.find_element_by_xpath("//img[@src='https://zoomvenues.info/images/logo.png']").click()



def Services_search_bar():
    driver.implicitly_wait(20)
    # home_page1 = driver.find_element_by_xpath("//img[@src='http://zoomvenues.info/images/logo.png']").click()

    # home_page2 = driver.find_element_by_css_selector(".logo-holder > img:nth-child(1)").click()
    service = driver.find_element_by_css_selector("a[href='#tab-inpt3']").click()
    driver.execute_script("window.scrollTo(0,300)")
    location = driver.find_element_by_xpath("//div[@class='main-search-input-item edited-item']//div[@class='nice-select chosen-select']")
    driver.execute_script("arguments[0].click();",location)
    select_loc = driver.find_element_by_xpath("//div[@class='nice-select chosen-select open']//li[@class='option'][normalize-space()='Sharjah']").click()
    categries = driver.find_element_by_xpath("(//div[@class='nice-select chosen-select'])[8]")
    driver.execute_script("arguments[0].click();",categries)
    select_categries = driver.find_element_by_xpath("//li[normalize-space()='Event Management']").click()
    search = driver.find_element_by_css_selector("div[id='tab-inpt1'] button[class='main-search-button color2-bg']")
    driver.execute_script("arguments[0].click();",search)
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("omsonar")
    # driver.execute_script("document.querySelector(your_name_css).value=('om soanr')")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("9158333486")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("05-07-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("2:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("nothing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()
    home_page1 = driver.find_element_by_css_selector(".logo-holder > img:nth-child(1)")
    driver.execute_script("arguments[0].click();", home_page1)


def click_Catering_Service():
    driver.implicitly_wait(20)
    service = driver.find_element_by_css_selector("a[href='#tab-inpt3']").click()
    driver.execute_script("window.scrollTo(0,300)")
    parent_page = driver.current_window_handle
    Catering_Service = driver.find_element_by_xpath("//img[@src='https://zoomvenues.info/images/catering.png']").click()
    child_page = driver.window_handles
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            click_service = driver.find_element_by_xpath("//a[normalize-space()='Cakewalk']").click()
    driver.switch_to.window(parent_page)


def click_Photography_Videography():
    driver.implicitly_wait(20)
    service = driver.find_element_by_css_selector("a[href='#tab-inpt3']").click()
    driver.execute_script("window.scrollTo(0,300)")
    parent_page = driver.current_window_handle
    Photography_Videography = driver.find_element_by_xpath("//span[normalize-space()='Photography & Videography']").click()
    child_page = driver.window_handles
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            click_service = driver.find_element_by_xpath("//a[normalize-space()='photogenic faces']").click()
    driver.switch_to.window(parent_page)


def click_Flowers_Decor():
    driver.implicitly_wait(20)
    service = driver.find_element_by_css_selector("a[href='#tab-inpt3']").click()
    driver.execute_script("window.scrollTo(0,300)")
    parent_page = driver.current_window_handle
    Flowers_Decor = driver.find_element_by_xpath("//img[@src='https://zoomvenues.info/images/decor.png']").click()
    child_page = driver.window_handles
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            click_service = driver.find_element_by_xpath("//a[normalize-space()='Tabrah Flowers']").click()
    driver.switch_to.window(parent_page)



#-------------- footer moduls --------------

def footer_socail_app():
    driver.implicitly_wait(20)
    driver.execute_script("window.scrollTo(0,3000)")
    fb_btn = driver.find_element_by_xpath("//a[@href='https://www.facebook.com/zoomvenuesforyou']").click()
    # time.sleep(3)
    driver.back()
    insta_btn = driver.find_element_by_xpath("//a[@href='https://www.instagram.com/zoomvenuesofficial']").click()
    # time.sleep(3)
    driver.back()
    linkedin_btn = driver.find_element_by_xpath("//a[contains(@href,'https://www.linkedin.com/company/zoomvenues')]")
    driver.execute_script("arguments[0].click();", linkedin_btn)
    # time.sleep(3)
    driver.back()
    twitter_btn = driver.find_element_by_xpath("//a[@href='https://twitter.com/zoomvenues']").click()


def our_latest_news():
    driver.implicitly_wait(20)
    driver.execute_script("window.scrollTo(0,3000)")
    parent_page = driver.current_window_handle
    news1 = driver.find_element_by_xpath("//a[contains(text(),'Emirati youth learning new skills to be ready for ')]").click()
    child_page = driver.window_handles
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
    driver.switch_to.window(parent_page)
    # time.sleep(3)
    news2 = driver.find_element_by_xpath("//a[contains(text(),'Sharjah to host National Libraries Summit from Nov')]").click()
    # time.sleep(3)
    news3 = driver.find_element_by_xpath("//a[normalize-space()='Gold price drops, but still trades above $1,800']").click()
    # time.sleep(3)
    news4 = driver.find_element_by_xpath("//a[contains(text(),'Gitex 2021: Meet the home assistant robot that has')]").click()
    # time.sleep(3)
    news5 = driver.find_element_by_xpath("//a[contains(text(),'4-day holidays in UAE: Top things to do at Expo 20')]").click()


def vendor_login_reg():
    driver.implicitly_wait(20)
    driver.execute_script("window.scrollTo(0,3000)")
    parent_page = driver.current_window_handle
    reg_vendor = driver.find_element_by_xpath("//a[normalize-space()='Register as Vendor']").click()
    child_page = driver.window_handles
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)

    driver.switch_to.window(parent_page)
    log_vendor = driver.find_element_by_xpath("//a[normalize-space()='Login as Vendor'] ").click()
    # time.sleep(5)
    reg_service_provider = driver.find_element_by_xpath("//a[normalize-space()='Register as Service Provider']").click()
    # time.sleep(5)
    log_service_proder = driver.find_element_by_xpath("//a[normalize-space()='Login as Service Provider']").click()


def contact_us_mail_call():
    driver.implicitly_wait(20)
    # contact = driver.find_element_by_xpath("//a[normalize-space()='info@zoomvenues.com']")
    # driver.execute_script("arguments[0].click();",contact)
    # time.sleep(3)
    call = driver.find_element_by_xpath("//a[normalize-space()='+971 554538026']").click()


# ------------------ show filter function are test -----------------

def show_filter():
    driver.implicitly_wait(20)
    event_venues = driver.find_element_by_xpath("//a[normalize-space()='Event Venues']")
    action = ActionChains(driver)
    action.move_to_element(event_venues).perform()
    banquets_c = driver.find_element_by_xpath("(//a[contains(text(),'Banquets')])[1]")
    driver.execute_script("arguments[0].click();", banquets_c)
    your_name = driver.find_element_by_css_selector(your_name_css)
    your_name.send_keys("om chavhan")
    mail_id = driver.find_element_by_css_selector(mail_id_css)
    mail_id.send_keys("omworld01@gmail.com")
    phone_no = driver.find_element_by_css_selector(phone_no_css)
    phone_no.send_keys("9158333486")
    select_type = driver.find_element_by_css_selector(select_event_type_css)
    dropdown = Select(select_type)
    dropdown.select_by_index(1)
    date = driver.find_element_by_css_selector(select_date_css)
    date.send_keys("05-07-2022")
    time = driver.find_element_by_css_selector(time_css)
    time.send_keys("2:30PM")
    no_of_people = driver.find_element_by_css_selector(no_of_people_css)
    no_of_people.send_keys(5)
    select_budget = driver.find_element_by_css_selector(select_budget_css)
    dropdown_budget = Select(select_budget)
    dropdown_budget.select_by_value("80 to 150")
    add_req = driver.find_element_by_css_selector(add_req_css)
    add_req.send_keys("nothing________")
    acc_term_condition = driver.find_element_by_css_selector(acc_term_condition_css)
    acc_term_condition.click()
    submit = driver.find_element_by_css_selector(submit_css).click()
    close_pop = driver.find_element_by_css_selector("div[id='venuemodalen5'] div[class='close-reg'] i[class='fal fa-times']").click()
    # time.sleep(3)
    click_show_filter = driver.find_element_by_css_selector("div[class='show-hidden-sb shsb_btn shsb_btn_act'] span").click()
    all_categories = driver.find_element_by_css_selector(".nice-select.chosen-select.no-search-select.filter_category").click()
    select_event  = driver.find_element_by_xpath("//li[@class='option selected focus']").click()


def Click_Add_User():
    driver.implicitly_wait(20)
    click_add_user = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/newuser/create']").click()


def test_customer_page():
    driver.implicitly_wait(40)
    driver.maximize_window()
    driver.get(zoomvenuesurl)

    # ---------------  Header functions testing -----------------------
    # Make_an_enquiry("om chavhan","omworld01@gmail.com","9158333486")
    # sign_in("om","chavhan","omworld",9195833486,"omworldo1","omworld01")
    login()
    # time.sleep(3)

    # ZoomVenues_logo()
    # time.sleep(3)

    # Blogs_share_mail()
    # time.sleep(5)
    # Blog_social_app_btn()
    # time.sleep(5)

    # admin_btn()

    #call_btn()
    # whatsapp_btn()


    #---------------  Events Venues Dropdown-----------------------
    # event_venues_Banquets_test(make_enquiry)
    # time.sleep(5)
    event_venues_Party_Halls_test()
    # event_venues_Convention_Centre_test()
    # event_venues_Farm_Houses_test()
    # event_venues_Roof_Tops_test()
    # event_venues_Auditoriums_test()
    # event_venues_Yacht_test()
    # event_venues_Palace_test()
    # event_venues_Sports_Complex_test()
    # event_venues_Open_air_places_test()

    # ---------------  Work Venues Dropdown-----------------------
    # work_venues_and_business_cent_test()
    # time.sleep(5)
    # work_venues_and_co_work_desk_test()
    # time.sleep(5)
    # work_venues_and_Conference_Rooms_test()
    # time.sleep(5)
    # work_venues_and_Study_Rooms_test()
    # time.sleep(5)
    # work_venues_and_Uni_halls_test()
    # time.sleep(5)
    # work_venues_and_Seminar_auditoriums_test()
    # time.sleep(5)

    # ---------------  Services Dropdown-----------------------
    # services_and_Event_Management()
    # time.sleep(5)
    # services_and_Equiptment_Supplier()
    # time.sleep(5)
    # services_and_Event_staff()
    # time.sleep(5)
    # services_and_Photograpy_Videograpy()
    # time.sleep(5)
    # services_and_Event_Artists()
    # time.sleep(5)
    # services_and_Birthday_Specialist()
    # time.sleep(5)
    # services_and_Catering_Service()
    # time.sleep(5)
    # services_and_Flowers_and_Decor()
    # time.sleep(5)

    # ---------------  Packages Dropdown-----------------------
    # packages_Event()
    # time.sleep(5)
    # packages_Work()
    # time.sleep(5)
    #

    # ---------------  Events Venues Search Bar-----------------------
    # event_venues_search_bar()
    # click_Banquets()
    # time.sleep(5)
    # click_Party_Halls()
    # time.sleep(5)
    # click_Yacht()
    # time.sleep(5)
    # click_Wedding()
    # time.sleep(5)
    # click_Birthday()

    # ---------------  Work Venues Search Bar-----------------------
    # work_venues_search_bar()
    # click_study_rooms()
    # click_meeting_rooms()
    # click_Conference_Rooms()
    # click_CoWork_Desks()
    # click_Business_Centres()

    # ---------------  Services Search Bar-----------------------
    # Services_search_bar()
    # click_Catering_Service()
    # click_Photography_Videography()
    # click_Flowers_Decor()

    # ---------------  Footer function testing -----------------------
    # footer_socail_app()
    # our_latest_news()
    # vendor_login_reg()
    # contact_us_mail_call()

    # show_filter()
    time.sleep(3)
    driver.quit()


