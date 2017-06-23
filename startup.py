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

def Convert_to_csv(List_of_docs):

    keys = ['id', 'name', 'tagline','adresse_web','jobs' ]
    with open('angel_co_jobs.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(List_of_docs)

PATH = 'C:/Users/vtec-mchen/PycharmProjects/chromedriver.exe'
Login = ["myouhu@yahoo.fr", "bismilah"]
List_of_docs = []
driver = webdriver.Chrome(PATH)
driver.get('http://lespepitestech.com/french-tech-hub/nice')
startups = driver.find_elements_by_tag_name('h3')
tagline = driver.find_elements_by_css_selector('p.text-muted')
dict = {}

for i in startups:
    dict["startup"] = i.text.encode("utf-8")

for j in tagline:
    dict["tagline"] = j.text.encode("utf-8")

print (dict)
