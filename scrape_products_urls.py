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

print(products_url) 

with open("urlbooks.txt", "w") as file :
    for product_page_url in products_url :
        file.write(str(product_page_url) + "\n")      

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
