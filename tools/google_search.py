import requests
from bs4 import BeautifulSoup

def google_search(query: str):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}

    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")

    results = []
    for container in soup.select(".tF2Cxc")[:5]:
        title = container.select_one("h3").text if container.select_one("h3") else ""
        snippet = container.select_one(".VwiC3b").text if container.select_one(".VwiC3b") else ""

        results.append({
            "title": title,
            "snippet": snippet
        })

    return results

