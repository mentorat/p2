import os

import requests
from requests import get

from bs4 import BeautifulSoup

import csv

def get_categories_urls(url,path):
    categories_urls = []
    categories_name = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    li = soup.find(class_= "nav nav-list").find_all("li")
    for item in li :
        category_url = str(url + item.find("a", href= True).get("href")).replace("http", "https")
        categories_urls.append(category_url)
        category_name = item.find("a").get_text().strip()
        categories_name.append(category_name)
    exist_ok=False
    os.makedirs(path, exist_ok=True)
    os.chdir(path)
    with open("categories.csv", "w", newline="", encoding="utf8") as csvfile :
        for category_url in categories_urls :
            csvfile.write(str(category_url)+"\n")
    return categories_urls

def get_category_name(choice, ) :
    page = requests.get(choice)
    soup = BeautifulSoup(page.content, 'html.parser')
    category = soup.find(class_="page-header action").get_text().strip()
    exist_ok=False
    os.makedirs(category, exist_ok=True)
    return category

def get_products_url(choice):
    products_urls = []
    page = requests.get(choice)
    soup = BeautifulSoup(page.content, 'html.parser')
    book_div = soup.find_all(class_="product_pod")
    for container in book_div:
        product_page_url = "http://books.toscrape.com/catalogue/" + container.h3.a.get("href").replace('../', '')
        products_urls.append(product_page_url)
    for i in range(2,10) :
        url = choice.replace("index.html","page-")+str(i)+".html"
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'html.parser')
        book_div = soup.find_all("article", class_="product_pod")
        for container in book_div:
            product_page_url = "http://books.toscrape.com/catalogue/" + container.h3.a.get("href").replace('../', '')
            products_urls.append(product_page_url)
    return  products_urls

def get_books_details(choice):
    category_title = get_category_name(choice)
    products_urls = get_products_url(choice)
    with open(os.path.join(category_title, category_title+"_books.csv"), "w", newline="", encoding="utf8") as csvfile:
        header =["product_page_url","universal_product_code","title","price_including_tax","price_excluding_tax","number_available","product_description","category","review_rating","image_url"]
        writer = csv.DictWriter(csvfile, fieldnames=header, delimiter=";")
        writer.writeheader()
        book ={}
        for product_page_url in products_urls:
            page = requests.get(product_page_url)
            soup = BeautifulSoup(page.content, "html.parser")
            book["product_page_url"] = product_page_url
            title = soup.h1.string
            book["title"] = title
            cleaned_title ="".join([char for char in title if char.isalnum()])
            td = soup.find(class_="table table-striped").find_all("td")
            book["universal_product_code"] = td[0].string
            book["price_including_tax"] = td[3].string
            book["price_excluding_tax"] = td[2].string
            book["number_available"] = td[5].string
            p = soup.find_all("p")
            book["product_description"] = p[3].string
            a = soup.find(class_= "breadcrumb").find_all("a")
            book["category"] = a[2].string
            book["review_rating"] = len(soup.find(class_="col-sm-6 product_main").find_all(class_= "icon-star"))
            image = soup.find("img")
            image_url = "https://books.toscrape.com" + image["src"].replace("../..","").replace("../../../..","")
            book["image_url"] = image_url  
            writer.writerow(book)    
            images = requests.get(image_url) 
            with open(os.path.join(category_title, cleaned_title+".jpg"), "wb") as file:
                file.write(images.content)
    print(" Congratulation, a folder named " + category_title + " has been created. It contains all the pictures from books and details in a file.csv.")        
          
