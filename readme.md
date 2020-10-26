BOOKS ONLINE  -   BOOKS to SCRAPE

Version bêta d'un système pour suivre les prix des livres chez Books to Scrape, une application exécutable à la demande visant à récupérer les prix au moment de son exécution.

PRE-REQUIS :

Python3 
pip install beautifulsoup4
            requests

LANCEMENT :

Executez bookstoscrape.py pour commencer 
Creation d'un dossier BooksToScrape contenant un fichier categorie.csv 
Copier/copier l'url de la categorie de livres a scraper
Creation d'un dossier au nom de la categorie  contenant :
    - un fichier csv des urls de tous les livres
    -les images de tous les livres
    - un fichier csv des informations de tous les livres :
        les informations extraites sont :
            -product_page_url
            -universal_ product_code (upc)
            -title
            -price_including_tax
            -price_excluding_tax
            -number_available
            -product_description
            -category
            -review_rating
            -image_url