import os

import requests
from requests import get

from bs4 import BeautifulSoup

import numpy as np

import time

import csv


url = "http://books.toscrape.com/" 
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
list_category = soup.find(class_= "nav nav-list")
li = list_category.find_all("li")
category_name = [item.find("a").text for item in li] # trouver comment obtenir  QUE le texte sans mise en page
category_url =[url + item.find("a", href= True).get("href") for item in  li]


#creation fichier CSV des categories + url :

with open("categories.csv", "w") as file :
    file.write("CATEGORY :, URL CATEGORY :\n")

os.system("pause") 
