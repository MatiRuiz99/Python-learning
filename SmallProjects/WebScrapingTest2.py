import requests
from bs4 import BeautifulSoup

for i in range(1, 6):  # Las 5 primeras páginas
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")   
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text 
        print(f"{title} - {price}")

