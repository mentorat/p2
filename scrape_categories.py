import os

import requests
from requests import get

from bs4 import BeautifulSoup

import numpy as np

import time

url = "http://books.toscrape.com/" 
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
list_category = soup.find(class_= "nav nav-list")
li = list_category.find_all("li")
category_url =[url + item.find("a", href= True).get("href") for item in  li]
print(category_url)

# si on veut creer une page CSV des categories:

#category.to_csv("accueil.to_csv")
os.system("pause") 