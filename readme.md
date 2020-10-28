WEB SCRAPING -  BOOKS TO SCRAPE <br>
<br>
## Overview
Beta version of a system for tracking book prices at Books to Scrape, an on-demand runtime application aimed at retrieving prices at runtime.
<br>
<br>
## PREREQUISITES <br>
<br>
Python3<br>
beautifulsoup4 <br>
requests <br>
<br>

## INSTALLATION 

Start by closing the repository :

```
git clone https://github.com/pascaline841/p2
```

We recommend to use `virtualenv` for development:

- Start by installing `virtualenv` if you don't have it
```
pip install virtualenv
```

- Once installed access the project folder
```
cd P02
```

- Create a virtual environment
```
virtualenv venv
```

- Enable the virtual environment
```
source venv/bin/activate
```

- Install the python dependencies on the virtual environment
```
pip install beautifulsoup4
```
```
pip install requests
```

- Start the application
```
./script.py

## LAUNCH 
<br>
Run scripts.py to start<br>
Creation of  a BooksToScrape repertory containing a categorie.csv file<br>
Copy/ Paste the url of the category wanted : <br>
Creation of a folder named by the category containing :<br>
- a picture of all books <br>
- a csv file with all the books : <br>
<br>
the additional informations are :<br>
- Product_page_url<br>
- Universal_produit_code (upc)<br>
- Title<br>
- Price_including_tax <br>
- Price_excluding_tax <br>
- Number_available <br>
- Product Description <br>
- Category <br>
- Review_rating <br>
- Image URL <br>

