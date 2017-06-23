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




##################Convert CSV###########################
def Convert_to_csv(List_of_docs):

    keys = ['id', 'name', 'tagline','adresse_web','jobs' ]
    with open('angel_co_jobs.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(List_of_docs)

#################Scrap websites#####################

def scrap_website(driver,List_of_docs, number_startups = 0):
    driver.implicitly_wait(100)
    tagline = driver.find_elements_by_css_selector("div.tagline")  # find tagline
    driver.implicitly_wait(500)
    jobs_title = driver.find_elements_by_css_selector("div.collapsed-listing-row")  # find number of jobs
    driver.implicitly_wait(500)
    startup_names = driver.find_elements_by_css_selector("a.startup-link")  # find startup's name
    driver.implicitly_wait(500)
    dict_job_titles = []
    print("display nb of startups scrapped")
    print(len(tagline), len(jobs_title), len(startup_names))

    number_startups = number_startups + len(startup_names)

    for index, name in enumerate(startup_names):
        dictionnaire = {}
        try:
            # print(name.text)
            dictionnaire["id"] = index
            dictionnaire["name"] = name.text.encode("utf-8")
            print(name.text.encode("utf-8"))

        except:
            print("saute")
        List_of_docs.append(dictionnaire)

    for index, i in enumerate(startup_names):
        site_web = driver.find_elements_by_partial_link_text(i.text.encode("utf-8"))
        for j in site_web:
            adresse = j.get_attribute("href")
            List_of_docs[index]["adresse_web"] = adresse



    for index, name in enumerate(tagline):
        try:
            print(index, name.text.encode("utf-8"))
            List_of_docs[index]['tagline'] = name.text.encode("utf-8")
        except:
            print(name)

    for index, name in enumerate(jobs_title):
        # List_of_docs[index]['jobs'] = name.text.encode("utf-8")
        try:
            dict_job_titles.append(name.text)
        except:
            dict_job_titles.append("job")

    return List_of_docs,number_startups


def scrap_website2(driver,List_of_docs, number_startups):

    startups = driver.find_elements_by_css_selector("div.djl87.job_listings.fbw9.browse_startups_table_row._a._jm")
    for company in startups:
        scrap_bloc = {}
        print(company)
        List_of_docs["company"] = company.text



##################Login#############################
def login(driver, username,pwd):

    driver.get('http://angel.co/job')

    driver.implicitly_wait(5)  # seconds

    link = driver.find_element_by_link_text('Log In')
    link.click()

    Facebook = driver.find_element_by_link_text('Log in with Facebook')
    email = driver.find_element_by_name('user[email]')
    driver.implicitly_wait(5)  # seconds
    pw = driver.find_element_by_name('user[password]')
    email.clear()
    pw.clear()
    email.send_keys(username)
    driver.implicitly_wait(5)  # seconds
    pw.send_keys(pwd)
    driver.implicitly_wait(5)  # seconds
    login = driver.find_element_by_name("commit")
    login.click()
    driver.implicitly_wait(100)

#################Enter words in serach bar###############

def search_bar(driver,research):
#reserach in keywords
    input = driver.find_element_by_css_selector("div.search-box")
    input.click()
    driver.implicitly_wait(1400)
    keyword= driver.find_element_by_xpath("//input[@class='input keyword-input']")

    for i in research:
        keyword.send_keys(i)
        driver.implicitly_wait(5)  # seconds

    button_save = driver.find_elements_by_css_selector("a.save-current-filters.c-button.c-button--gray.c-button--sm")[0]
    button_save.click() #wrong button


################### Scrap pages #########################


#########################Data Entry###################
#PATH = '/usr/local/bin/chromedriver'
PATH = 'C:/Users/vtec-mchen/PycharmProjects/chromedriver.exe'
Login = ["myouhu@yahoo.fr", "bismilah"]
List_of_docs = []
driver = webdriver.Chrome(PATH)

login(driver,Login[0],Login[1])
driver.implicitly_wait(500)
nb_startups = driver.find_elements_by_css_selector("div.label-container.u-floatLeft")[-1].text #find total number of startups
#print(nb_startups, number_startups)
scrap_website(driver,List_of_docs,100)

print(List_of_docs,number_startups)
Convert_to_csv(List_of_docs)

'''

while number_startups != nb_startups:
    print("enter in the loop")
    print("before %s " %(number_startups))
    List_of_docs,number_startups = scrap_website(List_of_docs,number_startups)
    print("after %s" %number_startups)
    # scroll down the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print(List_of_docs)
    nb_page_scrapped +=1

print(number_startups, nb_page_scrapped)
Convert_to_csv(List_of_docs) '''








