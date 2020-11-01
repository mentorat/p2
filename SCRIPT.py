import os

import requests

from requests import get

from bs4 import BeautifulSoup

import csv

import main

url = "http://books.toscrape.com/"

path = "BooksToScrape"

category_url = main.get_categories_urls(url, path)

print("\n\n" +"WELCOME TO BOOKS To SCRAPE"+ "\n\n")
print("A folder BookToScrape has been created. Open categories.csv and copy the category's url you want to scrape"+ "\n\n")
continue_scrape = True

while continue_scrape:
    choice = input("Which category would you like to scrape ?"+"\n\n")
    choice = str(choice)
    print("\n"+"Loading ... "+"\n")
    if choice in category_url:
        main.get_books_details(choice)
        more_scrape = input("Would you like to scrape an other category ? Y/N \n")
        if more_scrape in ["N", "n", "no", "NO"]:
            print("Thank you for using our app !\n")
            continue_scrape = False
        else :
            continue_scrape
    else:
        print("Incorrect adrress. Please try again.\n")
        continue_scrape
os.system("pause") 