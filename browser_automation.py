# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:41:57 2019

@author: keshav singh
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:/Users/keshav singh/Downloads/chromedriver")
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver,600)

target ='"Your friend name"'
string = "Message to be want to be sent"
x_arg='//span[contains(@title,'+target + ')]'
target =wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))
target.click()

input_box = driver.find_element_by_class_name('_1Plpp')
for i in range(50):
    input_box.send_keys(string+Keys.ENTER)