''' This script opens up the fb page, login in into the application 
using user credentials which are mentioned  '''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

user = "******" #username
pwd = "*****" #password

driver = webdriver.Firefox()

driver.get("http://www.facebook.com") #open fb page

#Enterning email 
email = driver.find_element_by_xpath("//input[contains(@type,'email')]")
email.send_keys(user)

#Entering password
pwd = driver.find_element_by_id("pass")
pwd.send_keys(pwd)

button = driver.find_element_by_xpath("//input[contains(@value,'Log In')]")
button.click()

time.sleep(4) #pause the script until page loads

#closing driver
driver.close()
