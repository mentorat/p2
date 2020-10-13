import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
url = input("Entrez l'adresse d'un produit : " )
#url = "http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html" 
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

product =pd.Series({
    "PRODUCT PAGE URL: ": product_page_url,
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
#changer pd.Series pour DataFrame

#product.to_csv("product.to_csv")
os.system("pause") 


