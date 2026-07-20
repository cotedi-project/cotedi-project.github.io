"""from wp_api import WPClient

client = WPClient(base_url="https://imaginatic.es")

# List published posts, number of post here 5, chose page 1 or 2, orderby
posts = client.posts.list(status="publish", per_page=1, page=1, orderby="date")
for post in posts:
    print(post['id'], post['title']['rendered'], post['date'][:10], post['content']['rendered'], post['link'], post['author'])  # Print first 100 characters of content """



# TODO: Automatically generate the YAML front matter for each post, including the hero image, language, and partner fields.


from wp_api import WPClient
from html.parser import HTMLParser
from wp_api.auth import ApplicationPasswordAuth
from pathlib import Path
import re
import os
from bs4 import BeautifulSoup

# https://stackoverflow.com/questions/76390320/how-do-i-include-github-secrets-in-a-python-script
username = os.environ.get("WP_USERNAME")
password = os.environ.get("WP_PASSWORD")

# Authenticate with WordPress using application password
auth = ApplicationPasswordAuth(username=username, app_password=password)
client = WPClient(base_url="https://imaginatic.es", auth=auth)


# Get published posts
posts = client.posts.list(status="publish", per_page=10, page=1, orderby="date")

# print all keys
# print(list(posts[0].keys()))
# # Find language in the yoast_head_json field
# print(posts['yoast_head_json'])

# Get published media items
media_items = client.media.list(media_type="image", per_page=100, page=1)

# print all media items
# print(list(media_items[0].keys()))

# Raw YAML output for debugging
# print("Raw YAML output:")
# for post in posts:
#     print(post)

# Uses BeautifulSoup (bs4) to parse HTML into a navigable tree (DOM-style),
# then extracts and returns only the plain text content, stripped of all tags. 
def strip_html(html):
    return BeautifulSoup(html, "html.parser").get_text().strip()

# SAX is more memory-efficient for large documents.
# Is event-driven and does not build a tree structure in memory.
# https://docs.python.org/3/library/html.parser.html
# class HTMLStripper(HTMLParser):
#     # set up parser to handle data and store it in a empty list
#     def __init__(self):
#         super().__init__()
#         self.text = []
#     # This method is called to process arbitrary data
#     def handle_data(self, data):
#         self.text.append(data)

# def strip_html(html):
#     stripper = HTMLStripper()# make a new "bucket" to hold the text
#     stripper.feed(html) # run the parser on the HTML
#     return ''.join(stripper.text).strip() # combine the collected text and clean it up

def get_all_images(html_content):
    """
    Find every <img> tag in the post's HTML content and return a list
    of their src URLs (the actual images used, in the order they appear).
    """
    soup = BeautifulSoup(html_content, "html.parser")
    images = [img['src'] for img in soup.find_all('img') if img.get('src')]
    return images

# Loop through media items and get urls for hero images
for media in media_items:
    media_id = media['id']
    media_url = media['source_url']

    # print(f"Media ID: {media_id}, URL: {media_url}")



# # Loop through the posts and save them to Markdown files
# # YAML ausgeben 
for post in posts:
    post_id   = post['id']
    title     = post['title']['rendered']
    date      = post['date'][:10]  # just the YYYY-MM-DD part
    category  = post['categories']  # This is a list of category IDs
    content   = strip_html(post['content']['rendered'])
    description = strip_html(post['excerpt']['rendered'])  # Use the description field
    link      = post['link']
    type      = post['type']
    tags      = post['tags']

    featured_media_id = post['featured_media'] # This is the media ID
    hero = "No image available" # Default value if no featured media is found
    if featured_media_id: # Check if there is a featured media ID
        media = client.media.get(featured_media_id) # Fetch the media item using the ID
        hero = media['source_url'] # Get the URL of the media item
    # Get every image embedded in the post body (in addition to the featured/hero image)
    gallery_images = get_all_images(post['content']['rendered'])
    
    language = post['yoast_head_json'].get('og_locale', None)
    # Fetch author name
    author_id = post['author']
    author    = client.users.get(author_id)
    author_name = author['name']

     # Create a directory for the post in the docs/news folder with id_number

    if 56 in category:
        folder = "docs/events"
    elif all(cat in category for cat in (42, 68)):
        folder = "docs/publications"
    else:
        folder = "docs/news"

    docs_dir = Path(__file__).resolve().parent.parent / folder

    page_dir = docs_dir / f"page_wp_{post_id}"  # Use post ID for unique directory name
    page_dir.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist

    # Create the Markdown content yaml preamble
    page_content = f"""---
title: {title}
author: {author_name}
date: {date}
type: {type}
categories: {category}
tags: {tags}
hero: {hero}
gallery: {gallery_images}
link: {link}
language: {language}
description: {description}
...
---
{content}
"""
    # Save the Markdown file
    (page_dir / "index.md").write_text(page_content, encoding="utf-8")
    print(f"Saved post to {page_dir / 'index.md'}")
