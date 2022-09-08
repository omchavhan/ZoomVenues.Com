import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path="/chromedriver.exe")
zoomvenues_url = "https://zoomvenues.info/"


# --------------------------- Food Type ---------------------
def admin_logIn():
    driver.implicitly_wait(20)
    parent_page = driver.current_window_handle
    admin_signup = driver.find_element_by_xpath("(//*[@href='http://vendor.zoomvenues.info'])[1]").click()
    child_page = driver.window_handles
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            close_screen = driver.find_element_by_xpath("//a[normalize-space()='Close']").click()
            mail_id = driver.find_element_by_css_selector("#user")
            mail_id.send_keys("sales@zoomvenues.com")
            time.sleep(2)
            password = driver.find_element_by_css_selector("#password")
            password.send_keys("Zoomvenues*1212")
            time.sleep(2)
            login = driver.find_element_by_css_selector("#form-submit").click()


def food_menu():
    driver.implicitly_wait(20)
    driver.execute_script("window.scrollTo(0,2700)")
    click_food_menu = driver.find_element_by_css_selector("body > div:nth-child(1) > aside:nth-child(2) > div:nth-child(2) > nav:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > ul:nth-child(1) > li:nth-child(19)").click()

def add_foods():
    driver.implicitly_wait(20)
    click_add_food = driver.find_element_by_xpath("//a[@href='http://vendor.zoomvenues.info/admin/food/create']")
    driver.execute_script("arguments[0].click();",click_add_food)
    time.sleep(2)
    food_nm = driver.find_element_by_xpath("//input[@name='food_item']")
    food_nm.send_keys("Gajar Ka Halwa1")
    time.sleep(2)
    # food_type = driver.find_element_by_css_selector("input[value='Non-Veg']").click()
    food_type = driver.find_element_by_css_selector("input[value='Veg']").click()
    time.sleep(2)
    food_des = driver.find_element_by_css_selector("textarea[placeholder='About Food']")
    food_des.send_keys("Gajar Ka Halwa..........")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,700)")
    food_time1 = driver.find_element_by_css_selector("input[value='1'][name='food_time_id[]']").click()
    food_time2 = driver.find_element_by_css_selector("input[value='2'][name='food_time_id[]']").click()
    food_time3 = driver.find_element_by_css_selector("input[value='3'][name='food_time_id[]']").click()
    food_time4 = driver.find_element_by_css_selector("input[value='4'][name='food_time_id[]']").click()
    time.sleep(2)
    food_cuisine1 = driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[5]/div[2]/div[1]/ul[1]/li[2]/input[1]").click()
    food_cuisine2 = driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[5]/div[2]/div[1]/ul[1]/li[1]/input[1]").click()
    food_cuisine3 = driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[5]/div[2]/div[1]/ul[1]/li[3]/input[1]").click()
    food_cuisine4 = driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[5]/div[2]/div[1]/ul[1]/li[4]/input[1]").click()
    food_cuisine5 = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div/div/div/form/div[2]/div[5]/div[2]/div/ul/li[5]/input").click()
    food_cuisine6 = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div/div/div/form/div[2]/div[5]/div[2]/div/ul/li[6]/input").click()
    time.sleep(2)
    manu_type1 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div/div/div/div/form/div[2]/div[6]/div[2]/div/ul/li[1]/input").click()
    menu_type2 = driver.find_element_by_css_selector("input[value='2'][name='food_type_id[]']").click()
    menu_type3 = driver.find_element_by_css_selector("input[value='3'][name='food_type_id[]']").click()
    menu_type4 = driver.find_element_by_css_selector("input[value='5']").click()
    menu_type5 = driver.find_element_by_css_selector("input[value='6']").click()
    time.sleep(2)
    Frequently_use = driver.find_element_by_css_selector("input[value='1'][name='is_frequent']").click()
    time.sleep(2)
    submit = driver.find_element_by_css_selector("input[value='Submit']").click()


def food_list_edit_food():
    driver.implicitly_wait(20)
    food_list = driver.find_element_by_css_selector("a[class='btn btn-outline-primary float-right']").click()

def food_list_food_menu_dropdown():
    driver.implicitly_wait(20)
    driver.execute_script("window.scrollTo(0,700)")
    food_list = driver.find_element_by_xpath("//a[@href='http://vendor.zoomvenues.info/admin/food/list']")
    driver.execute_script("arguments[0].click();",food_list)
    time.sleep(3)


def view_food():
    driver.implicitly_wait(20)
    view_f = driver.find_element_by_xpath("//a[@href='http://vendor.zoomvenues.info/admin/food/view/9']").click()


def add_food_food_list():
    driver.implicitly_wait(20)
    food_list = driver.find_element_by_xpath("//a[contains(text(),'Food List')]").click()

def food_list_Home():
    driver.implicitly_wait(20)
    food_list = driver.find_element_by_xpath("//a[normalize-space()='Home']").click()
    time.sleep(2)

def edit():
    driver.implicitly_wait(20)
    Edit = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/food/edit/11']").click()
    time.sleep(2)
    food_nm = driver.find_element_by_css_selector("input[placeholder='Butter Chicken']").clear()
    food_nm = driver.find_element_by_css_selector("input[placeholder='Butter Chicken']")
    food_nm.send_keys("Stir-fried Beef with Oyster Sauce")
    time.sleep(2)
    food_type = driver.find_element_by_css_selector("input[value='Non-Veg']").click()
    time.sleep(2)
    food_des = driver.find_element_by_css_selector("textarea[placeholder='About Food']").clear()
    food_des = driver.find_element_by_css_selector("textarea[placeholder='About Food']")
    food_des.send_keys("Stir-fried Beef with Oyster Sauce------------")
    time.sleep(2)
    food_time = driver.find_element_by_css_selector("input[value='2'][name='food_time_id[]']").click()
    time.sleep(2)
    food_cuisine = driver.find_element_by_css_selector("input[value='   2']").click()
    time.sleep(2)
    menu_type = driver.find_element_by_css_selector("input[value='4'][name='food_type_id[]']").click()
    time.sleep(2)
    update = driver.find_element_by_css_selector("input[value='Update']").click()

# --------------------------------------------------------------------------------------------------------
# ------------------ Menu List ---------

def admin_logIn_menu_list():
    driver.implicitly_wait(20)
    parent_page = driver.current_window_handle
    admin_signup = driver.find_element_by_xpath("//*[@id='main']/header/div[2]/a").click()
    child_page = driver.window_handles
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            close_screen = driver.find_element_by_xpath("//a[@href='#close-modal']").click()
            mail_id = driver.find_element_by_css_selector("#user")
            mail_id.send_keys("hisham.kassem@crowneplazadubai.com")
            time.sleep(2)
            password = driver.find_element_by_css_selector("#password")
            password.send_keys("12345678")
            time.sleep(2)
            login = driver.find_element_by_css_selector("#form-submit").click()


def Menu_list():
    driver.implicitly_wait(20)
    driver.execute_script("window.scrollTo(0,600)")
    click_menu_list = driver.find_element_by_xpath("(//*[@class='nav-link'])[7]").click()
    time.sleep(2)
    click_add_menu = driver.find_element_by_link_text("Add Menu").click()
    time.sleep(2)

