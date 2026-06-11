import requests
from bs4 import BeautifulSoup
import json

url = "https://www.bbc.com/news"

response = requests.get(url)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

headlines = []

for headline in soup.find_all("h2")[:5]:

    headlines.append(
        headline.get_text()
    )

with open(
    "news.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        headlines,
        file,
        indent=4,
        ensure_ascii=False
    )

print("News updated")