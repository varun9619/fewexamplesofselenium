''' This script of selenium lets you select between sunscreen 
and moisturizer by checking with the temperature provided in the webpage'''

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Firefox() 
driver.get('http://weathershopper.pythonanywhere.com') #opening the weather shopper app

time.sleep(2)

temp = driver.find_element_by_id("temperature")
temp2 = temp.text
print(temp2)
temp3 = ''.join((ch if ch in '0123456789' else ' ') for ch in temp2)  
lst = [int(i) for i in temp3.split()]
print(temp3)

temp3 = int(temp3)+0

if temp3>34:
    button=driver.find_element_by_xpath("//button[contains(.,'Buy sunscreens')]")
    button.click()
    print("It is hot you need to go with the sunscreen")
elif temp3<19:
    button = button.find_element_by_xpath("//button[contains(.,'Buy moisturizers')]")
    print("It is Cold better choose moisturizer")
else:
    print("The temperature is normal")

time.sleep(1)
driver.quit() #closing the browser





 
