#list1 = [10,34,4,56,90,1]

# l =[]
#
# num = int(input("enter digit: "))
# for x in range(num):
#     no = int(input("enter num: "))
#     l.append(no)
#
# for j in range(len(l)-1):
#     for i in range(len(l) - 1-j):
#         if l[i] > l[i + 1]:
#             l[i], l[i + 1] = l[i + 1], l[i]
#             print(l)
#         else:
#             print(l)


#
# def add():
#     x=5
#     def inner():
#         y=6
#         r = x+5
#         return r
#     return inner()
#
# a= add()
# print(a)



# num=[4,56,10,9,11]
#
# a=list(filter(lambda x:x<10,num))
# print(a)


# def outer(func):
#     x=10
#     def inner(a,b):
#
#         z=x+a+b
#         return z
#     return inner(20,30)
#
# def other(a,b):
#     print(a+b)
#
# a=outer(other(3,4))
# print(a)


# def con_up(func):
#     def inner():
#         str1=func()
#         return str1.upper()
#     return inner()
#
# @con_up
# def sentence():
#     return "om chavhan"
#
# print(sentence)

# def outer(func):
#     def inner(x,y):
#         if x==0:
#             return "om sonar"
#         return func
#     return inner
# @outer
# def add(a,b):
#     return a-b
#
# print(add(0,5))



# def other(func):
#     def inner():
#         str1=func()
#         return str1.upper()
#     return inner

# def outer(func):
#     def inner():
#         str1 = func
#         return str1.split()
#     return inner
# @outer
# @other
# def world():
#     return "om Sonar"
#
# print(world())


# def outer1(exp):
#     def outer2(func):
#         def inner():
#             return func() + exp
#         return inner
#     return outer2
#
# @outer1(" chavan")
# def other():
#     return "om"
#
# print(other())


#
# def all(func):
#     def inner(x,y):
#         a= func
#         return a
#     return inner
#
# @all
# def add(a,b):
#     return a+b
# @all
# def minus(a,b):
#     return a-b
#
# print(add(6,8))
# print(minus(5,6))

# def fun(a,b,*argv):
#     mul = a*b
#     for x in argv:
#         mul *=x
#     return mul
#
# print(fun(1,2,3,4,5))
import time
from functools import reduce



# def reverseWordSentence(Sentence):
#     words = Sentence.split(" ")
#     newWords = [word[::-1] for word in words]
#     newSentence = " ".join(newWords)
#     return newSentence
#
#
# Sentence = "I am in gslab"
# print(reverseWordSentence(Sentence))

from selenium import webdriver
import pytest


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_trip():
    driver = webdriver.Chrome(executable_path="/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.expedia.com/")
    assert driver.title == "Expedia Travel: Vacation Homes, Hotels, Car Rentals, Flights &amp"

def test_fb():
    driver = webdriver.Chrome(executable_path="/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    assert driver.title == "Facebook – log in or sign up"

def test_insta():
    driver = webdriver.Chrome(executable_path="/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.instagram.com/")
    assert driver.title == "Instagram"


def test_Fb_Sign_Up():
    global driver
    option = Options()
    option.add_argument("--disable-notifications--")
    driver = webdriver.Chrome(executable_path="/chromedriver.exe", chrome_options=option)
    driver.implicitly_wait(10)
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    sign_click()
    sign_in_Id("919158333486")
    continue_btn_click()
    sign_in_pwd("omworld")
    sign_btn_click()

def sign_click():
    driver.implicitly_wait(10)
    Action = ActionChains(driver)
    click = driver.find_element_by_css_selector("span[class='nav-line-2 ']")
    Action.move_to_element(click).perform()
    sign_in_btn = driver.find_element_by_xpath("//*[@id='nav-flyout-ya-signin']/a/span")
    sign_in_btn.click()

def sign_in_Id(ID):
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10)
    id = wait.until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, '#ap_email')))
    # id= driver.find_element_by_css_selector("#ap_email")
    id.send_keys(ID)

def continue_btn_click():
    driver.implicitly_wait(10)
    btn_click = driver.find_element_by_xpath("//input[@id='continue']")
    btn_click.click()

def sign_in_pwd(pwd):
    driver.implicitly_wait(10)
    password=driver.find_element_by_css_selector("#ap_password")
    password.send_keys(pwd)

def sign_btn_click():
    driver.implicitly_wait(10)
    click_btn = driver.find_element_by_css_selector("#signInSubmit")
    click_btn.click()

def All_dropdown_select():
    driver.implicitly_wait(10)
    All_dropdown = driver.find_element_by_css_selector("#searchDropdownBox")
    dropdown = Select(All_dropdown)
    dropdown.select_by_index(16)

def Search_box(product):
    driver.implicitly_wait(10)
    serach_click = driver.find_element_by_css_selector("#twotabsearchtextbox")
    serach_click.send_keys(product)

def Search_box_click():
    driver.implicitly_wait(10)
    click = driver.find_element_by_css_selector("#nav-search-submit-button")
    click.click()

def Select_Product_And_Buy_click():
    driver.implicitly_wait(10)
    Home_Page = driver.current_window_handle
    product = driver.find_element_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal'][contains(text(),'AmazonBasics 109 cm (43 inches) 4K Ultra HD Smart ')]")
    product.click()
    Product_Page = driver.window_handles

    for Product in Product_Page:
        if Product != Home_Page:
            driver.switch_to.window(Product)
            Buy_product = driver.find_element_by_css_selector("#buy-now-button")
            Buy_product.click()





