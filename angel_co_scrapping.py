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

def Get_to_list(driver, url):
    driver.get(url)
    url2 = 'https://angel.co/paris/jobs'

    print('got to list')

def Convert_to_csv(List_of_docs):

    keys = ['Startup_name', 'Jobs',
            'Duration']
    with open('angel_co.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(List_of_docs)

