import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url)

soup = BeautifulSoup(
response.text,
"html.parser"
)

print("\nHeadlines\n")

for headline in soup.find_all("h2")[:5]:

    print(
    headline.get_text()
    )