def Add_Menu():
    driver.implicitly_wait(20)
    menu_card_name = driver.find_element_by_css_selector("input[placeholder='Menu Card Name']")
    menu_card_name.send_keys("GALA DINNER BUFFET MENU 115")
    time.sleep(2)
    menu_description = driver.find_element_by_xpath("//*[@name='menu_card_details']")
    menu_description.send_keys("Indian Menu – 1")
    time.sleep(2)
    Frequently_use = driver.find_element_by_xpath("(//*[@name='if_frequently_used'])[1]").click()
    time.sleep(2)
    Price = driver.find_element_by_css_selector("input[placeholder='Menu Card Price']")
    Price.send_keys("135/-")
    time.sleep(2)
    Cuisine = driver.find_element_by_xpath("//*[@id='Indian']").click()
    time.sleep(3)
    Submit = driver.find_element_by_xpath("//*[@id='submit']").click()



def Config_Menu_card():
    driver.implicitly_wait(20)
    driver.execute_script("window.scrollTo(0,600)")
    select_menu_card = driver.find_element_by_xpath("//*[@id='food_types']")
    dropdown_menu_type = Select(select_menu_card)
    dropdown_menu_type.select_by_visible_text("Soup")
    time.sleep(2)
    food_items = driver.find_element_by_xpath("//*[@class='form-control mdb-select md-form']")
    dropdown_food_item = Select(food_items)
    dropdown_food_item.select_by_visible_text("Soup Non Veg 1")
    time.sleep(2)
    add_food_item = driver.find_element_by_xpath("//*[@class='btn btn-secondary']")


# -------------------------------Business Hubs ---------------------------


def Business_Hubs():
    driver.implicitly_wait(20)
    click_business_hubs = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/hubs/all']").click()
    time.sleep(2)
    TestHub_View = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/hubs/show/166']").click()
    time.sleep(2)
    Approve = driver.find_element_by_css_selector("button[type='submit']").click()


def Leads():
    driver.implicitly_wait(20)
    click_lead = driver.find_element_by_xpath("(//*[@href='http://vendor.zoomvenues.info/admin/enquiries/leads'])[1]").click()


def add_new_lead():
    driver.implicitly_wait(20)
    click_add_lead = driver.find_element_by_link_text("Add Leads").click()
    venue_name = driver.find_element_by_xpath("(//*[text()='-Select Venue-'])[2]").click()
    time.sleep(2)
    select_venue_name = driver.find_element_by_xpath("(//*[text()='Other (Other)'])[2]")
    driver.execute_script("arguments[0].click();",select_venue_name)
    time.sleep(2)
    cust_nm = driver.find_element_by_css_selector("input[placeholder='Enter Customer Name']")
    cust_nm.send_keys("Gayl")
    time.sleep(2)
    cust_mail = driver.find_element_by_css_selector("input[placeholder='Email Address*']")
    cust_mail.send_keys("omworld01@gmail.com")
    time.sleep(2)
    event_type = driver.find_element_by_id("event_type")
    dropdown_event_type = Select(event_type)
    dropdown_event_type.select_by_visible_text("Birthday")
    click_phone_no = driver.find_element_by_xpath("//*[@class='iti__selected-flag']").click()
    select_india_phone_code = driver.find_element_by_xpath("(//*[text()='India (भारत)'])[1]").click()
    write_phone_no = driver.find_element_by_css_selector("input[placeholder='Enter Customer Phone Number']")
    write_phone_no.send_keys("9158333486")
    event_date = driver.find_element_by_css_selector("input[placeholder='Enter Event Date ']")
    event_date.send_keys("27-07-2022")
    event_time = driver.find_element_by_css_selector("input[placeholder='Enter Time']")
    event_time.send_keys("03:46PM")
    no_of_people = driver.find_element_by_css_selector("input[placeholder='Enter no of people']")
    no_of_people.send_keys("100")
    bugest = driver.find_element_by_css_selector("input[placeholder='Enter Budget ']")
    bugest.send_keys(20)
    additional_info =driver.find_element_by_xpath("(//*[@class='form-control'])[13]")
    additional_info.send_keys("best venues....")
    source = driver.find_element_by_xpath("//*[@id='source']")
    dropdown_select_source = Select(source)
    dropdown_select_source.select_by_visible_text("Web")
    time.sleep(2)
    channal = driver.find_element_by_xpath("//*[@id='channel']")
    dropdown_select_channal = Select(channal)
    dropdown_select_channal.select_by_visible_text("Personal")
    note = driver.find_element_by_css_selector("textarea[name='note']")
    note.send_keys("nothing ---------")
    add_enquiry = driver.find_element_by_css_selector("input[type='submit']").click()



def Edit_and_updateLead():
    driver.implicitly_wait(20)
    click_action_edit = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/enquiries/editleads/313']").click()

    click_update_lead = driver.find_element_by_css_selector("input[type='submit']").click()




# ----------------------- Business Hubs ---------------------


def Business_Hub_click():
    driver.implicitly_wait(20)
    click_business_hub = driver.find_element_by_xpath("//*[text()='Business Hubs']").click()
    click_push_menu = driver.find_element_by_css_selector(".fas.fa-bars").click()

def Business_Hub_Edit():
    driver.implicitly_wait(20)
    click_business_hub = driver.find_element_by_xpath("//*[text()='Business Hubs']").click()
    click_pushmenu = driver.find_element_by_xpath("//*[@class='fas fa-bars']").click()
    click_edit = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/hubs/edit/168']").click()
    click_businesshub_name = driver.find_element_by_css_selector("input[placeholder='Enter Hub Name']").clear()
    click_businesshub_name = driver.find_element_by_css_selector("input[placeholder='Enter Hub Name']")
    click_businesshub_name.send_keys("infoTeck")
    click_description = driver.find_element_by_css_selector("p[data-placeholder='Place some text here upto 50 to 1000 characters']")
    click_description.send_keys(" ZoomVenuessssss")
    time.sleep(2)
    click_Loction = driver.find_element_by_css_selector("input[placeholder='Enter a location']").clear()
    click_Loction = driver.find_element_by_css_selector("input[placeholder='Enter a location']")
    click_Loction.send_keys("Dubai - United Arab Emirates")
    time.sleep(2)
    click_Loction.send_keys(Keys.ARROW_DOWN)
    click_Loction.send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    click_Loction.send_keys(Keys.ENTER)
    click_job_title = driver.find_element_by_xpath("//*[@id='job_title']").clear()
    click_job_title = driver.find_element_by_xpath("//*[@id='job_title']")
    click_job_title.send_keys("testinggggggggggg")
    click_logo_upload = driver.find_element_by_xpath("//*[@id='hubFile']")
    click_logo_upload.send_keys("C:\\Users\\GiTESH SONAR\\PycharmProjects\\GoogleAuto\\ZoomVenues\\imgs\\marten-bjork-n_IKQDCyrG0-unsplash.jpg")
    click_date = driver.find_element_by_xpath("//*[@id='datepicker']").clear()
    click_date_btn = driver.find_element_by_xpath("//*[@id='datepicker']").click()
    click_date = driver.find_element_by_xpath("//td[normalize-space()='30']").click()
    submit = driver.find_element_by_xpath("//button[normalize-space()='Submit']")
    driver.execute_script("arguments[0].scrollIntoView();", submit)
    submit.click()

