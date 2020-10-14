import os

import requests
from requests import get

from bs4 import BeautifulSoup

import pandas as pd
import numpy as np

books = [] #va contenir la liste des titres de tous les livres de la categorie
products_url = [] #va contenir la liste des urls des livres de la categorie
pages = np.arange(1, 3, 1) # debute page 1, termine page 2, va de 1 en 1
for page in pages: #page est la variable iteree dans pages creee ci dessus
    page = requests.get("http://books.toscrape.com/catalogue/category/books/mystery_3/page-" + str(page) + ".html")
    soup = BeautifulSoup(page.content, 'html.parser')
    book_div = soup.find_all("article", class_="product_pod")
    for container in book_div:
        title = container.h3.a.text # le titre du livre est contenu dans a qui est contenu dans h3, il faut prendre le texte
        books.append(title) # on ajoute la valeur de book a la liste book
        product_page_url = container.h3.a.get("href")
        products_url.append(product_page_url)
print(products_url)       

#creation d un tableau avec pandas DataFrame
my_work = pd.DataFrame( 
    {
        "TITLE : ": books,
        "URL" : products_url,
    })
print(my_work)

#creation d un fichier CSV contenant le tableau ordoné
#my_work.to_csv("toutelacategory.to_csv")

os.system("pause") 
