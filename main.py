import os

import requests

from requests import get

from bs4 import BeautifulSoup

import csv

import scrape

url = "http://books.toscrape.com/"

path = "BooksToScrape"

categories_urls = scrape.get_categories_urls(url, path)

print("\n\n" +"WELCOME TO BOOKS To SCRAPE"+ "\n\n")
print("A folder BookToScrape has been created. Open categories.csv and copy the category's url you want to scrape"+ "\n\n")
continue_scrape = True

while continue_scrape:
    choice = input("Which category would you like to scrape ?"+"\n\n")
    if choice not in categories_urls:
        print("Incorrect adrress. Please try again.\n")
    else : 
        scrape.get_all(choice)
    print("\n"+"Loading ... "+"\n")
    more_scrape = input("Would you like to scrape an other category ? Y/N \n")
    if more_scrape.lower() in ("n", "no"):
        print("Thank you for using our app !\n")
        continue_scrape = False
        

