import os
import requests
from requests import get

from bs4 import BeautifulSoup


def get_category(url, path):
    categories_urls = []
    categories_name = []
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

    try: 
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            Raise
    os.chdir(path) 


    with open("categories.csv", "w", newline="", encoding="utf8") as csvfile :
        for category_url in categories_urls :
            csvfile.write(str(category_url)+"\n")
    csvfile.close()
    return()


def get_books(choice):
    products_urls = []
    books =[]
    header =["product_page_url","universal_product_code","title","price_including_tax","price_excluding_tax","number_available","product_description","category","review_rating","image_url"]
    book ={}
    page1 = requests.get(choice)
    soup1 = BeautifulSoup(page1.content, 'html.parser')
    category_title = soup1.find(class_="page-header action")
    book_div = soup1.find_all("article", class_="product_pod")
    for container in book_div:
        product_page_url = "http://books.toscrape.com/catalogue/" + container.h3.a.get("href").replace('../', '')
        products_urls.append(product_page_url)

    for i in range(2,10) :
        url2 = choice.replace("index.html","page-")+str(i)+".html"
        page1 = requests.get(url2)
        soup2 = BeautifulSoup(page1.content,'html.parser').get_text().strip()
        book_div = soup2.find_all("article", class_="product_pod")
        for container in book_div:
            product_page_url = "http://books.toscrape.com/catalogue/" + container.h3.a.get("href").replace('../', '')
            products_urls.append(product_page_url)

    path_cat = category_title
    try: 
        os.makedirs(path_cat)
    except OSError:
        if not os.path.isdir(path_cat):
            Raise
    os.chdir(path_cat)

    with open(category_title+"_url.csv", "w", newline="", encoding="utf8") as csvfile :
        for product_page_url in products_urls:
            csvfile.write(str(product_page_url)+"\n")
    csvfile.close()

    with open(category_title+"_url.csv", "r") as inf:
        with open(category_title+"_books.csv", "w", newline="", encoding="utf8") as outf :
            writer = csv.DictWriter(outf, fieldnames=header, delimiter=";")
            writer.writeheader()
            for row in inf:
                url3 = row.strip()
                page3 = requests.get(url3)
                soup3 = BeautifulSoup(page3.content, "html.parser")
                book["product_page_url"] = url3
                title = soup3.h1.string
                book["title"] = title
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
                file = open(title +".jpg", "wb")
                file.write(images.content)
                file.close()
                writer.writerow(book)
        outf.close()
    inf.close()

    print("Un dossier "+ category_title +" a été créé contenant toutes les informations de chaque livre de la categorie.\n")
    return()