def Click_View():
    driver.implicitly_wait(20)
    click_pushmenu = driver.find_element_by_xpath("//*[@class='fas fa-bars']").click()
    click_view = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/hubs/show/168']").click()
    # comments = driver.find_element_by_xpath("//textarea[@name='comments']").send_keys("sdnclks")
    disapprove = driver.find_element_by_xpath("(//*[@class='btn btn-primary'])[1]").click()
    click_business_hub = driver.find_element_by_xpath("//*[text()='Business Hubs']").click()

def Click_venues_list():
    driver.implicitly_wait(20)
    click_pushmenu = driver.find_element_by_xpath("//*[@class='fas fa-bars']").click()
    venues_list = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/venues/all/168']").click()
    click_business_hub = driver.find_element_by_xpath("//*[text()='Business Hubs']").click()

def Click_packages_list():
    driver.implicitly_wait(20)
    click_pushmenu = driver.find_element_by_xpath("//*[@class='fas fa-bars']").click()
    driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/hubs/packages/168']").click()
    click_business_hub = driver.find_element_by_xpath("//*[text()='Business Hubs']").click()

def Click_download_pdf():
    driver.implicitly_wait(20)
    click_pushmenu = driver.find_element_by_xpath("//*[@class='fas fa-bars']").click()
    driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/displayContract/168']").click()
    click_business_hub = driver.find_element_by_xpath("//*[text()='Business Hubs']").click()


def Click_BH_Bank_Detial():
    driver.implicitly_wait(20)
    click_contact_person = driver.find_element_by_css_selector("[placeholder='Enter  Name']")
    click_contact_person.send_keys("[placeholder='Enter  Name']")
    click_contact_person.send_keys("om1")
    click_pin_code = driver.find_element_by_xpath("//form[@id='formVendorSignup']//div[@class='iti__selected-dial-code'][normalize-space()='+971']").click()
    time.sleep(2)
    pin_code_india = driver.find_element_by_xpath("(//span[@class='iti__country-name'][contains(text(),'India (भारत)')])[1]").click()
    contact = driver.find_element_by_xpath("//input[@class='form-control contact_number']")
    contact.send_keys("9158333486")
    time.sleep(2)
    click_accound_holder_name = driver.find_element_by_css_selector("placeholder='Account Name'")
    click_accound_holder_name.send_keys("om chavan Testing")
    click_bank_name = driver.find_element_by_xpath("(//*[@class='form-control'])[14]")
    click_bank_name.send_keys("BOM")
    click_acc_number = driver.find_element_by_xpath("//*[@id='acc_number']")
    click_acc_number.send_keys("123456789012")
    click_re_acc_number = driver.find_element_by_xpath("//*[@id='re_acc_number']")



#--------------------- Business Hubs Leads -------------------------------------------------

def Click_Business_hubs_leads():
    driver.implicitly_wait(5)
    click_business_hubs = driver.find_element_by_xpath("//*[text()='Business Hubs Leads']").click()

def Add_new_Business_hubs_leads():
    driver.implicitly_wait(5)
    new_add = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/hub/add']").click()
    click_pushmenu = driver.find_element_by_xpath("//*[@class='fas fa-bars']").click()
    other_business_hub_name = driver.find_element_by_css_selector("[placeholder='Enter Hub Name']")
    other_business_hub_name.send_keys("HP Business hub name")
    f_name = driver.find_element_by_xpath("(//input[@id='first_name'])[1]")
    f_name.send_keys("ganesh")
    l_name = driver.find_element_by_css_selector("#last_name")
    l_name.send_keys("sir")
    location = driver.find_element_by_css_selector("[placeholder='Enter a location']")
    location.send_keys("Dubai")
    location.send_keys(Keys.TAB)
    job_title = driver.find_element_by_css_selector("[placeholder='Job Title']")
    job_title.send_keys("Tester")
    contract_person_name = driver.find_element_by_xpath("//*[@name='business_hub_contact_person_name']")
    contract_person_name.send_keys("om chavan")
    business_hub_email = driver.find_element_by_xpath("//*[@name='business_hub_email']")
    business_hub_email.send_keys("omworld013443@gmail.com")
    mobile_no = driver.find_element_by_xpath("//*[@name='business_hub_contact']")
    mobile_no.send_keys("9158333486")
    commission = driver.find_element_by_xpath("//*[@class='form-control pull-right']")
    commission.send_keys("10")
    website_url = driver.find_element_by_css_selector("#business_hub_web_url")
    website_url.send_keys("https://www.w3schools.com/python/")
    submit = driver.find_element_by_xpath("//*[text()='Submit']").click()


def Edit_business_hubs_lead():
    driver.implicitly_wait(5)
    click_pushmenu = driver.find_element_by_xpath("//*[@class='fas fa-bars']").click()
    click_edit = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/hub/edit/60']")
    driver.execute_script("arguments[0].scrollIntoView();", click_edit)
    click_edit.click()
    submit = driver.find_element_by_xpath("//*[text()='Submit']").click()

def View_business_hubs_lead():
    driver.implicitly_wait(5)
    click_pushmenu = driver.find_element_by_xpath("//*[@class='fas fa-bars']").click()
    click_view = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/hub/show/60']")
    driver.execute_script("arguments[0].scrollIntoView();", click_view)
    click_view.click()
    enter_comments = driver.find_element_by_xpath("(//*[@placeholder='Place some text here'])[1]")
    enter_comments.send_keys("automtion testing for create")
    add_response = driver.find_element_by_xpath("//*[text()='Add Response']").click()


# --------------------------------  Renewal Users --------------------

def Renewal_Users():
    driver.implicitly_wait(5)
    click_renewal_users = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/users/renewal']").click()
    click_action_view = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/hubs/show/19']").click()
    click_message = driver.find_element_by_xpath("//*[@class='btn btn-primary float-right']").click()
    enter_message = driver.find_element_by_xpath("(//*[@placeholder='Place some text here'])[2]")
    enter_message.send_keys("Testing so ignore")
    click_send = driver.find_element_by_xpath("(//*[@class='btn btn-primary'])[2]").click()
    time.sleep(2)
    driver.switch_to.alert.accept()
    time.sleep(2)
    click_close = driver.find_element_by_xpath("//*[@class='btn btn-default']").click()
    comments = driver.find_element_by_xpath("//*[@class='textarea']")
    comments.send_keys("Testing so ingnore this")
    approve_or_disapprove = driver.find_element_by_xpath("(//*[@class='btn btn-primary'])[1]").click()


# --------------------------- Venues -------------------------------------------------


def Venues_Promoted():
    driver.implicitly_wait(5)
    click_venues = driver.find_element_by_xpath("(//*[@href='http://vendor.zoomvenues.info/admin/venues/all'])[1]").click()
    click_promote = driver.find_element_by_xpath("(//a[@title='Promote'][normalize-space()='Promote'])[2]").click()
    click_date = driver.find_element_by_xpath("//*[@name='fromDate']").click()
    i = 0
    while i == 0:
        title = driver.find_element_by_xpath("(//*[@class='datepicker-switch'])[1]").text
        if title == "August 2022" or title != "August 2022":
            driver.find_element_by_xpath("//div[@class='datepicker-days']//th[@class='next'][normalize-space()='»']").click()
            time.sleep(2)
        else:
            break
    select_date = driver.find_element_by_xpath("//td[@class='day'][normalize-space()='1']").click()

    # click_start_date = driver.find_element_by_xpath("//*[@id='fromDate']").click()
    # select_date = driver.find_element_by_xpath("//td[@class='day'][normalize-space()='1']").click()
    # click_End_date = driver.find_element_by_xpath("//*[@id='toDate']").click()
    # select_date = driver.find_element_by_xpath("//td[normalize-space()='30']").click()
    # promoted_flag1 = driver.find_element_by_xpath("//*[@id='promotedflag']").click()
    # click_update = driver.find_element_by_xpath("(//*[@class='btn btn-primary'])[1]").click()

