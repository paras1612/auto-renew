# exclusively for IIIT Delhi :p
from selenium import webdriver
username="username" #type your username
password="password" #type your password
driver=webdriver.Chrome()
def login():
    driver.get("http://library.iiitd.edu.in")
    driver.find_element_by_id("userid").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_css_selector(".action>.btn").click()
    driver.find_element_by_css_selector(".btn:nth-child(5)").click()
    driver.find_element_by_id("logout").click()
    driver.close()

login()