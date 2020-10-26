import os

import requests

from requests import get

from bs4 import BeautifulSoup

import csv

import main

url = "http://books.toscrape.com/"

path = 'BooksToScrape'

print("BIENVENUE SUR BOOK to SCRAPE : \n\n")

continuer_scraper = True
while continuer_scraper :
    choice = input("Quelle est l'URL de la categorie voulez vous scraper ? "+"\n")
    choice = str(choice)
    print("Veuillez patienter ... "+"\n")

    with open("categories.csv") as csvfile :
        for choice in csvfile : 
            main.get_books(choice)

            encore = input("Voulez-vous scraper une autre categorie de livre?   O/N \n")
            if encore == "N" or encore == "n" or encore =="non" or encore =="NON":
                print("Merci et a bientot!\n")
                continuer_scraper = False
            else :
                continuer_scraper
        elif choice == "https://books.toscrape.com/catalogue/category/books_1/index.html":
            print("Adresse URL invalide, Veuillez reessayer.")
            continuer_scraper
        else :
            print("Adresse URL invalide, Veuillez reessayer.\n")
            continuer_scraper
    csvfile.close()    

os.system("pause") 
    