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
import sys



#########################Data Entry###################
#PATH = '/usr/local/bin/chromedriver'
PATH = 'C:/Users/vtec-mchen/PycharmProjects/chromedriver.exe'
Login = ["myouhu@yahoo.fr", "bismilah"]
research = ["Paris"]

######################################################

##################Variable############################
List_of_docs = []

##################Fonction###########################
def Convert_to_csv(List_of_docs):

    keys = ['startup-names', 'tagline','jobs']
    with open('angel_co_jobs.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(List_of_docs)



driver = webdriver.Chrome(PATH)
driver.get('http://angel.co/job')

driver.implicitly_wait(5) # seconds

link = driver.find_element_by_link_text('Log In')
link.click()

Facebook = driver.find_element_by_link_text('Log in with Facebook')
email= driver.find_element_by_name('user[email]')
driver.implicitly_wait(5) # seconds
pw= driver.find_element_by_name('user[password]')
email.clear()
pw.clear()
email.send_keys(Login[0])
driver.implicitly_wait(5) # seconds
pw.send_keys(Login[1])
driver.implicitly_wait(5) # seconds
login = driver.find_element_by_name("commit")
login.click()
input = driver.find_element_by_css_selector("div.search-box")
input.click()
keyword= driver.find_element_by_xpath("//input[@class='input keyword-input']")

for i in research:
    keyword.send_keys(i)
    driver.implicitly_wait(5)  # seconds

button_save = driver.find_elements_by_css_selector("a.save-current-filters.c-button.c-button--gray.c-button--sm")[0]
button_save.click()

nb_startups = driver.find_elements_by_css_selector("span.label")[-1].text

tagline = driver.find_elements_by_css_selector("div.tagline")
jobs_title = driver.find_elements_by_css_selector("div.collapsed-listing-row")
startup_names = driver.find_elements_by_css_selector("a.startup-link")
#info_table = driver.find_elements_by_css_selector("div.startup-info-table")

for index, name in enumerate(startup_names):
    dictionnaire = {}
    try:
        #print(name.text)
        dictionnaire["id"] = index
        dictionnaire["name"] = name.text

    except:
        print("saute")
    List_of_docs.append(dictionnaire)


for index, name in enumerate(tagline):
        List_of_docs[index]['tagline'] = name.text.encode("utf-8")

for index, name in enumerate(jobs_title):
        List_of_docs[index]['jobs'] = name.text.encode("utf-8")




print(List_of_docs)

#scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")






