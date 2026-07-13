"""from wp_api import WPClient

client = WPClient(base_url="https://imaginatic.es")

# List published posts, number of post here 5, chose page 1 or 2, orderby
posts = client.posts.list(status="publish", per_page=1, page=1, orderby="date")
for post in posts:
    print(post['id'], post['title']['rendered'], post['date'][:10], post['content']['rendered'], post['link'], post['author'])  # Print first 100 characters of content """


# TODO: Get API User name and password
# TODO: hero, language and partner fields are not available in the API, so we need to find a way to get them. 
# TODO: Use same description body as the website
# TODO: Automatically generate the YAML front matter for each post, including the hero image, language, and partner fields.
# TODO: Implement a function that creats a new page in the Cotedi Repo
# TODO: Content als HTML lassen

from wp_api import WPClient
from html.parser import HTMLParser
from wp_api.auth import ApplicationPasswordAuth
from pathlib import Path
import re

# Simple HTML stripper 
class HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
    def handle_data(self, data):
        self.text.append(data)
    def get_text(self):
        return ''.join(self.text).strip()
# removes the Elementor HTML tags for plain text for the description/body
def strip_html(html):
    stripper = HTMLStripper()
    stripper.feed(html)
    return stripper.get_text()
auth = ApplicationPasswordAuth(username="noirin", app_password="WmX5 IHp8 5XYN jByj vqD4 nPLN")
client = WPClient(base_url="https://imaginatic.es", auth=auth)

# Get published posts
posts = client.posts.list(status="publish", per_page=1, page=1, orderby="date")

# Get published media items
media_items = client.media.list(media_type="image", per_page=100, page=1)

for post in posts:
    post_id   = post['id']
    title     = post['title']['rendered']
    date      = post['date'][:10]  # just the YYYY-MM-DD part
    content   = post['content']['rendered']
    link      = post['link']
    # language  = post['language']

    # Fetch author name
    author_id = post['author']
    author    = client.users.get(author_id)
    author_name = author['name']

    # Fetch media items for the post
    media_items = []



    docs_dir = Path(__file__).resolve().parent.parent / "docs/news"
    page_numbers = [
            int(match.group(1))
            for path in docs_dir.glob("page_wp_*")
            if path.is_dir()
            if (match := re.fullmatch(r"page_wp_(\d+)", path.name))
    ]
    next_page_number = max(page_numbers, default=0) + 1

    page_dir = docs_dir / f"page_wp_{next_page_number}"
    page_dir.mkdir(parents=True, exist_ok=False)

    page_content = f"""---
title: {title}
author: {author_name}
date: {date}
type: news
tags:
- news
hero: {media_items if media_items else 'No image available'}
link: {link}
partner:
language:
description: |
    {content[:200]}...
---
{content}
"""

    (page_dir / "index.md").write_text(page_content, encoding="utf-8")
    print(f"Saved post to {page_dir / 'index.md'}")
