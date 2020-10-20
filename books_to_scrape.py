import os

import requests
from requests import get

from bs4 import BeautifulSoup

import csv

categories_urls =[]
products_url = []
books =[]
book = {}

url = "http://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
list_category = soup.find(class_= "nav nav-list")
li = list_category.find_all("li")
for item in li :
    category_url = url + item.find("a", href= True).get("href")
    categories_urls.append(category_url)

#creation fichier CSV des categories + url :
with open("categories.csv", "w",) as csvfile :
    for category_url in categories_urls :
        csvfile.write(str(category_url)+"\n")

print("BIENVENUE SUR BOOK to SCRAPE : ")
choix = input("Quelle est l'URL de la categorie voulez vous scraper ? "+"\n")

if choix in categories_urls :
    print("Veuillez patienter ... "+"\n")
    #ca marche pour la 1ere page de la categorie
    page1 = requests.get(choix)
    soup1 = BeautifulSoup(page1.content, 'html.parser')
    book_div = soup1.find_all("article", class_="product_pod")
    for container in book_div:
        product_page_url = "http://books.toscrape.com/catalogue/" + container.h3.a.get("href").replace('../../../', '').replace("../../", "")
        products_url.append(product_page_url)
    print("La categorie contient : " + str(len(products_url))+" livres.")
    print("Veuillez patienter ... "+"\n")

    with open("products.csv", "w",) as csvfile :
        for product_page_url in products_url:
            csvfile.write(str(product_page_url)+"\n")

    for product_page_url in products_url :
        page1 = requests.get(product_page_url)
        soup = BeautifulSoup(page1.content, "html.parser")
        book["product_page_url"] = product_page_url
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
        category = a[2].string
        book["category"] = a[2].string
        stars = soup.find(class_="col-sm-6 product_main")
        book["review_rating"] = len(stars.find_all(class_= "icon-star"))
        image = soup.find("img")
        book["image_url"] = product_page_url + image["src"]
        books.append(book)

    with open(str(category)+".csv", "w", newline="", encoding="utf8") as out_file :
        writer = csv.DictWriter(out_file, fieldnames=book.keys(), delimiter=";")
        writer.writeheader()
        writer.writerow(book)
    print("Un fichier " + str(category)+ ".CSV a été créé avec tous les détails de chaque livre")
else :
    print("ERREUR ! VEUILLEZ RE ESSAYER ")

os.system("pause") 