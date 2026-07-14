from collections import deque
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests

base_url = "https://imaginatic.es"
seed_urls = [
    "https://imaginatic.es/cotedi/"
]

seen = set()
queue = deque(seed_urls)

while queue:
    url = queue.popleft()
    if url in seen:
        continue
    seen.add(url)

    html = requests.get(url, timeout=20).text
    soup = BeautifulSoup(html, "html.parser")

    print("\nPAGE:", url)

    for a in soup.find_all("a", href=True):
        link = urljoin(url, a["href"])
        parsed = urlparse(link)

        if parsed.netloc != urlparse(base_url).netloc:
            continue

        if link not in seen:
            print("  found:", link)
            queue.append(link)