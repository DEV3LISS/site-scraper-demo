import requests, csv
from bs4 import BeautifulSoup

url = "https://habr.com/ru/all/"
soup = BeautifulSoup(requests.get(url).text, "html.parser")
rows = [[h.text.strip()] for h in soup.select("article h2")]

with open("posts.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(rows)

print("Сохранил", len(rows), "заголовков")