def Venues_Feature():
    driver.implicitly_wait(5)
    click_venues = driver.find_element_by_xpath("(//*[@href='http://vendor.zoomvenues.info/admin/venues/all'])[1]").click()
    click_feature = driver.find_element_by_xpath("(//a[@title='Feature'][normalize-space()='Feature'])[1]").click()
    upload_img = driver.find_element_by_xpath("//*[@name='image']")
    # upload_img.send_keys("C:\\Users\GiTESH SONAR\\PycharmProjects\\GoogleAuto\\ZoomVenues\\imgs\\marten-bjork-n_IKQDCyrG0-unsplash.jpg")
    click_from_date = driver.find_element_by_xpath("//*[@name='featuredfromDate']").click()
    select_from_date = driver.find_element_by_xpath("//td[@class='day'][normalize-space()='29']").click()
    click_end_date = driver.find_element_by_xpath("//input[@id='featuredtoDate']").click()
    select_end_date = driver.find_element_by_xpath("//td[@class='day'][normalize-space()='30']").click()
    promoted_flag2 = driver.find_element_by_xpath("//input[@id='featuredflag']").click()
    click_update = driver.find_element_by_xpath("(//*[@class='btn btn-primary'])[2]").click()





def Venues_Edit():
   driver.implicitly_wait(5)
   click_venues = driver.find_element_by_xpath("(//*[@href='http://vendor.zoomvenues.info/admin/venues/all'])[1]").click()
   click_edit_venue = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/venues/edit/44']").click()
   click_name = driver.find_element_by_css_selector("[placeholder='Name']").clear()
   click_name = driver.find_element_by_css_selector("[placeholder='Name']")
   click_name.send_keys("Testing")
   # description
   click_paragaph = driver.find_element_by_xpath("//button[@class='ck ck-button ck-off ck-button_with-text ck-dropdown__button']").click()
   select_style = driver.find_element_by_xpath("(//button[@class='ck ck-button ck-heading_heading3 ck-off ck-button_with-text'])[1]").click()
   click_description = driver.find_element_by_xpath("//div[@aria-label='Rich Text Editor, main']")
   click_description.send_keys("  Testing plz ingnor   ")
   click_listing_type = driver.find_element_by_xpath("//*[@name='listing_type']")
   dropdown_listing_type = Select(click_listing_type)
   dropdown_listing_type.select_by_visible_text("Work Venue")
   click_location = driver.find_element_by_css_selector("[value='Casablanca Road , Al Garhoud , Dubai ,United Arab Emirates.']").clear()
   click_location = driver.find_element_by_css_selector("[value='Casablanca Road , Al Garhoud , Dubai ,United Arab Emirates.']")
   click_location.send_keys("Dubai")
   time.sleep(2)
   click_location.send_keys(Keys.ARROW_DOWN)
   time.sleep(2)
   click_location.send_keys(Keys.RETURN)

   # upload_photos = WebDriverWait(driver, 50).until(EC.invisibility_of_element((By.XPATH, "//*[@class='row imageRow']")))
   # driver.execute_script("arguments[0].scrollIntoView();", upload_photos)
   # upload_photos = driver.find_element_by_xpath("//*[@class='row imageRow']")
   # upload_photos.send_keys("C:\\Users\\GiTESH SONAR\\PycharmProjects\\GoogleAuto\\ZoomVenues\\imgs\\marten-bjork-n_IKQDCyrG0-unsplash.jpg")
   # upload_photos.send_keys(Keys.TAB)

   seating_arrangement = driver.find_element_by_xpath("(//*[@class='form-check-input arrangements'])[6]").click()
   capacity_min = driver.find_element_by_css_selector("input[placeholder='Min people capacity']").clear()
   capacity_min = driver.find_element_by_css_selector("input[placeholder='Min people capacity']")
   capacity_min.send_keys(20)
   capacity_max = driver.find_element_by_xpath("//*[@id='bhName']").clear()
   capacity_max = driver.find_element_by_xpath("//*[@id='bhName']")
   capacity_max.send_keys("25")
   area_sqm = driver.find_element_by_css_selector("[placeholder='sqm']").clear()
   area_sqm = driver.find_element_by_css_selector("[placeholder='sqm']")
   area_sqm.send_keys("123")
   area_sqft = driver.find_element_by_xpath("//*[@name='areasqft']").clear()
   area_sqft = driver.find_element_by_xpath("//*[@name='areasqft']")
   area_sqft.send_keys("1234")

   venue_type = driver.find_element_by_xpath("(//*[@class='form-check-input venueTypes'])[3]").click()
   # venue_type = driver.find_element_by_class_name("form-check-input venueTypes").text
   # print(venue_type)

   areacity_type = driver.find_element_by_xpath("//*[@id='area_city']")
   dropdown_areacity_type = Select(areacity_type)
   # dropdown_areacity_type.deselect_by_visible_text("Dubai")
   dropdown_areacity_type.select_by_visible_text("Abu Dhabi")

   rating = driver.find_element_by_xpath("//*[@id='ratings']")
   dropdown_rating = Select(rating)
   dropdown_rating.select_by_visible_text("5 Star")

   title = driver.find_element_by_xpath("//*[@class='title form-control']")
   title.send_keys("testing")
   submit = driver.find_element_by_xpath("//*[@value='submit']").click()



def Venues_Edit_360():
    driver.implicitly_wait(20)
    click_venues = driver.find_element_by_xpath("(//*[@href='http://vendor.zoomvenues.info/admin/venues/all'])[1]").click()
    click_edit_360 = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/venues/edit-photo/229']").click()
    time.sleep(2)
    click_photo_upload = driver.find_element_by_xpath("//*[@class='col-sm-12 imageSectionDiv imageVenueSectionThree']")
    # click_photo_upload  = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='row imageRow']")))
    click_photo_upload.send_keys("C:\\Users\\GiTESH SONAR\\PycharmProjects\\GoogleAuto\\ZoomVenues\\imgs\\marten-bjork-n_IKQDCyrG0-unsplash.jpg")

    venue_img_link = driver.find_element_by_css_selector("[placeholder='Venue Image Link']")
    venue_img_link.send_keys("imges testing")
    sumbit = driver.find_element_by_css_selector("[value='submit']").click()


def Venues_Add_360():
    driver.implicitly_wait(20)
    click_venues = driver.find_element_by_xpath("(//*[@href='http://vendor.zoomvenues.info/admin/venues/all'])[1]").click()
    click_edit_360 = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/venues/add-photo/229']").click()

    # time.sleep(5)
    # # click_photo_upload = driver.find_element_by_xpath("//*[@class='col-sm-12 imageSectionDiv imageVenueSectionThree']")
    # click_photo_upload  = WebDriverWait(driver, 30).until(EC.invisibility_of_element((By.XPATH, "//*[@class='row imageRow']")))
    # click_photo_upload.send_keys("C:\\Users\\GiTESH SONAR\\PycharmProjects\\GoogleAuto\\ZoomVenues\\imgs\\marten-bjork-n_IKQDCyrG0-unsplash.jpg")
    #
    venue_img_link = driver.find_element_by_xpath("//*[@name='venueImageLink']")
    # venue_img_link = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "[placeholder='Venue Image Link']")))
    venue_img_link.send_keys("imges testing")
    sumbit = driver.find_element_by_css_selector("[value='submit']").click()


