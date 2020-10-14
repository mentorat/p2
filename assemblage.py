import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import numpy as np

url = "http://books.toscrape.com/" 
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
liste_category = soup.find(class_= "nav nav-list")
li = liste_category.find_all("li")
category_url =[url + item.find("a", href= True).get("href") for item in  li]

print(category_url[1])

for books in category_url[1] :
    books = [] #va contenir la liste des titres de tous les livres de la categorie
    url_books = []#va contenir la liste des urls des livres de la categorie
    page_category = requests.get(category_url[1])
    soup_category = BeautifulSoup(page_category.content, "html.parser")
    book_div = soup_category.find_all("article", class_="product_pod")
    for container in book_div:
        book = container.h3.a.text # le titre du livre est contenu dans a qui est contenu dans h3, il faut prendre le texte
        books.append(book) # on ajoute la valeur de book a la liste book
        url_book = container.h3.a.get("href")# url est contenu dans a qui est contenu dans h3, on veut la valeur de href
        url_books.append(url_book)# on ajoute url a la liste url_books
print(len(books))



