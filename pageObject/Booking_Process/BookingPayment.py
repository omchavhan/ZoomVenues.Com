
import pyperclip
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BookingPayment:
    click_Action_booking_xpath = "(//*[@title='Create Booking'])[1]"
    click_booking_xpath = "//*[@class='btn btn-primary booking_btn']"
    click_yes_xpath = "//*[@class='swal2-confirm swal2-styled']"
    click_no_xpath = "//*[@class='swal2-deny swal2-styled']"
    copy_link_xpath = "//*[@class='btn btn-success']"
    click_ok_xpath = "//*[@class='swal2-confirm swal2-styled']"
    close_page_xpath = "//*[@class='btn btn-warning']"
    click_pay_xpath = "//*[@class='btn btn-block btn-success text-uppercase']"
    card_no_xpath = "//*[@class='cardNumberInput input top']"
    card_exp_date_xpath = "//*[@id='cc-exp']"
    cvv_no_xpath = "//*[@id='cc-csc']"
    final_pay_xpath = "//*[@class='iconTick']"

    def __init__(self,driver):
        self.driver = driver

    def click_Action_booking(self):
        self.driver.find_element(By.XPATH,self.click_Action_booking_xpath).click()

    def click_booking(self):
        self.driver.find_element(By.XPATH,self.click_booking_xpath).click()

    def click_yes(self):
        self.driver.find_element(By.XPATH, self.click_yes_xpath).click()

        # try:
        #     self.wait = WebDriverWait(self.driver, 9)
        #     element = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.click_yes_xpath)))
        #     print("Element Clicked")
        #
        # except Exception as e:
        #     print("Element not Cliked")

    def copy_link(self):
        self.driver.find_element(By.XPATH, self.copy_link_xpath).click()
        # self.action = ActionChains(self.driver)
        # self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

    def click_ok(self):
        self.driver.find_element(By.XPATH, self.click_ok_xpath).click()

    def close_page(self):
        self.driver.find_element(By.XPATH, self.close_page_xpath).click()

    def link_open_newTab(self):
        action = ActionChains(self.driver)
        # self.driver.execute_script("window.open('about:blank','_blank');")
        new_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(new_tab)
        self.driver.get(pyperclip.paste())

    def click_payment(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,self.click_pay_xpath).click()

    def insert_cardNo(self,card_no):
        self.driver.find_element(By.XPATH, self.card_no_xpath).send_keys(card_no)

    def insert_card_exp(self,card_exp_date):
        self.driver.find_element(By.XPATH, self.card_exp_date_xpath).send_keys(card_exp_date)

    def insert_card_CVV(self,card_cvv):
        self.driver.find_element(By.XPATH, self.cvv_no_xpath).send_keys(card_cvv)

    def click_final_pay(self):
        self.driver.find_element(By.XPATH, self.final_pay_xpath).click()














