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


# Bellow Web Elements
click_venuename_xpath = "(//*[@class='filter-option-inner-inner'])[2]"
select_venue_name_xpath = "//div[@aria-expanded='true']//ul[@class='dropdown-menu inner show']//li/a//span[normalize-space()='20 June 4-venue1 (20 June 4)']"
OtherBH_Name_xpath = "//*[@id='other_business_hub_name']"
OtherBH_Email_xpath = "//*[@id='old_hub_email1']"
OtherBH_ContactNo_xpath = "//*[@id='old_hub_contact1']"
Add_MoreBH_xpath = "//*[@id='addMoreOptions1']"

vendor_login_xpath = "(//a[@class='btn btn-default'])[2]"
pop_up_close_xpath = "//div[@id='simpleModal']//span[@aria-hidden='true'][normalize-space()='×']"
email_id_xpath = "//input[@id='user']"
password_xpath = "//input[@id='password']"
login_xpath = "//button[normalize-space()='Login']"
venue_lead_select_xpath = "//*[@href='http://vendor.zoomvenues.info/admin/enquiries/leads']"
add_lead_xpath = "//a[normalize-space()='Add New Leads']"
customer_name_xpath = "//input[@id='custname']"
cust_mail_id_xpath = "//input[@id='email']"
event_type_xpath = "//select[@id='event_type']"
mobile_no_xpath = "//input[@id='phone']"
event_date_xpath = "//input[@placeholder='Enter Event Date ']"
event_time_xpath = "//input[@id='eventTime']"
no_of_people_xpath = "//input[@id='people']"
budget_xpath = "//input[@id='budget']"
additional_info_xpath = "//textarea[@id='message']"
source_xpath = "//select[@id='source']"
channel_xpath = "//select[@id='channel']"
add_menu_xpath = "//textarea[@id='menus']"
note_xpath = "//textarea[@name='note']"
Add_Lead_xpath = "//*[@id='btnSubmitEnquiry']"

driver = webdriver.Chrome(executable_path="C:\\Users\\GiTESH SONAR\\PycharmProjects\\ZoomVenues.Com\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="/geckodriver.exe")
zoomvenuesurl = "https://zoomvenues.info/"


def click_vendor_login(self):
    parent = self.driver.current_window_handle
    print(parent)
    self.driver.find_element(By.XPATH, self.vendor_login_xpath).click()
    all_handle = self.driver.window_handles
    print(all_handle)
    for handle in all_handle:
        if handle != parent:
            self.driver.switch_to.window(handle)
            self.driver.find_element(By.XPATH, self.pop_up_close_xpath).click()
            time.sleep(5)
            # self.driver.close()
            # time.sleep(4)
            break


def close_popup(self):
    popup = self.driver.find_element(By.XPATH, self.pop_up_close_xpath)
    self.driver.execute_script("arguments[0].click();", popup)


def enter_vendor_id(self, vendor_id):
    self.driver.find_element(By.XPATH, self.email_id_xpath).send_keys(vendor_id)


def enter_vendor_pass(self, vendor_password):
    self.driver.find_element(By.XPATH, self.password_xpath).send_keys(vendor_password)


def submit_vendor_login(self):
    self.driver.find_element(By.XPATH, self.login_xpath).click()


def click_venue_lead(self):
    self.driver.find_element(By.XPATH, self.venue_lead_select_xpath).click()


def click_venue_add_new_leads(self):
    self.driver.find_element(By.XPATH, self.add_lead_xpath).click()


def select_venue_name(self):
    # venue_name = self.driver.find_element(By.XPATH,self.click_venuename_xpath).click()
    #  self.driver.find_element(By.XPATH,self.select_venue_name_xpath).click()

    venues_name = ui.WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "(//*[@class='selectpicker form-control'])[1]")))
    # venues_name =  self.driver.find_element(By.XPATH,"(//*[@class='selectpicker form-control'])[1]")
    dropdown_venues_name = Select(venues_name)
    dropdown_venues_name.select_by_value("57*20*Al Aweer Meeting Room 2")

    # venue_name_search = self.driver.find_element(By.XPATH, self.venue_name_search_xpath)
    # venue_name_search.send_keys("Python")
    # venue_name_search.send_keys(Keys.ARROW_DOWN)
    # venue_name_search.send_keys(Keys.ENTER)


def Add_OtherBH(self, other_bh, otherBh_email, otherBh_conatct):
    self.driver.find_element(By.XPATH, self.OtherBH_Name_xpath).send_keys(other_bh)
    self.driver.find_element(By.XPATH, self.OtherBH_Email_xpath).send_keys(otherBh_email)
    self.driver.find_element(By.XPATH, self.OtherBH_ContactNo_xpath).send_keys(otherBh_conatct)

    AddMore_BH = self.driver.find_element(By.XPATH, self.Add_MoreBH_xpath)

    if AddMore_BH.click():
        self.driver.find_element(By.XPATH, self.OtherBH_Name_xpath).send_keys(other_bh)
        self.driver.find_element(By.XPATH, self.OtherBH_Email_xpath).send_keys(otherBh_email)
        self.driver.find_element(By.XPATH, self.OtherBH_ContactNo_xpath).send_keys(otherBh_conatct)


def enter_cust_name(self, cust_name):
    self.driver.find_element(By.XPATH, self.customer_name_xpath).send_keys(cust_name)


def enter_cust_id(self, cust_mail):
    self.driver.find_element(By.XPATH, self.cust_mail_id_xpath).send_keys(cust_mail)


def select_event_type(self):
    event_type = self.driver.find_element(By.XPATH, self.event_type_xpath)
    event_type_dropdown = Select(event_type)
    event_type_dropdown.select_by_value("Anniversary")


def enter_phone_number(self, phone_no):
    self.driver.find_element(By.XPATH, self.mobile_no_xpath).send_keys(phone_no)


def enter_event_date(self):
    date = self.driver.find_element(By.XPATH, self.event_date_xpath).send_keys('25May', Keys.TAB, '2023')


def enter_event_time(self, event_time):
    self.driver.find_element(By.XPATH, self.event_type_xpath).send_keys(event_time)


def enter_no_of_people(self, no_of_people):
    self.driver.find_element(By.XPATH, self.no_of_people_xpath).send_keys(no_of_people)


def enter_budget(self, budget):
    self.driver.find_element(By.XPATH, self.budget_xpath).send_keys(budget)


def enter_additional_info(self, additional_info):
    self.driver.find_element(By.XPATH, self.additional_info_xpath).send_keys(additional_info)


def select_source(self):
    source = self.driver.find_element(By.XPATH, self.source_xpath)
    source_dropdown = Select(source)
    source_dropdown.select_by_value("Google")


def select_channel(self):
    channel = self.driver.find_element(By.XPATH, self.channel_xpath)
    channel_dropdown = Select(channel)
    channel_dropdown.select_by_value("Personal")


def enter_menu(self, add_menu):
    self.driver.find_element(By.XPATH, self.add_menu_xpath).send_keys(add_menu)


def enter_note(self, Note):
    self.driver.find_element(By.XPATH, self.note_xpath).send_keys(Note)


def Add_Lead(self):
    self.driver.find_element(By.XPATH, self.Add_Lead_xpath).click()


def test_customer_page():
    driver.implicitly_wait(40)
    driver.maximize_window()
    driver.get(zoomvenuesurl)
    click_vendor_login()
    close_popup()
