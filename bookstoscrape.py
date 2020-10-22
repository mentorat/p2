import os

import requests
from requests import get

from bs4 import BeautifulSoup

import csv


path = 'BooksToScrape'
try: 
 os.makedirs(path)
except OSError:
    if not os.path.isdir(path):
        Raise
os.chdir(path) #ouvre le fichier path et va enregistrer les fichiers csv dedans

producs_urls = []
categories_name = []
categories_urls = []
books =[]
book ={}
header =["product_page_url","universal_product_code","title","price_including_tax","price_excluding_tax","number_available","product_description","category","review_rating","image_url"]

url = "http://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
list_category = soup.find(class_= "nav nav-list")
li = list_category.find_all("li")

for item in li :
    category_url = url + item.find("a", href= True).get("href")
    categories_urls.append(category_url)
    category_name = item.find("a").get_text().strip()
    categories_name.append(category_name)

with open("categories.csv", "w", newline="", encoding="utf8") as csvfile :
    for category_url in categories_urls :
        csvfile.write(str(category_url)+"\n")
csvfile.close()

print("BIENVENUE SUR BOOK to SCRAPE : ")
choice = input("Quelle est l'URL de la categorie voulez vous scraper ? "+"\n")
print("Veuillez patienter ... "+"\n")

page1 = requests.get(choice)
soup1 = BeautifulSoup(page1.content, 'html.parser')
category_title = soup1.find(class_="page-header action").get_text().strip()
book_div = soup1.find_all("article", class_="product_pod")
for container in book_div:
    product_page_url = "http://books.toscrape.com/catalogue/" + container.h3.a.get("href").replace('../../../', '').replace("../../", "")
    producs_urls.append(product_page_url)

for i in range(2,10) :
    url = choice.replace("index.html","page-")+str(i)+".html"
    page1 = requests.get(url)
    soup1 = BeautifulSoup(page1.content, 'html.parser')
    book_div = soup1.find_all("article", class_="product_pod")
    for container in book_div:
        product_page_url = "http://books.toscrape.com/catalogue/" + container.h3.a.get("href").replace('../../../', '').replace("../../", "")
        producs_urls.append(product_page_url)

print("La categorie contient : " + str(len(producs_urls))+" livres.")
print("Veuillez patienter ... "+"\n")

path_cat = category_title
try: 
 os.makedirs(path_cat)
except OSError:
    if not os.path.isdir(path_cat):
        Raise
os.chdir(path_cat)

with open(category_title+"_url.csv", "w", newline="", encoding="utf8") as csvfile :
    for product_page_url in producs_urls:
        csvfile.write(str(product_page_url)+"\n")
csvfile.close()
with open(category_title+"_url.csv", "r") as inf :
    with open(category_title+"_books.csv", "w", newline="", encoding="utf8") as outf :
        writer = csv.DictWriter(outf, fieldnames=header, delimiter=";")
        writer.writeheader()
        for row in inf:
            url = row.strip()
            page1 = requests.get(url)
            soup = BeautifulSoup(page1.content, "html.parser")
            book["product_page_url"] = url
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
            book["image_url"] = url + image["src"]
            books.append(book)
            writer.writerow(book)
    outf.close()
inf.close()
print("Un dossier "+ category_title +"a été créé contenant toutes les informations de chaque livre de la categorie.")

os.system("pause") 

#A FAIRE
# trouver comment avoir fieldnames=book.keys()
# integrer le propgramme dans la boucle if/else
# boucle en cas de else : redemander une categorie valide
# boucle pour demander une autre categorie
# recuperer les images
# mise en page des fichiers csv
