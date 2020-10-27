import os

import requests

from requests import get

from bs4 import BeautifulSoup

import csv

categories_urls = []
categories_name = []
products_urls = []
header =["product_page_url","universal_product_code","title","price_including_tax","price_excluding_tax","number_available","product_description","category","review_rating","image_url"]
books =[]
book ={}

url = "http://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
list_category = soup.find(class_= "nav nav-list")
li = list_category.find_all("li")
for item in li :
    cate_url = str(url + item.find("a", href= True).get("href"))
    category_url = cate_url.replace("http", "https")
    categories_urls.append(category_url)
    category_name = item.find("a").get_text().strip()
    categories_name.append(category_name)

path = 'BooksToScrape'
exist_ok=False
    os.makedirs(path, exist_ok=True)
    os.chdir(path)

with open("categories.csv", "w", newline="", encoding="utf8") as csvfile :
    for category_url in categories_urls :
        csvfile.write(str(category_url)+"\n")

print("WELCOME TO BOOKS To SCRAPE \n\n")

continue_scrape = True

while continue_scrape :
    choice = input("Which category would you like to scrape ?\n\n")
    print("Loading ... "+"\n")
    if choice in categories_urls :
        page1 = requests.get(choice)
        soup1 = BeautifulSoup(page1.content, 'html.parser')
        category_title = soup1.find(class_="page-header action").get_text().strip()
        book_div = soup1.find_all("article", class_="product_pod")
        for container in book_div:
            product_page_url = "http://books.toscrape.com/catalogue/" + container.h3.a.get("href").replace('../', '')
            products_urls.append(product_page_url)

        for i in range(2,10) :
            url2 = choice.replace("index.html","page-")+str(i)+".html"
            page1 = requests.get(url2)
            soup2 = BeautifulSoup(page1.content,'html.parser')
            book_div = soup2.find_all("article", class_="product_pod")
            for container in book_div:
                product_page_url = "http://books.toscrape.com/catalogue/" + container.h3.a.get("href").replace('../', '')
                products_urls.append(product_page_url)

        exist_ok=False
        os.makedirs(category_title, exist_ok=True)
        with open(category_title+"_url.csv", "w", newline="", encoding="utf8") as csvfile :
            for product_page_url in products_urls:
                csvfile.write(str(product_page_url)+"\n")

        with open(category_title+"_url.csv", "r") as csvfile :
            with open(category_title+"_books.csv", "w", newline="", encoding="utf8") as outf :
                writer = csv.DictWriter(outf, fieldnames=header, delimiter=";")
                writer.writeheader()
                for row in csvfile:
                    url3 = row.strip()
                    page3 = requests.get(url3)
                    soup3 = BeautifulSoup(page3.content, "html.parser")
                    book["product_page_url"] = url3
                    title = soup3.h1.string
                    book["title"] = title
                    cleaned_title = [char for char in title if char.isalnum()]
                    result ="".join(cleaned_title)
                    table_striped = soup3.find(class_="table table-striped")
                    td = table_striped.find_all("td")
                    book["universal_product_code"] = td[0].string
                    book["price_including_tax"] = td[3].string
                    book["price_excluding_tax"] = td[2].string
                    book["number_available"] = td[5].string
                    p = soup3.find_all("p")
                    book["product_description"] = p[3].string
                    breadcrumb = soup3.find(class_= "breadcrumb")
                    a = breadcrumb.find_all("a")
                    book["category"] = a[2].string
                    stars = soup3.find(class_="col-sm-6 product_main")
                    book["review_rating"] = len(stars.find_all(class_= "icon-star"))
                    image = soup3.find("img")
                    image_url = "https://books.toscrape.com" + image["src"].replace("../..","").replace("../../../..","")
                    book["image_url"] = image_url
                    books.append(book)
                    images = requests.get(image_url)
                    file = open(str(result)+".jpg", "wb")
                    file.write(images.content)
                    file.close()  
                    writer.writerow(book)
    
        print("Congradulation ! \n\n")

        more_scrape = input("Would you like to scrape an other category ? Y/N \n")
        if more_scrape in ["N", "n", "no", "NO"]:
            print("Thank you for using our app !\n")
            continue_scrape = False
        else :
            continue_scrape

    elif choice == "https://books.toscrape.com/catalogue/category/books_1/index.html":
        print("Adresse URL invalide, Veuillez reessayer.")
        continue_scrape
    else :
        print("Incorrect adrress. Please try again.\n")
        continue_scrape
        
os.system("pause") 

#A FAIRE
# trouver comment avoir fieldnames=book.keys()