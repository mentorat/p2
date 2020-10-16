import os

import requests
from requests import get

from bs4 import BeautifulSoup

import pandas as pd
import numpy as np
import time


url = "http://books.toscrape.com/catalogue/"

products_url = [] #va contenir la liste des urls des livres de la categorie
pages = np.arange(1, 3, 1) # debute page 1, termine page 2, va de 1 en 1
for page in pages: #page est la variable iteree dans pages creee ci dessus
    page = requests.get("http://books.toscrape.com/catalogue/category/books/mystery_3/page-" + str(page) + ".html")
    soup = BeautifulSoup(page.text, 'html.parser')
    book_div = soup.find_all("article", class_="product_pod")
    for container in book_div:
        product_page_url = url + container.h3.a.get("href").replace('../../../', '')
        products_url.append(product_page_url)
    time.sleep(1)

with open("urlbooks.txt", "w") as file :
    for product_page_url in products_url :
        file.write(str(product_page_url) + "\n")      

with open("urlbooks.txt", "r") as file :
    for row in file :
        url = row.strip()
        page1 = requests.get(url)
        if page1.ok :
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
            print( "TITLE : " + title)
        time.sleep(1)



"""#creation d un tableau avec pandas DataFrame
my_work = pd.DataFrame( 
    {
        "TITLE : ": books,
        "URL" : products_url,
    })
print(my_work)

#creation d un fichier CSV contenant le tableau ordoné
#my_work.to_csv("toutelacategory.to_csv")"""

os.system("pause") 
