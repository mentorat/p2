import os

import requests
from requests import get

from bs4 import BeautifulSoup

import numpy as np

import time
categories_url = []

url = "http://books.toscrape.com/" 
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
list_category = soup.find(class_= "nav nav-list")
li = list_category.find_all("li")
for item in li :
    category_url = url + item.find("a", href= True).get("href")
    categories_url.append(category_url)
time.sleep(1)

with open("urlcategories.txt", "w") as file :
    for category_url in categories_url :
        file.write(str(category_url) + "\n")

# si on veut creer une page CSV des categories:        
#category.to_csv("accueil.to_csv")
os.system("pause") 