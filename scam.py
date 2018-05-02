import selenium
from selenium import webdriver
# import random
# import string
from faker import Faker
fake = Faker("en_CA")

x = 0
y = 1

driver = webdriver.Chrome()

while x<10:
    driver.get("WEBSITE")
    user = driver.find_element_by_id("username")
    pas = driver.find_element_by_id("password")
    subm = driver.find_element_by_id("submit")
    user.send_keys(fake.ascii_email())
    pas.send_keys(fake.password())
    subm.click()
    x = x+1
    print('Logged in ' + str(x) + ' times')