def Venue_View():
    driver.implicitly_wait(5)
    click_venues = driver.find_element_by_xpath("(//*[@href='http://vendor.zoomvenues.info/admin/venues/all'])[1]").click()
    search = driver.find_element_by_xpath("//*[@class='form-control form-control-sm']")
    search.send_keys("Hall A - The Oberoi Dubai")
    time.sleep(1)
    click_view = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/venues/show/229']").click()
    time.sleep(1)

    click_approve = driver.find_element_by_xpath("//*[text()='Approve']").click()
    click_disapprove = driver.find_element_by_xpath("//*[text()='Disapprove']").click()





# ------------------------------------ service provider-------------------------

def Service_Provider_Click():
    driver.implicitly_wait(20)
    click_service_provider = driver.find_element_by_link_text("Service Providers").click()

def Service_Provider_Edit():
    driver.implicitly_wait(20)
    click_edit = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/serviceProviders/edit/456']").click()
    click_first_name = driver.find_element_by_css_selector("[placeholder='First Name']").clear()
    click_first_name = driver.find_element_by_css_selector("[placeholder='First Name']")
    click_first_name.send_keys(" Edit Fun ")

    click_Last_name = driver.find_element_by_css_selector("[placeholder='Last Name']").clear()
    click_Last_name = driver.find_element_by_css_selector("[placeholder='Last Name']")
    click_Last_name.send_keys(" Testing ")

    click_contact = driver.find_element_by_xpath("//*[@class='iti__selected-flag']").click()
    select_state_code = driver.find_element_by_xpath("//*[@id='iti-0__item-in-preferred']").click()
    click_mob_no = driver.find_element_by_xpath("//*[@name='contact_number']").clear()
    click_mob_no = driver.find_element_by_xpath("//*[@name='contact_number']")
    click_mob_no.send_keys("9158333486")

    click_mailId = driver.find_element_by_css_selector("[placeholder='Login Email']").clear()
    click_mailId = driver.find_element_by_css_selector("[placeholder='Login Email']")
    click_mailId.send_keys("omworld01111@gmail.com")

    click_photo = driver.find_element_by_css_selector(".userFile")
    click_photo.send_keys("C:\\Users\\GiTESH SONAR\\PycharmProjects\\GoogleAuto\\ZoomVenues\\imgs\\marten-bjork-n_IKQDCyrG0-unsplash.jpg")
    click_submit = driver.find_element_by_css_selector("[value='submit']").click()


def Service_Provitor_service_list():
    driver.implicitly_wait(10)
    click_service_list = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/services/all/456']").click()

def Service_Provider_Delete():
    driver.implicitly_wait(10)
    click_delete = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/serviceProviders/deleteone/418']").click()



# -------------------- My Booking  ------------------------------------------------------

def Click_My_Booking():
    driver.implicitly_wait(10)
    click_my_booking = driver.find_element_by_link_text("My Bookings").click()

def My_Booking_Click_Venue_Name():
    driver.implicitly_wait(10)
    click_venue_name = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/enquiries/venues/show/213']").click()
    driver.execute_script("window.scrollTo(0,2000)")
    time.sleep(2)
    click_close = driver.find_element_by_xpath("(//*[@href='http://vendor.zoomvenues.info/admin/enquiries/venues'])[3]").click()



# -------------------- Leads  -------------------------------------------------------------

def Click_Leads():
    driver.implicitly_wait(20)
    click_leads = driver.find_element_by_xpath("(//*[@href='http://vendor.zoomvenues.info/admin/enquiries/leads'])[1]").click()
    # click_pushmenu = driver.find_element_by_class_name("fas fa-bars").click()

def Lead_Action_Edit():
    driver.implicitly_wait(20)
    click_edit = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/enquiries/editleads-new/502']")
    driver.execute_script("arguments[0].scrollIntoView();", click_edit)
    click_edit.click()
    click_status = driver.find_element_by_xpath("//select[@id='status']")

    dropdown_lead_status = Select(click_status)
    dropdown_lead_status.select_by_index(2)
    # time.sleep(1)
    # dropdown_lead_status.select_by_index(1)
    click_uplead = driver.find_element_by_css_selector("[value='Update Lead']").click()
    time.sleep(1)
    click_venue_enquiry = driver.find_element_by_xpath("//input[@id='btnSubmitEnquiry']").click()


# def Leads_Add_Lead():
#     driver.implicitly_wait(20)
#     click_add_leads = driver.find_element_by_link_text("Add New Leads").click()
#     click_venue_name = driver.find_element_by_xpath("//select[@id='venues_id']")
#     dropdown_venue_name = Select(click_venue_name)
#     dropdown_venue_name.select_by_index(6)
#     time.sleep(1.5)
#
#     click_other_businessHub_name = driver.find_element_by_xpath("(//*[@class='form-control'])[2]")
#     click_other_businessHub_name.send_keys("Testing Hub")
#     click_other_businessHub_mail = driver.find_element_by_xpath("(//*[@class='form-control'])[4]")
#     click_other_businessHub_mail.send_keys("omworld01@gmail.com")
#     click_other_businessHub_contact = driver.find_element_by_xpath("(//*[@class='form-control'])[5]")
#     click_other_businessHub_contact.send_keys("9158333486")
#     click_custome_name = driver.find_element_by_xpath("(//*[@class='form-control'])[6]")
#     click_custome_name.send_keys("om chavan 2A")
#     click_custome_mail = driver.find_element_by_xpath("(//*[@class='form-control'])[7]")
#     click_custome_mail.send_keys("ombhagyeshchavan@gmail.com")
#     time.sleep(2)
#
#     click_event_type = driver.find_element_by_css_selector("#event_type")
#     dropdown_event_type = Select(click_event_type)
#     dropdown_event_type.select_by_visible_text("Birthday")
#     time.sleep(1.5)
#
#     click_contact = driver.find_element_by_xpath("//*[@class='iti__selected-flag']").click()
#     select_state_code = driver.find_element_by_xpath("//*[@id='iti-0__item-in-preferred']").click()
#     click_mob_no = driver.find_element_by_xpath("//input[@id='phone']")
#     click_mob_no.send_keys("9158333486")
#     time.sleep(1.5)
#
#     click_date = driver.find_element_by_css_selector("input[placeholder='Enter Event Date ']")
#     click_date.send_keys("02-09-2022")
#     time.sleep(1.5)
#
#     click_every_time = driver.find_element_by_xpath("//*[@id='eventTime']")
#     click_every_time.send_keys("06:03PM")
#     time.sleep(1.5)
#
#     click_no_people = driver.find_element_by_xpath("//*[@id='people']")
#     click_no_people.send_keys("200")
#     time.sleep(1.5)
#
#     click_budget = driver.find_element_by_xpath("//*[@id='budget']")
#     click_budget.send_keys("3456")
#     time.sleep(1.5)
#
#     click_addtional_information = driver.find_element_by_xpath("//textarea[@id='message']")
#     click_addtional_information.send_keys("aaaaaaaaa bbbbbbbbbb")
#     time.sleep(1.5)
#
#     click_source = driver.find_element_by_xpath("//select[@id='source']")
#     dropdown_source = Select(click_source)
#     dropdown_source.select_by_visible_text("LinkedIn")
#     time.sleep(1.5)
#
#     click_channel = driver.find_element_by_css_selector("#channel")
#     dropdown_channel = Select(click_channel)
#     dropdown_channel.select_by_index(2)
#     time.sleep(1.5)
#
#     click_note = driver.find_element_by_css_selector("textarea[name='note']")
#     click_note.send_keys("dsklmd,dsmclmcsdl")
#
#     click_add_enquiry = driver.find_element_by_xpath("//input[@id='btnSubmitEnquiry']").click()


