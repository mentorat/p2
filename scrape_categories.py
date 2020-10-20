import os

import requests
from requests import get

from bs4 import BeautifulSoup

import numpy as np

import csv

categories_urls =[]
url = "http://books.toscrape.com/" 
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
list_category = soup.find(class_= "nav nav-list")
li = list_category.find_all("li")
for item in li :
    category_url= url + item.find("a", href= True).get("href")
    categories_urls.append(category_url)

#creation fichier CSV des categories + url :
with open("categories.csv", "w",) as csvfile :
    for category_url in categories_urls :
        csvfile.write(str(category_url)+"\n")
      
os.system("pause") 
