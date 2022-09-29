# name="one one for omsonar one"
# z=name.replace("one","five",2)
# a=name.replace("one","Ten")
# print(z,"--",a)

# name="one one for omsonar one"
# z=name.split(",") -----conver to one string
# print(z)

# txt = "apple#banana#cherry#orange"
# z=txt.split("#") -------remove the #
# print(z)

# txt = "apple#banana#cherry#orange"
# z=txt.split("#",1) ----------remove only first #
# print(z)

# myTuple = ("John", "Peter", "Vicky")
# z=" om ".join(myTuple) ---- add om word in tuple
# print(z)

# myTuple = ("John", "Peter", "Vicky")
# name= " test "
# z=name.join(myTuple) ----add string
# print(z)

# myTuple = ("John", "Peter", "Vicky")
# txt= " : "
# z=txt.join(myTuple)
# print(z)
import traceback

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class A:
    def test_case(self):
        driver = webdriver.Chrome(executable_path="/chromedriver.exe")
        driver.get("https://www.expedia.com/")

        try:
            attribute = driver.find_element_by_xpath("//span[normalize-space()='Flight']")
        except NoSuchElementException:
            print(traceback.format_exc())

        z = driver.find_element_by_xpath("//span[normalize-space()='Flights']").click()
        driver.close()

p=A()
p.test_case()