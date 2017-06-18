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
research = ["Paris", ""]

######################################################

##################Variable############################
List_of_docs = []
number_startups = 0
nb_page_scrapped = 0

##################Fonction###########################
def Convert_to_csv(List_of_docs):

    keys = ['id', 'name', 'tagline','jobs']
    with open('angel_co_jobs.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(List_of_docs)

def scrap_website(List_of_docs,number_startups):

    tagline = driver.find_elements_by_css_selector("div.tagline")  # find tagline
    jobs_title = driver.find_elements_by_css_selector("div.collapsed-listing-row")  # find number of jobs
    startup_names = driver.find_elements_by_css_selector("a.startup-link")  # find startup's name
    print("display nb of startups scrapped")
    print(len(tagline), len(jobs_title), len(startup_names))

    number_startups = number_startups + len(startup_names)

    for index, name in enumerate(startup_names):
        dictionnaire = {}
        try:
            # print(name.text)
            dictionnaire["id"] = index
            dictionnaire["name"] = name.text

        except:
            print("saute")
        List_of_docs.append(dictionnaire)

    for index, name in enumerate(tagline):
        List_of_docs[index]['tagline'] = name.text.encode("utf-8")

    for index, name in enumerate(jobs_title):
        # List_of_docs[index]['jobs'] = name.text.encode("utf-8")
        print(index, name.text.encode("utf-8"))

    return List_of_docs,number_startups





##################Login#############################
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

#################Enter words in serach bar###############

input = driver.find_element_by_css_selector("div.search-box")
input.click()
driver.implicitly_wait(14000)
keyword= driver.find_element_by_xpath("//input[@class='input keyword-input']")

for i in research:
    keyword.send_keys(i)
    driver.implicitly_wait(5)  # seconds

button_save = driver.find_elements_by_css_selector("a.save-current-filters.c-button.c-button--gray.c-button--sm")[0]
button_save.click() #wrong button

################### Scrap pages #########################

nb_startups = driver.find_elements_by_css_selector("span.label")[-1].text #find total number of startups

while number_startups != nb_startups:
    print("before %s " %(number_startups))
    List_of_docs,number_startups = scrap_website(List_of_docs,number_startups)
    print("after %s" %number_startups)
    # scroll down the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print(List_of_docs)
    nb_page_scrapped +=1

print(number_startups, nb_page_scrapped)
Convert_to_csv(List_of_docs)








