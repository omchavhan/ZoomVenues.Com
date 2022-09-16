from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time


class BusinesHubs:

    bhClick_link = "Business Hubs"
    click_edit_xpath = "(//*[@class='nav-icon fas fa-edit EditText'])[1]"
    bhNm_css = "#name"
    loc_xpath = "//*[@class='form-control pac-target-input']"
    jobTitle_css = "input[placeholder='Job Title']"
    fNm_xpath = "(//*[@class='form-control'])[5]"
    lNm_xpath = "(//*[@class='form-control'])[6]"
    mail_xpath = "//*[@id='email']"
    contact_xpath = "//*[@name='contact_phone']"
    ceoNm_css = "input[placeholder='CEO Contact Person Name']"
    ceoMail_css = "[placeholder='CEO Contract Person Email Id']"
    cafonm_css = "[placeholder='CAFO Name']"
    cadoMail_css = "[placeholder='CAFO Email Id']"
    uploadImg_xpath = "//*[@class='hubFile']"
    submit_xpath = "(//*[@class='btn btn-primary'])[1]"


    def __init__(self,driver):
        self.driver = driver


    def clickBH(self):
        self.driver.find_element(By.LINK_TEXT,self.bhClick_link).click()

    def clickEdit(self):
        self.driver.find_element(By.XPATH,self.click_edit_xpath).click()

    def setBHnm(self,Bname):
        # self.driver.find_element(By.XPATH, self.bhNm_xpath).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.bhNm_css).send_keys(Bname)

    def setloc(self):
        que = self.driver.find_element(By.XPATH,self.loc_xpath)
        que.send_keys("Dubai")
        time.sleep(2)
        que.send_keys(Keys.ARROW_DOWN)
        que.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        que.send_keys(Keys.RETURN)

    def setjobTitle(self,title):
        self.driver.find_element(By.CSS_SELECTOR, self.jobTitle_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.jobTitle_css).send_keys(title)


    def setFname(self,Fname):
        self.driver.find_element(By.CSS_SELECTOR, self.fNm_xpath).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.jobTitle_css).send_keys(Fname)

    def setLname(self,Lname):
        self.driver.find_element(By.CSS_SELECTOR, self.lNm_xpath).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.jobTitle_css).send_keys(Lname)

    def setMail(self,Bmail):
        self.driver.find_element(By.CSS_SELECTOR, self.mail_xpath).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.mail_xpath).send_keys(Bmail)

    def setMobNo(self,mobNo):
        self.driver.find_element(By.XPATH, self.contact_xpath).clear()
        self.driver.find_element(By.XPATH, self.contact_xpath).send_keys(mobNo)

    def setCEONm(self,ceonm):
        self.driver.find_element(By.CSS_SELECTOR, self.ceoNm_css).send_keys(ceonm)

    def setCEOMail(self,ceoMail):
        self.driver.find_element(By.CSS_SELECTOR, self.ceoNm_css).send_keys(ceoMail)

    def setCAFONm(self,cafonm):
        self.driver.find_element(By.CSS_SELECTOR, self.cafonm_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.cafonm_css).send_keys(cafonm)

    def setCAFOmail(self,cafomail):
        self.driver.find_element(By.CSS_SELECTOR, self.cadoMail_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.cadoMail_css).send_keys(cafomail)

    def setuplodImg(self,uploadimg):
        self.driver.find_element(By.XPATH, self.uploadImg_xpath).send_keys(uploadimg)

    def setSubmit(self,submit):
        self.driver.find_element(By.XPATH, self.submit_xpath).send_keys(submit).click()










