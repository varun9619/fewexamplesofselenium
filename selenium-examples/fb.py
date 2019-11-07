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
pas = driver.find_element_by_id("pass")
pas.send_keys(pwd)

button = driver.find_element_by_xpath("//input[contains(@value,'Log In')]")
button.click()
#elem.send_keys(Keys.RETURN) #clicking the button

time.sleep(4) #pause the script until page loads

#closing driver
driver.close()
