# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 01:41:53 2021

@author: HI
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import pandas as pd
  



driver = webdriver.Chrome(executable_path='C:/Users/HI/chromedriver.exe')
driver.get('http://cbseaff.nic.in/cbse_aff/schdir_Report/userview.aspx')
sleep(1)
tap=driver.find_element_by_id("optlist_0")
tap.click()

key=driver.find_element_by_id("keytext").send_keys("a")
key2=driver.find_element_by_id("keytext").send_keys(Keys.RETURN)

table=driver.find_element_by_id("p1")

print(table.text)
sleep(1)
try:
    nextp=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Button1")) 
    ) 
    nextp.click()
except:
   driver.quit()    
table=driver.find_element_by_id("p1")
print(table.text)
table. to_csv('keywords.csv')
