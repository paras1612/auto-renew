# exclusively for IIIT Delhi students :p
from selenium import webdriver
username="username" #type your username
password="password" #type your password
option = webdriver.ChromeOptions()
option.add_argument("headless") #making chrome invisible XDDDD
driver = webdriver.Chrome(options=option)
driver.maximize_window()

def login():
    driver.get("http://library.iiitd.edu.in") 
    driver.find_element_by_id("userid").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.execute_script("arguments[0].click();",driver.find_element_by_css_selector(".action>.btn"))
    driver.find_element_by_css_selector(".btn:nth-child(5)").click()
    driver.find_element_by_id("logout").click()
    driver.close()

login()
