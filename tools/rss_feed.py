import requests
from bs4 import BeautifulSoup

def read_rss(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "xml")

    items = soup.find_all("item")[:5]

    return [
        {"title": i.title.text, "link": i.link.text, "description": i.description.text}
        for i in items
    ]