def Leads_New_Other_BH():
    driver.implicitly_wait(20)
    lick_add_leads = driver.find_element_by_link_text("Add New Leads").click()
    click_venue = driver.find_element_by_xpath("(//*[@class='dropdown bootstrap-select show-tick form-control'])[2]")
    driver.execute_script("arguments[0].click();", click_venue)

    click_other_BH_nm = driver.find_element_by_xpath("//input[@id='other_business_hub_name']")
    click_other_BH_nm.send_keys("om 17/08 - 26")
    click_other_BH_mail = driver.find_element_by_xpath("(//input[@id='old_hub_email1'])[1]")
    click_other_BH_mail.send_keys("ommworld01@gmail.com")
    click_other_BH_contact = driver.find_element_by_xpath("(//input[@id='old_hub_contact1'])[1]")
    click_other_BH_contact.send_keys("1234567890")
    # click_add_other_BH = driver.find_element_by_xpath("//*[@id='addMoreOptions1']").click()
    # time.sleep(3)
    # click_other_BH_nm1 = driver.find_element_by_xpath("//input[@id='other_business_hub_name']").clear()
    # click_other_BH_nm1 = driver.find_element_by_xpath("//input[@id='other_business_hub_name']")
    # click_other_BH_nm1.send_keys("om 17/08 - 02")
    # click_other_BH_mail1 = driver.find_element_by_xpath("(//input[@id='old_hub_email1'])[1]").clear()
    # click_other_BH_mail1 = driver.find_element_by_xpath("(//input[@id='old_hub_email1'])[1]")
    # click_other_BH_mail1.send_keys("ombhagyesh@gmail.com")
    # click_other_BH_contact1 = driver.find_element_by_xpath("(//input[@id='old_hub_contact1'])[1]").clear()
    # click_other_BH_contact1 = driver.find_element_by_xpath("(//input[@id='old_hub_contact1'])[1]")
    # click_other_BH_contact1.send_keys("1234567899")

    click_custome_name = driver.find_element_by_xpath("//input[@id='custname']")
    click_custome_name.send_keys("om chavan 2Kk")
    click_custome_mail = driver.find_element_by_xpath("//input[@id='email']")
    click_custome_mail.send_keys("ombhagyeshchavan@gmail.com")
    time.sleep(2)

    click_event_type = driver.find_element_by_css_selector("#event_type")
    dropdown_event_type = Select(click_event_type)
    dropdown_event_type.select_by_visible_text("Birthday")
    time.sleep(1.5)

    click_contact = driver.find_element_by_xpath("//*[@class='iti__selected-flag']").click()
    select_state_code = driver.find_element_by_xpath("//*[@id='iti-0__item-in-preferred']").click()
    click_mob_no = driver.find_element_by_xpath("//input[@id='phone']")
    click_mob_no.send_keys("9158333488")
    time.sleep(1.5)

    click_date = driver.find_element_by_css_selector("input[placeholder='Enter Event Date ']")
    click_date.send_keys("03-09-2022")
    time.sleep(1.5)

    click_every_time = driver.find_element_by_xpath("//*[@id='eventTime']")
    click_every_time.send_keys("06:03PM")
    time.sleep(1.5)

    click_no_people = driver.find_element_by_xpath("//*[@id='people']")
    click_no_people.send_keys("200")
    time.sleep(1.5)

    click_budget = driver.find_element_by_xpath("//*[@id='budget']")
    click_budget.send_keys("3456")
    time.sleep(1.5)

    click_addtional_information = driver.find_element_by_xpath("//textarea[@id='message']")
    click_addtional_information.send_keys("testingggggggggg")
    time.sleep(1.5)

    click_source = driver.find_element_by_xpath("//select[@id='source']")
    dropdown_source = Select(click_source)
    dropdown_source.select_by_visible_text("LinkedIn")
    time.sleep(1.5)

    click_channel = driver.find_element_by_css_selector("#channel")
    dropdown_channel = Select(click_channel)
    dropdown_channel.select_by_index(2)
    time.sleep(1.5)

    click_venues_nm = driver.find_element_by_css_selector("[placeholder='Enter Menus Name ']")
    click_venues_nm.send_keys("Indian,Arbic,South")

    click_note = driver.find_element_by_css_selector("textarea[name='note']")
    click_note.send_keys("dsklmd,dsmclmcsdl")

    click_add_enquiry = driver.find_element_by_xpath("//input[@id='btnSubmitEnquiry']").click()

def Lead_Upadate_other_BH():
    driver.implicitly_wait(20)
    click_lead_edit = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/enquiries/editleads-new/503']")
    driver.execute_script("arguments[0].scrollIntoView();", click_lead_edit)
    click_lead_edit.click()
    click_status = driver.find_element_by_xpath("//select[@id='status']")

    dropdown_lead_status = Select(click_status)
    dropdown_lead_status.select_by_index(3)
    # time.sleep(1)
    # dropdown_lead_status.select_by_index(1)
    click_uplead = driver.find_element_by_css_selector("[value='Update Lead']").click()
    time.sleep(1)
    click_venue_enquiry = driver.find_element_by_xpath("//input[@id='btnSubmitEnquiry']").click()




