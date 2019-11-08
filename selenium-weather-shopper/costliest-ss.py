'''
Finding most expensive Sunscreen Programs: 
Add all the Sunscreen to a cart of this site https://weathershopper.pythonanywhere.com/sunscreen
----------------------------------
Python 3.7.0 and Selenium 3.141.0
----------------------------------
Author : Srinivasa Varun
E-mail : tcvarun96@gmail.com''' 

from selenium import webdriver
import time

driver = webdriver.Firefox() 
driver.maximize_window()
driver.get('http://weathershopper.pythonanywhere.com/sunscreen') #opening weather shopper page

time.sleep(2) #giving time for the page to load

driver1 = driver.find_elements_by_xpath("//p[contains(.,'Price:')]") #X_path for the price


list1 = []
list2 = []
for i in driver1:
    list2.append(i.text.split("\n"))
    list1.append(i.text) #Assigning the values to a empty list
    
#initiating two psuedo lists, slicing the above list into two other list based on their condition
psuedo_list1 = list1[:3] 
list3 = [int(sub.split('.')[1]) for sub in psuedo_list1]

psuedo_list2 = list1[3:]
list4 = [int(sub.split(':')[1]) for sub in psuedo_list2]

#concatenating the above two pseudo lists to as int
concat_list = list3+list4
print(concat_list)
max_val=max(concat_list) #finding the max value of the list
max_index=concat_list.index(max_val) #finding the index of the max value
print(max_val)
print(max_index)

#getting all button objects to click the max priced moisturizer button
button=driver.find_elements_by_xpath('//button[contains(@class,"btn btn-primary")]')
button=button[max_index]
button.click()

time.sleep(5)

#Clicking the cart button and showing cart

cart=driver.find_element_by_id("cart")
cart.click()
time.sleep(5)

if(driver.current_url == "http://weathershopper.pythonanywhere.com/cart"):
    print("Successfully Added")
else:
    print("Failure")

time.sleep(2)
#closing the driver
driver.quit()

 
