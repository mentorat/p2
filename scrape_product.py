import os

import requests
from requests import get

from bs4 import BeautifulSoup


import csv

books =[]
book = {}

url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

#PRODUCT PAGE URL :
book["product_page_url"] = url

#TITLE :
title = soup.h1.string
book["title"] = soup.h1.string

#UPC+ PRICE inc Tx + PRICE ex TAX + NUMBER AVAILABLE :
table_striped = soup.find(class_="table table-striped")
td = table_striped.find_all("td")
book["universal_product_code"] = td[0].string
book["price_including_tax"] = td[3].string
book["price_excluding_tax"] = td[2].string
book["number_available"] = td[5].string

#PRODUCT DESCRIPTION :
p = soup.find_all("p")
book["product_description"] = p[3].string

#CATEGORY :
# trouver une maniere + courte pour category
breadcrumb = soup.find(class_= "breadcrumb")
a = breadcrumb.find_all("a")
book["category"] = a[2].string

#REVIEW_RATING :
stars = soup.find(class_="col-sm-6 product_main")
book["review_rating"] = len(stars.find_all(class_= "icon-star"))
#IMAGE :
image = soup.find("img")
book["image_url"] = url + image["src"]

#si on veut creer une page CSV pour le livre :
with open(str(title)+".csv", "w", newline="", encoding="utf8") as file :
    writer = csv.DictWriter(file, fieldnames=book.keys(), delimiter=";")
    writer.writeheader()
    writer.writerow(book)

os.system("pause") 