def Leads_New_Add_Lead():
    driver.implicitly_wait(20)
    click_add_leads = driver.find_element_by_link_text("Add New Leads").click()
    click_venue = driver.find_element_by_xpath("(//*[@class='dropdown bootstrap-select show-tick form-control'])[2]")
    driver.execute_script("arguments[0].click();", click_venue)
    click_venue_name = driver.find_element_by_xpath("(//*[@class='selectpicker form-control'])[2]")
    dropdown_select_venues = Select(click_venue_name)
    dropdown_select_venues.select_by_index(4)
    dropdown_select_venues.select_by_index(12)
    click_other_BH_nm = driver.find_element_by_css_selector("#other_business_hub_name")
    click_other_BH_nm.send_keys("om 17/08 - 09")
    click_other_BH_mail = driver.find_element_by_css_selector("#old_hub_email1")
    click_other_BH_mail.send_keys("omworld01@gmail.com")
    click_other_BH_contact = driver.find_element_by_css_selector("#old_hub_contact1")
    click_other_BH_contact.send_keys("1234569890")
    # click_add_other_BH = driver.find_element_by_xpath("(//a[normalize-space()='Add More Business hubs +'])[1]").click()

    click_custome_name = driver.find_element_by_xpath("//input[@id='custname']")
    click_custome_name.send_keys("om chavan 2ZA")
    click_custome_mail = driver.find_element_by_xpath("//input[@id='email']")
    click_custome_mail.send_keys("ombhagyeshchavan@gmail.com")
    time.sleep(2)

    click_event_type = driver.find_element_by_css_selector("#event_type")
    dropdown_event_type = Select(click_event_type)
    dropdown_event_type.select_by_visible_text("Birthday")
    time.sleep(1.5)

    click_contact = driver.find_element_by_xpath("//*[@class='iti__selected-flag']").click()
    select_state_code = driver.find_element_by_xpath("//*[@id='iti-0__item-in-preferred']").click()
    click_mob_no = driver.find_element_by_xpath("//input[@id='phone']")
    click_mob_no.send_keys("9158333488")
    time.sleep(1.5)

    click_date = driver.find_element_by_css_selector("input[placeholder='Enter Event Date ']")
    click_date.send_keys("11-09-2022")
    time.sleep(1.5)

    click_every_time = driver.find_element_by_xpath("//*[@id='eventTime']")
    click_every_time.send_keys("06:03PM")
    time.sleep(1.5)

    click_no_people = driver.find_element_by_xpath("//*[@id='people']")
    click_no_people.send_keys("200")
    time.sleep(1.5)

    click_budget = driver.find_element_by_xpath("//*[@id='budget']")
    click_budget.send_keys("3456")
    time.sleep(1.5)

    click_addtional_information = driver.find_element_by_xpath("//textarea[@id='message']")
    click_addtional_information.send_keys("testingggggggggg")
    time.sleep(1.5)

    click_source = driver.find_element_by_xpath("//select[@id='source']")
    dropdown_source = Select(click_source)
    dropdown_source.select_by_visible_text("LinkedIn")
    time.sleep(1.5)

    click_channel = driver.find_element_by_css_selector("#channel")
    dropdown_channel = Select(click_channel)
    dropdown_channel.select_by_index(2)
    time.sleep(1.5)

    click_add_menus = driver.find_element_by_css_selector("[placeholder='Enter Menus Name ']")
    click_add_menus.send_keys("indian,chaines")

    click_note = driver.find_element_by_css_selector("textarea[name='note']")
    click_note.send_keys("dsklmd,dsmclmcsdl")

    click_add_enquiry = driver.find_element_by_xpath("//input[@id='btnSubmitEnquiry']").click()





def Lead_Add_Venues():
    driver.implicitly_wait(20)
    click_add_leads = driver.find_element_by_link_text("Add New Leads").click()
    click_venue = driver.find_element_by_xpath("(//*[@class='dropdown bootstrap-select show-tick form-control'])[2]")
    driver.execute_script("arguments[0].click();", click_venue)
    click_venue_name = driver.find_element_by_xpath("(//*[@class='selectpicker form-control'])[2]")
    dropdown_select_venues = Select(click_venue_name)
    # dropdown_select_venues.select_by_index(4)
    # dropdown_select_venues.select_by_index(12)
    dropdown_select_venues.select_by_value("583")
    dropdown_select_venues.select_by_value("585")

    click_custome_name = driver.find_element_by_xpath("//input[@id='custname']")
    click_custome_name.send_keys("om 17/08 - 23")
    click_custome_mail = driver.find_element_by_xpath("//input[@id='email']")
    click_custome_mail.send_keys("omworld01@gmail.com")
    time.sleep(2)

    click_event_type = driver.find_element_by_css_selector("#event_type")
    dropdown_event_type = Select(click_event_type)
    dropdown_event_type.select_by_visible_text("Cocktail Parties")
    time.sleep(1.5)

    click_contact = driver.find_element_by_xpath("//*[@class='iti__selected-flag']").click()
    select_state_code = driver.find_element_by_xpath("//*[@id='iti-0__item-in-preferred']").click()
    click_mob_no = driver.find_element_by_xpath("//input[@id='phone']")
    click_mob_no.send_keys("9158333488")
    time.sleep(1.5)

    click_date = driver.find_element_by_css_selector("input[placeholder='Enter Event Date ']")
    click_date.send_keys("07-09-2022")
    time.sleep(1.5)

    click_every_time = driver.find_element_by_xpath("//*[@id='eventTime']")
    click_every_time.send_keys("06:03PM")
    time.sleep(1.5)

    click_no_people = driver.find_element_by_xpath("//*[@id='people']")
    click_no_people.send_keys("200")
    time.sleep(1.5)

    click_budget = driver.find_element_by_xpath("//*[@id='budget']")
    click_budget.send_keys("3000")
    time.sleep(1.5)

    click_addtional_information = driver.find_element_by_xpath("//textarea[@id='message']")
    click_addtional_information.send_keys("testingggggggggg")
    time.sleep(1.5)

    click_source = driver.find_element_by_xpath("//select[@id='source']")
    dropdown_source = Select(click_source)
    dropdown_source.select_by_visible_text("LinkedIn")
    time.sleep(1.5)

    click_channel = driver.find_element_by_css_selector("#channel")
    dropdown_channel = Select(click_channel)
    dropdown_channel.select_by_index(2)
    time.sleep(1.5)

    click_venues_nm = driver.find_element_by_css_selector("[placeholder='Enter Menus Name ']")
    click_venues_nm.send_keys("Indian,Arbic,South")

    click_note = driver.find_element_by_css_selector("textarea[name='note']")
    click_note.send_keys("Veg")

    click_add_enquiry = driver.find_element_by_xpath("//input[@id='btnSubmitEnquiry']").click()



def Lead_Upadate_Venues():
    driver.implicitly_wait(20)
    click_lead_edit = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/enquiries/editleads-new/507']")
    driver.execute_script("arguments[0].scrollIntoView();", click_lead_edit)
    click_lead_edit.click()
    click_status = driver.find_element_by_xpath("//select[@id='status']")

    dropdown_lead_status = Select(click_status)
    dropdown_lead_status.select_by_index(3)
    # time.sleep(1)
    # dropdown_lead_status.select_by_index(1)
    click_uplead = driver.find_element_by_css_selector("[value='Update Lead']").click()
    time.sleep(1)
    click_venue_enquiry = driver.find_element_by_xpath("//input[@id='btnSubmitEnquiry']").click()


# -------------------- Venue Enquiry Detail Calculation -------------------------------------------------------------

def Click_Venues_Enquiry():
    driver.implicitly_wait(20)
    click_venues_enq = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/enquiries/venues']").click()


