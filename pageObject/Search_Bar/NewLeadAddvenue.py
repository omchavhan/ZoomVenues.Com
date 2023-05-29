# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class NewLeadflow:
    # Bellow Web Elements
    vendor_login_xpath = "(//a[@class='btn btn-default'])[2]"
    pop_up_close_xpath = "//div[@id='simpleModal']//span[@aria-hidden='true'][normalize-space()='×']"
    email_id_xpath = "//input[@id='user']"
    password_xpath = "//input[@id='password']"
    login_xpath = "//button[normalize-space()='Login']"
    venue_lead_select_xpath = "(//*[@href='http://vendor.zoomvenues.info/admin/enquiries/leads'])[1]"
    add_lead_xpath = "//a[normalize-space()='Add New Leads']"
    customer_name_xpath = "//input[@id='custname']"
    cust_mail_id_xpath = "//input[@id='email']"
    event_type_xpath = "//select[@id='event_type']"
    mobile_no_xpath = "//input[@id='phone']"
    event_date_xpath = "//input[@placeholder='Enter Event Date ']"
    event_time_xpath = "//input[@id='eventTime']"
    no_of_people_xpath = "//input[@id='people']"
    budget_xpath = "//label[normalize-space()='Budget (AED) (PPR)']"
    additional_info_xpath = "//textarea[@id='message']"
    source_xpath = "//select[@id='source']"
    channel_xpath = "//select[@id='channel']"
    add_menu_xpath = "//textarea[@id='menus']"
    note_xpath = "//textarea[@name='note']"

    def __int__(self,driver):
        self.driver = driver

    def click_vendor_login(self):
        self.driver.get_element(By.XPATH,self.vendor_login_xpath).click()

    def close_popup(self):
        self.driver.get_element(By.XPATH, self.pop_up_close_xpath).click()

    def enter_vendor_id(self,vendor_id ):
        self.driver.get_element(By.XPATH, self.email_id_xpath).send_keys(vendor_id)

    def enter_vendor_pass(self,vendor_password):
        self.driver.get_element(By.XPATH, self.email_id_xpath).send_keys(vendor_password)

    def submit_vendor_login(self):
        self.driver.get_element(By.XPATH, self.login_xpath).click()

    def click_venue_lead(self):
        self.driver.get_element(By.XPATH, self.venue_lead_select_xpath).click()

    def enter_cust_name(self,cust_name):
        self.driver.get_element(By.XPATH, self.customer_name_xpath).send_keys(cust_name)

    def enter_cust_id(self,cust_mail):
        self.driver.get_element(By.XPATH, self.cust_mail_id_xpath).send_keys(cust_mail)

    def select_event_type(self):
        event_type = self.driver.get_element(By.XPATH, self.event_type_xpath)
        event_type_dropdown = Select(event_type)
        event_type_dropdown.select_by_value("Anniversary")

    def enter_phone_number(self,phone_no):
        self.driver.get_element(By.XPATH, self.mobile_no_xpath).send_keys(phone_no)

    def enter_event_date(self,event_date):
        self.driver.get_element(By.XPATH, self.event_date_xpath).send_keys(event_date)

    def enter_event_time(self,event_time):
        self.driver.get_element(By.XPATH, self.event_type_xpath).send_keys(event_time)

    def enter_no_of_people(self,no_of_people):
        self.driver.get_element(By.XPATH, self.no_of_people_xpath).send_keys(no_of_people)

    def enter_budget(self,budget):
        self.driver.get_element(By.XPATH, self.budget_xpath).send_keys(budget)

    def enter_additional_info(self,additional_info):
        self.driver.get_element(By.XPATH, self.additional_info_xpath).send_keys(additional_info)

    def select_source(self):
        source = self.driver.get_element(By.XPATH, self.source_xpath)
        source_dropdown = Select(source)
        source_dropdown.select_by_value("Google")

    def select_channel(self):
        channel = self.driver.get_element(By.XPATH, self.channel_xpath)
        channel_dropdown = Select(channel)
        channel_dropdown.select_by_value("Personal")

    def enter_menu(self,add_menu):
        self.driver.get_element(By.XPATH, self.add_menu_xpath).send_keys(add_menu)

    def enter_note(self,Note):
        self.driver.get_element(By.XPATH, self.note_xpath).send_keys(Note)