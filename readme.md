WEB SCRAPING -  BOOKS TO SCRAPE <br>
<br>
## OVERVIEW
Beta version of a system for tracking book prices at Books to Scrape, an on-demand runtime application aimed at retrieving prices at runtime.
<br>
<br>
## REQUISITORIES <br>
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



- Start access the project folder

- Create a virtual environment
```
python -m venv mon_env
```

- Enable the virtual environment
```
cd mon_env/scripts
```
```
source activate
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
```
## LAUNCH 

Run scripts.py to start<br>
Creation of  a BooksToScrape repertory containing a categorie.csv file<br>
Copy/ Paste the url of the category wanted<br>
Creation of a folder named by the category containing :<br>
- a picture of all books 
- a csv file with all the books<br>
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

