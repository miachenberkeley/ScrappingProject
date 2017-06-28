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


PATH = 'C:/Users/vtec-mchen/PycharmProjects/chromedriver.exe'
driver = webdriver.Chrome(PATH)

def Convert_to_csv(List_of_docs):

    keys = ['startup', 'jobs','site web']
    with open('Welcome_jungle_scrapping.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        try:
            dict_writer.writerows(List_of_docs)
        except:
            print("saute")


jobs = []

for j in range(7):
    web_path = 'https://www.welcometothejungle.co/companies?q=&hPP=30&idx=cms_companies_production&p=' + str(j) + '&dFR%5Bcompany_size%5D%5B0%5D=Entre%2015%20et%2050%20salari%C3%A9s&is_v=1'
    driver.get(web_path)
    startups_name = driver.find_elements_by_tag_name("h4")
    if not startups_name:
        print(startups_name)
        print("Attention pas de scrapping")
    for i in startups_name:
        job = {}
        number = [int(s) for s in i.text.encode("utf-8").split() if s.isdigit()]
        try:
            if number[0] <2:
                text = i.text.replace('JOB', '')
            else:
                text = i.text.replace('JOBS', '')
        except:
            print(number)
            number = [0]
        name = re.sub('[^a-zA-Z]+', ' ', text).encode("utf-8")
        #print(text)
        job['startup'] = name
        job['jobs'] = number[0]
        site_web = driver.find_elements_by_partial_link_text(name)
        site_web1 = driver.find_elements_by_partial_link_text(text)
        site_web2 = driver.find_elements_by_partial_link_text(re.sub('[^a-zA-Z]+', ' ', text))
        if not site_web:
            if not site_web1:
                site_web = site_web2
            else:
                site_web = site_web1
        for h in site_web:
                adresse = h.get_attribute("href")
                job['site web'] = adresse

        if not site_web:
            job['site web'] = "None"


        print(job)

        jobs.append(job)
    #print(job)

    print("page scrapped %s" %j)

print(jobs)
Convert_to_csv(jobs)