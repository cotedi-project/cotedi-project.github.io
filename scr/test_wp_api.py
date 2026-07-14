"""from wp_api import WPClient

client = WPClient(base_url="https://imaginatic.es")

# List published posts, number of post here 5, chose page 1 or 2, orderby
posts = client.posts.list(status="publish", per_page=1, page=1, orderby="date")
for post in posts:
    print(post['id'], post['title']['rendered'], post['date'][:10], post['content']['rendered'], post['link'], post['author'])  # Print first 100 characters of content """


# TODO: hero, language and partner fields are not available in the API, so we need to find a way to get them. 
# TODO: Use same description body as the website
# TODO: Automatically generate the YAML front matter for each post, including the hero image, language, and partner fields.
# TODO: SAX parser

from wp_api import WPClient
from html.parser import HTMLParser
from wp_api.auth import ApplicationPasswordAuth
from pathlib import Path
import re
import os

# https://stackoverflow.com/questions/76390320/how-do-i-include-github-secrets-in-a-python-script
username = os.environ.get("WP_USERNAME")
password = os.environ.get("WP_PASSWORD")

# Authenticate with WordPress using application password
auth = ApplicationPasswordAuth(username=username, app_password=password)
client = WPClient(base_url="https://imaginatic.es", auth=auth)

# Get published posts
posts = client.posts.list(status="publish", per_page=2, page=1, orderby="date")

# Get published media items
media_items = client.media.list(media_type="image", per_page=100, page=1)


# Loop through the posts and save them to Markdown files
# YAML ausgeben 
for post in posts:
    post_id   = post['id']
    title     = post['title']['rendered']
    date      = post['date'][:10]  # just the YYYY-MM-DD part
    content   = post['content']['rendered']
    link      = post['link']
    type      = post['type']
    tags      = post['tags']
    # language  = post['language']

    # Fetch author name
    author_id = post['author']
    author    = client.users.get(author_id)
    author_name = author['name']

    # Fetch media items for the post
    media_items = []


    # Create a directory for the post in the docs/news folder with id_number

    docs_dir = Path(__file__).resolve().parent.parent / "docs/news"

    page_dir = docs_dir / f"page_wp_{post_id}"  # Use post ID for unique directory name
    page_dir.mkdir(parents=True)

    # Create the Markdown content yaml preamble
    page_content = f"""---
title: {title}
author: {author_name}
date: {date}
type: {type}
tags: {tags}
hero: {media_items if media_items else 'No image available'}
link: {link}
partner:
language:
description: |
    {content[:200]}...
---
{content}
"""
    # Save the Markdown file
    (page_dir / "index.md").write_text(page_content, encoding="utf-8")
    print(f"Saved post to {page_dir / 'index.md'}")
