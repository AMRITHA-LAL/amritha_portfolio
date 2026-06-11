import requests
from bs4 import BeautifulSoup
import json

sites = [

    "https://www.bbc.com/news",

    "https://www.reuters.com/world",

    "https://edition.cnn.com/world"

]

headlines = []

for site in sites:

    try:

        response = requests.get(site)

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        for h in soup.find_all(
            ["h1","h2","h3"]
        )[:3]:

            headlines.append(
                h.get_text().strip()
            )

    except:

        pass

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

print("News Updated")