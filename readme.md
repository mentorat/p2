BOOKS ONLINE  -   BOOKS to SCRAPE

Version bêta d'un système pour suivre les prix des livres chez Books to Scrape, une application exécutable à la demande visant à récupérer les prix au moment de son exécution.

PRE-REQUIS :<br>
<br>
Python3 <br>
pip install beautifulsoup4 <br>
pip install requests <br>
<br>
LANCEMENT :<br>
<br>
Executez bookstoscrape.py pour commencer <br>
Creation d'un dossier BooksToScrape contenant un fichier categorie.csv <br>
Copier/copier l'url de la categorie de livres a scraper <br>
Creation d'un dossier au nom de la categorie  contenant : <br>
    - un fichier csv des urls de tous les livres<br>
    -les images de tous les livres<br>
    - un fichier csv des informations de tous les livres :<br>
        les informations extraites sont :<br>
            -product_page_url <br>
            -universal_ product_code (upc)<br>
            -title<br>
            -price_including_tax <br>
            -price_excluding_tax <br>
            -number_available <br>
            -product_description <br>
            -category <br>
            -review_rating <br>
            -image_url<br>
