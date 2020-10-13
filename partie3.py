import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com/" 
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
liste = soup.find(class_= "nav nav-list")
li =[]
li = liste.find_all("li")
category_url =[url + item.find("a", href= True).get("href") for item in  li]

category = pd.DataFrame(
    {
        "CATEGORY URL": category_url,
    })
print(category)

#category.to_csv("accueil.to_csv")