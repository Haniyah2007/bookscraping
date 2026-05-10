import requests
import csv
from bs4 import BeautifulSoup
url="https://books.toscrape.com/"
response= requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")
books=soup.find_all("article",class_="product_pod")
with open("books.csv","w",newline="",encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerow(["Book_Title","price"])

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").get_text()

        writer.writerow([title, price])

        print(title, price)