def Add_Venues_Enquiry():
    driver.implicitly_wait(20)
    click_add_venues = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/enquiries/add-enquiry']").click()
    click_pushmenu = driver.find_element_by_xpath("//*[@class='fas fa-bars']").click()
    time.sleep(2)
    venues_name = driver.find_element_by_xpath("//*[@class='selectpicker']")
    dropdown_venues_name = Select(venues_name)
    dropdown_venues_name.select_by_value("57*20*Al Aweer Meeting Room 2")
    # dropdown_venues_name.select_by_value("588*496*ZoomVenue_Room1")
    # time.sleep(1)
    # dropdown_venues_name.select_by_value("590*496*ZoomVenue_Room2")

    click_custome_name = driver.find_element_by_xpath("//input[@id='custname']")
    click_custome_name.send_keys("om chavan -- 18")
    click_custome_mail = driver.find_element_by_xpath("//input[@id='email']")
    click_custome_mail.send_keys("omworld01@gmail.com")
    time.sleep(2)

    click_contact = driver.find_element_by_xpath("//*[@class='iti__selected-flag']").click()
    select_state_code = driver.find_element_by_xpath("//*[@id='iti-0__item-in-preferred']").click()
    click_mob_no = driver.find_element_by_xpath("//input[@id='phone']")
    click_mob_no.send_keys("9158333488")
    time.sleep(1.5)

    click_date = driver.find_element_by_css_selector("input[placeholder='Enter Event Date ']")
    click_date.send_keys("07-09-2022")
    time.sleep(1.5)

    click_every_time = driver.find_element_by_xpath("//*[@id='eventTime']")
    click_every_time.send_keys("06:03PM")
    time.sleep(1.5)

    click_no_people = driver.find_element_by_xpath("//*[@id='people']")
    click_no_people.send_keys("200")
    time.sleep(1.5)

    click_budget = driver.find_element_by_xpath("//*[@id='budget']")
    click_budget.send_keys("3000")
    time.sleep(1.5)

    click_addtional_information = driver.find_element_by_xpath("//textarea[@id='message']")
    click_addtional_information.send_keys("testing to om")
    time.sleep(1.5)

    click_event_type = driver.find_element_by_css_selector("#event_type")
    dropdown_event_type = Select(click_event_type)
    dropdown_event_type.select_by_visible_text("Cocktail Parties")
    time.sleep(2)

    click_add_enquiry = driver.find_element_by_xpath("//*[@class='btn btn-success']").click()



def Venue_Enquiry_Cal():
    driver.implicitly_wait(10)
    No_of_Guests = driver.find_element_by_css_selector("[placeholder='No. OF  PAX']").clear()
    No_of_Guests = driver.find_element_by_css_selector("[placeholder='No. OF  PAX']")
    No_of_Guests.send_keys("20")
    time.sleep(2)
    BH_Offer_Price = driver.find_element_by_css_selector("[placeholder=' BH Offer Price']").clear()
    BH_Offer_Price = driver.find_element_by_css_selector("[placeholder=' BH Offer Price']")
    BH_Offer_Price.send_keys("60")
    time.sleep(2)
    ZV_Commission = driver.find_element_by_css_selector("[placeholder='Commission']").clear()
    ZV_Commission = driver.find_element_by_css_selector("[placeholder='Commission']")
    ZV_Commission.send_keys("10")
    time.sleep(2)
    ZV_2_TOC = driver.find_element_by_css_selector("[placeholder='ZV 2 T O Commission (%)']").clear()
    ZV_2_TOC = driver.find_element_by_css_selector("[placeholder='ZV 2 T O Commission (%)']")
    ZV_2_TOC.send_keys("10")
    time.sleep(2)
    ZV_2_TAX = driver.find_element_by_xpath("//*[@class='form-control zv_vat_per text-right']").clear()
    ZV_2_TAX = driver.find_element_by_xpath("//*[@class='form-control zv_vat_per text-right']")
    ZV_2_TAX.send_keys("8")
    time.sleep(2)
    ZV_Payment_Charge = driver.find_element_by_css_selector("[placeholder='Payment Charage']").clear()
    ZV_Payment_Charge = driver.find_element_by_css_selector("[placeholder='Payment Charage']")
    ZV_Payment_Charge.send_keys("2")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,2000)")


def Venues_Enquiry_New_Response():
    driver.implicitly_wait(20)
    click_venues_Enquiry_N_R = driver.find_element_by_xpath("//*[@href='http://vendor.zoomvenues.info/admin/enquiries/venues/newsharedrespond/807']").click()
    click_pushmenu = driver.find_element_by_xpath("//*[@class='fas fa-bars']").click()

    click_venue_name = driver.find_element_by_xpath("//*[@class='form-control select2 newselect']")
    dropdown_venues_name = Select(click_venue_name)
    dropdown_venues_name.select_by_value("592")
    click_new_time = driver.find_element_by_xpath("//*[@name='new_event_time']")
    click_new_time.send_keys("06:13PM")

    click_final_offer_des = driver.find_element_by_xpath("(//div[@aria-label='Rich Text Editor, main'])[1]")
    click_final_offer_des.send_keys("Final Offer Description............")
    click_terms_conditions = driver.find_element_by_xpath("(//*[@class='ck ck-content ck-editor__editable ck-rounded-corners ck-editor__editable_inline ck-blurred'])[2]")



def test_admin_page():
    driver.set_page_load_timeout(10)
    driver.maximize_window()
    driver.get(zoomvenues_url)
    # driver.get("http://vendor.zoomvenues.info/admin/enquiries/venues/newsharedrespond/340")

    # admin_logIn()
    # time.sleep(2)
    #
    # food_menu()
    # time.sleep(2)
    #
    # food_list_food_menu_dropdown()
    # time.sleep(2)
    # view_food()
    # time.sleep(2)
    # edit()

    # food_list_Home()
    # time.sleep(2)

    # add_foods()
    # time.sleep(2)

    # add_food_food_list()
    # time.sleep(2)

    # food_list_edit_food()
    # time.sleep(2)

    # -------------------- Menu List  ----------------------

    # admin_logIn_menu_list()
    # time.sleep(2)
    # Menu_list()
    # time.sleep(2)
    # Add_Menu()
    # time.sleep(2)
    # Config_Menu_card()

    # ------------------ admin page ----------

    # ----------------- commission lead -------------------
    # Leads()
    # Edit_and_updateLead()

    # --------------Business hub -------------
    #
    # admin_logIn()
    # Business_Hub_click()
    # Business_Hub_Edit()

    #
    # Click_View()
    # Click_venues_list()
    # Click_packages_list()
    # Click_download_pdf()
    # time.sleep(5)

    # ------------------------- Business Hubs Leads ------------------------------

    # admin_logIn()
    # Click_Business_hubs_leads()
    # Add_new_Business_hubs_leads()
    # Edit_business_hubs_lead()
    # View_business_hubs_lead()
    # -------------------------------- Renewal Users-----------------------------
    # Renewal_Users()
    # -------------------------------- Venues -----------------------------
    # admin_logIn()
    # Venues_Edit()
    # Venues_Promoted()
    # Venues_Feature()
    # Venue_View()
    # Venues_Add_360()
    # Venues_Edit_360()

    # ------------------------------ Service_Provider--------------------------------
    # admin_logIn()
    # Service_Provider_Click()
    # Service_Provider_Edit()
    # Service_Provitor_service_list()
    # Service_Provider_Delete()

    # ------------------------------ My Booking --------------------------------
    # admin_logIn()
    # Click_My_Booking()
    # My_Booking_Click_Venue_Name()

    # ------------------------------ Leads -----------------------------------
    admin_logIn()
    # Click_Leads()
    # Leads_New_Add_Lead()
    # Lead_Action_Edit()
    # Leads_Add_Lead()
    # Leads_New_Other_BH()
    # Lead_Upadate_other_BH()
    # Lead_Add_Venues()
    # Lead_Upadate_Venues()


    # ----------------------------- Venues Enquirey ---------------------------------

    Click_Venues_Enquiry()
    # Add_Venues_Enquiry()
    # Venue_Enquiry_Cal()
    Venues_Enquiry_New_Response()
    # time.sleep(6)
    # driver.quit()


