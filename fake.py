import selenium
from selenium import webdriver
import random
import string
from faker import Faker
fake = Faker("en_CA") # Change this to match your locale

x = 0
y = 1

def gen():
    gens = ['male', 'female', 'Non-binary']
    y = random.randint(1,3)
    return gens[y-1]

driver = webdriver.Chrome() # Change this to the one you are using.

while x<10: #CHANGE THIS
    driver.get("WEBSITE NAME")
    user = driver.find_element_by_id("login-username")
    pas = driver.find_element_by_id("login-password")
    subm = driver.find_element_by_id("g-recaptcha-button")
    user.send_keys(fake.ascii_email())
    pas.send_keys(fake.password())
    subm.click()
    x = x+1
    print('Logged in ' + str(x) + ' times')
    a = driver.find_element_by_name("firstname")
    b = driver.find_element_by_name("lastname")
    c = driver.find_element_by_name("address")
    d = driver.find_element_by_name("city")
    e = driver.find_element_by_name("postcode")
    f = driver.find_element_by_name("dobmonth")
    g = driver.find_element_by_name("dobday")
    h = driver.find_element_by_name("dobyear")
    i = driver.find_element_by_name("gender")
    j = driver.find_element_by_name("phonenumber")
    k = driver.find_element_by_name("securityquestion")
    l = driver.find_element_by_name("securityanswer")
    m = driver.find_element_by_name("socialinsurancenumber")
    n = driver.find_element_by_name("country")
    o = driver.find_element_by_id("profile_save_profile")
    a.send_keys(fake.first_name())
    b.send_keys(fake.last_name())
    c.send_keys(fake.street_address())
    d.send_keys(fake.city())
    e.send_keys(fake.postalcode())
    f.send_keys(fake.month())
    g.send_keys(fake.day_of_month())
    h.send_keys(fake.year())
    i.send_keys(gen())
    j.send_keys(fake.random_number(10))
    #k.send_keys(seq())
    l.send_keys(fake.first_name_female())
    m.send_keys(fake.random_number(9))
    #n.send_keys(fake.country())
    o.click()

    p = driver.find_element_by_name("cardholder")
    q = driver.find_element_by_id("cardnumber")
    r = driver.find_element_by_id("expiry-month")
    s = driver.find_element_by_id("expiry-year")
    t = driver.find_element_by_id("security-code")
    u = driver.find_element_by_id("g-recaptcha-button")

    p.send_keys(fake.name())
    q.send_keys(fake.credit_card_number(card_type=None))
    r.send_keys(fake.credit_card_expire(start="now", end="+10y", date_format="%m"))
    s.send_keys(fake.credit_card_expire(start="now", end="+10y", date_format="%y"))
    t.send_keys(fake.credit_card_security_code(card_type=None))
    u.click()
    
