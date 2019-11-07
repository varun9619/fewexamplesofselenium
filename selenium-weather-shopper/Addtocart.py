from selenium import webdriver
import time

driver = webdriver.Firefox() 
driver.get('http://weathershopper.pythonanywhere.com/moisturizer') #opening the weather shopper app

time.sleep(2)

print("Adding moisturizers to the cart")
button1 = driver.find_elements_by_xpath("//button[contains(@class,'btn btn-primary')]")
for item in button1:
    item.click()

button2 = driver.find_element_by_xpath("//button[contains(@class,'thin-text nav-link')]")
button2.click()

time.sleep(2)

driver.quit()


