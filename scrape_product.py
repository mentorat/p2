import os

import requests
from requests import get

from bs4 import BeautifulSoup

import numpy as np

import time

#SCRAPER LES INFOS D UN LIVRE  SUR SA PAGE 

url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

#PRODUCT PAGE URL :
product_page_url = url

#TITLE :
title = soup.h1.string

#UPC+ PRICE inc Tx + PRICE ex TAX + NUMBER AVAILABLE :
table_striped = soup.find(class_="table table-striped")
td = table_striped.find_all("td")
universal_product_code = td[0].string
price_including_tax = td[3].string
price_excluding_tax = td[2].string
number_available = td[5].string

#PRODUCT DESCRIPTION :
p = soup.find_all("p")
product_description = p[3].string

#CATEGORY :
# trouver une maniere + courte pour category
breadcrumb = soup.find(class_= "breadcrumb")
a = breadcrumb.find_all("a")
category = a[2].string

#REVIEW_RATING :
stars = soup.find(class_="col-sm-6 product_main")
review_rating = len(stars.find_all(class_= "icon-star"))

#IMAGE :
image = soup.find("img")
image_url = url + image["src"]

#si on veut creer une page CSV par livre :
#product.to_csv("product.to_csv")

os.system("pause") 


