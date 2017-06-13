import math
import os
import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import csv
import time

#PATH = '/usr/local/bin/chromedriver'
PATH = 'C:\Users\vtec-mchen\PycharmProjects\chromedriver.exe'
research = ["Paris"]

info = {}

driver = webdriver.Chrome(PATH)
driver.get('http://angel.co/job')

Login = ["myouhu@yahoo.fr", "Bismilah19921963"]
"need waiting"

link = driver.find_element_by_link_text('Log In')
link.click()
Facebook = driver.find_element_by_link_text('Log in with Facebook')
email= driver.find_element_by_name("email")
pw= driver.find_element_by_name("pass")
email.clear()
pw.clear()
email.send_keys(Login[0])
pw.send_keys(Login[1])
login = driver.find_element_by_name("login")
login.click()
input = driver.find_element_by_css_selector("div.search-box")
input.click()
keyword= driver.find_element_by_xpath("//input[@class='input keyword-input']")
for i in research:
    keyword.send_keys(i)

button_save = driver.find_elements_by_css_selector("a.save-current-filters.c-button.c-button--gray.c-button--sm")[0]
button_save.click()
startup_names = driver.find_elements_by_css_selector("a.startup-link")
tagline = driver.find_elements_by_css_selector("div.tagline")
for i in tagline:
    try:
        print(i.text)
    raise:
        print("saute")
jobs = driver.find_elements_by_css_selector("div.startup-info-table")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#scroll down the page





