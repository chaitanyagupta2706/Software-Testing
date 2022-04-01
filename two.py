from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://facebook.com")

email = driver.find_element_by_name("email")
password = driver.find_element_by_name("pass")

# User-id & password have been changed
email.send_keys("abc@gmail.com")
password.send_keys("12345678")
login = driver.find_element_by_name("login").click()
print('Could not Log in')

time.sleep(5)
driver.close()