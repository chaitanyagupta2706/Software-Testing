from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://facebook.com")

email = driver.find_element_by_name("email")
password = driver.find_element_by_name("pass")

# User-id & password have been changed
email.send_keys("abc@gmail.com")
password.send_keys("123456")
login = driver.find_element_by_name("login").click()
print('Logged in successfully!!')

# logout1=driver.find_element_by_css_selector("#userNavigationLabel").click()
time.sleep(5)
# logout2=driver.find_element_by_xpath("//li[12]/a/span/span").click()
# driver.find_element_by_css_selector("a[data-gt*='menu_logout']>span>span._54nh").click();
print('Logged out successfully!!')
driver.close()