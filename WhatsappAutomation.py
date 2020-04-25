# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:28:39 2020

@author: ADMIN
"""

from selenium import webdriver
#Connect with the ChromeDriver
driver = webdriver.Chrome(executable_path='C:\chromedriver_win32\chromedriver.exe')

#Go to the Website
driver.get('https://web.whatsapp.com/')


name = input('Enter the name of user or group : ')
msg = input('Enter your message')
count = int(input('Enter the count'))

input('Enter anything after scanning QR code')

#Finding the name of the person via XPATH - To get the Xpath Inspect the element and click copy -copy Xpath
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click() 

msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]') # fIND THE TEXTbox

for i in range(count):
    msg_box.send_keys(msg) # Message that should be sent
    button = driver.find_element_by_class_name('_35EW6') #Find send button via Xpath
    button.click() #Click on send button