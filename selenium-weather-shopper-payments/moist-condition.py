'''
Finding least expensive Moisturizer based on the condition and doing payment Program: 
Used this site  https://weathershopper.pythonanywhere.com/moisturizer
----------------------------------
Python 3.7.0 and Selenium 3.141.0
----------------------------------
Author : Srinivasa Varun
E-mail : tcvarun96@gmail.com''' 

import time
from selenium import webdriver
import rand_email

driver=webdriver.Firefox()
driver.maximize_window()
driver.get('http://weathershopper.pythonanywhere.com/moisturizer')

time.sleep(2)

driver1 = driver.find_elements_by_xpath("(//p[contains(@class,'font-weight-bold top-space-10')])")
list_for_driver1_values = []
list_to_append_text_values = []
for i in driver1:
    list_to_append_text_values.append(i.text.split("\n"))
    list_for_driver1_values.append(i.text)

driver2 = driver.find_elements_by_xpath("//p[contains(.,'Price:')]")
list_for_driver2_values = []
list_to_append_driver2_text_values = []
for j in driver2:
    list_to_append_driver2_text_values.append(j.text.split("\n"))
    list_for_driver2_values.append(j.text)

psuedo_list1_to_get_int_values = list_for_driver2_values[:3] 
list_to_store_int_values = [int(sub.split('.')[1]) for sub in psuedo_list1_to_get_int_values]

psuedo_list2_to_get_int_values = list_for_driver2_values[3:]
list2_to_store_int_values = [int(sub.split(':')[1]) for sub in psuedo_list2_to_get_int_values]

#concatenating the above two pseudo lists to as int
concat_list = list_to_store_int_values+list2_to_store_int_values

Dict = dict(zip(list_for_driver1_values, concat_list))

filtered_dict_for_Aloe = {list_for_driver1_values:concat_list for (list_for_driver1_values, concat_list) in Dict.items() if 'Aloe' in list_for_driver1_values}

filtered_dict_for_Almond = {list_for_driver1_values:concat_list for (list_for_driver1_values, concat_list) in Dict.items() if 'Almond' in list_for_driver1_values}



min_val_of_Aloe = min(filtered_dict_for_Aloe, key=lambda x: filtered_dict_for_Aloe.get(x))
print(min_val_of_Aloe, "has the lowest price in Aloe category")


min_val_of_Almond = min(filtered_dict_for_Almond, key=lambda y: filtered_dict_for_Almond.get(y))
print(min_val_of_Almond, "has the lowest price in Almond Category")

print("Adding them to the Cart.")

time.sleep(3)
map_dict_list=[]
for list_for_driver1_values, concat_list in Dict.items():
    map_dict_list.append((list_for_driver1_values, concat_list))
locations1 = [i for i, t in enumerate(map_dict_list) if t[0]==min_val_of_Aloe]

loc1_for_clicking_min_aloe= locations1[0]

locations2 = [i for i, e in enumerate(map_dict_list) if e[0]==min_val_of_Almond]
loc2_for_clicking_min_almond = locations2[0]

button=driver.find_elements_by_xpath('//button[contains(@class,"btn btn-primary")]')
button=button[loc1_for_clicking_min_aloe]
button.click()

button=driver.find_elements_by_xpath('//button[contains(@class,"btn btn-primary")]')
button=button[int(loc2_for_clicking_min_almond)]
button.click()

time.sleep(1)

#Opening the cart by clicking the cart button
cart=driver.find_element_by_id("cart")
cart.click()

time.sleep(2)

cart_table=driver.find_element_by_xpath("//table[contains(@class,'table table-striped')]")
cart_rows=cart_table.find_elements_by_xpath("//tbody/descendant::tr")
for cart_item in cart_rows:
    print(cart_item.text)
    
'''if min_val_of_Aloe and min_val_of_Almond in cart_item.text:
    print("success")
else:
    print("fail")'''

#Clicking the pay button after verifying the cart
button_to_pay = driver.find_element_by_xpath("//button[contains(@type,'submit')]")
button_to_pay.click()

driver.switch_to.frame(driver.find_element_by_tag_name("iframe")) #Switching to frame box to fill in the details for payment gateway

email = driver.find_element_by_xpath("//input[contains(@type,'email')]").send_keys(rand_email.random_mail())

card_number = driver.find_element_by_xpath("//input[contains(@placeholder,'Card number')]").send_keys("4242424242424242")

month_year = driver.find_element_by_xpath("//input[contains(@placeholder,'MM / YY')]").send_keys("11/22")

cv = driver.find_element_by_xpath("//input[contains(@maxlength,'4')]").send_keys(rand_email.random_cvv(3))

zip_code = driver.find_element_by_xpath("//input[contains(@placeholder,'ZIP Code')]")
time.sleep(0.5)
zip_code.send_keys(rand_email.random_zip(6))

remember = driver.find_element_by_xpath("//label[contains(@class,'Fieldset-label')]").click()

phone = driver.find_element_by_xpath("//input[contains(@autocomplete,'mobile tel')]")
time.sleep(0.5)
phone.send_keys(rand_email.random_phone(10))

time.sleep(3)

button_to_submit = driver.find_element_by_xpath("//button[contains(@type,'submit')]").click()

driver.switch_to.frame(0) #Going back to default frame after clicking the pay button

time.sleep(9)




driver.quit() #closing the driver




