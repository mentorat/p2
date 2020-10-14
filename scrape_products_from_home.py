import os

import requests
from requests import get

from bs4 import BeautifulSoup

import pandas as pd
import numpy as np

url = "http://books.toscrape.com/"
products_url = [] #va contenir la liste des urls des livres 
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
book_div = soup.find_all("article", class_="product_pod")
for container in book_div:
    product_page_url = url + container.h3.a.get("href")
    products_url.append(product_page_url)

for items in products_url : # remplacer items pour que la demande soit generique
    page1 = requests.get(products_url[3])  #va etudier le 4eme livre
    soup1 = BeautifulSoup(page1.content, "html.parser")
    title = soup1.h1.string
    table_striped = soup1.find(class_="table table-striped")
    td = table_striped.find_all("td")
    universal_product_code = td[0].string
    price_including_tax = td[3].string
    price_excluding_tax = td[2].string
    number_available = td[5].string
    p = soup1.find_all("p")
    product_description = p[3].string
    breadcrumb = soup1.find(class_= "breadcrumb")
    a = breadcrumb.find_all("a")
    category = a[2].string
    stars = soup1.find(class_="col-sm-6 product_main")
    review_rating = len(stars.find_all(class_= "icon-star"))
    image = soup1.find("img")
    image_url = url + image["src"]
        
product =pd.Series({
    "PRODUCT_PAGE_URL : ": product_page_url,
    "UNIVERSAL PRODUCT CODE : ": universal_product_code,
    "TITLE : " : title,
    "PRICE INCLUDING TAX : ": price_including_tax,
    "PRICE EXCLUDING TAX : ": price_excluding_tax,
    "NUMBER AVAILABLE : ": number_available,
    "PRODUCT DESCRIPTION" : product_description,
    "CATEGORY : ": category,
    "REVIEW_RATING : ": review_rating,
    "IMAGE_URL : ": image_url,
    })

print(product)
os.system("pause") 