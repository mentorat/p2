import os

import requests
from requests import get

from bs4 import BeautifulSoup

import numpy as np

import time

import csv

#creation d une liste contenant les url des categories :
def category():
    categories_urls =[]
    url = "http://books.toscrape.com/" 
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    list_category = soup.find(class_= "nav nav-list")
    li = list_category.find_all("li")
    for item in li :
        category_url= url + item.find("a", href= True).get("href")
        categories_urls.append(category_url)
    #print(categories_urls)
    # #len(categories_urls)= 50    
    return

#CA FONCTIONNE 

def products():
    products_url = []
    for category_url in categories_urls :    
        #pages = np.arange(1, 10, 1)
        #url = category_url.replace("index.html","")
        #for page in pages:
        products_url = []
        page = requests.get(category_url)
        soup = BeautifulSoup(page.text, 'html.parser')
        book_div = soup.find_all("article", class_="product_pod")
        for container in book_div:
            product_page_url = "http://books.toscrape.com/catalogue/" + container.h3.a.get("href").replace('../../../', '').replace("../../", "")
            products_url.append(product_page_url)
    #print(products_url)
    #len(products_url)= 537
    return

#CA FONCTIONNE 

# creation dictionnaire qui va contenir les details dun livre
def books():
    for product_page_url in products_url :
        url_book = product_page_url
        page = requests.get(url_book)
        soup = BeautifulSoup(page.content, "html.parser")
        book["title"] = soup.h1.string
        table_striped = soup.find(class_="table table-striped")
        td = table_striped.find_all("td")
        book["universal_product_code"] = td[0].string
        book["price_including_tax"] = td[3].string
        book["price_excluding_tax"] = td[2].string
        book["number_available"] = td[5].string
        p = soup.find_all("p")
        book["product_description"] = p[3].string
        breadcrumb = soup.find(class_= "breadcrumb")
        a = breadcrumb.find_all("a")
        book["category"] = a[2].string
        stars = soup.find(class_="col-sm-6 product_main")
        book["review_rating"] = len(stars.find_all(class_= "icon-star"))
        image = soup.find("img")
        book["image_url"] = url_book + image["src"]
        books.append(book)
    #print(len(books))
    return()
