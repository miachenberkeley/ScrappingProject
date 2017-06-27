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

    keys = ['startup', 'job']
    with open('Welcome_jungle_scrapping.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(List_of_docs)


jobs = []

for j in range(5):
    web_path = 'https://www.welcometothejungle.co/companies?q=&hPP=30&idx=cms_companies_production&p=' + str(j) + '&dFR%5Bcompany_size%5D%5B0%5D=Entre%2015%20et%2050%20salari%C3%A9s&is_v=1'
    driver.get(web_path)
    startups_name = driver.find_elements_by_tag_name("h4")
    job = {}
    for i in startups_name:
        text = i.text.split(" ")
        #print(text)
        job['startup'] = text[0]
        job['job'] = text[1]
    jobs.append(job)
    print("page scrapped %s" %j)

print(jobs)
Convert_to_csv(jobs)