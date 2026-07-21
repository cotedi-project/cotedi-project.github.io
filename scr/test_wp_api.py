from wp_api import WPClient
from html.parser import HTMLParser
from wp_api.auth import ApplicationPasswordAuth
from pathlib import Path
import re
import os
from bs4 import BeautifulSoup
import yaml
from markdownify import markdownify as md # https://pypi.org/project/markdownify/

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


# print all keys
# print(list(posts[0].keys()))

# print all media items
# print(list(media_items[0].keys()))

# Find language in the yoast_head_json field
# print(posts['yoast_head_json'])

# Raw YAML output for debugging
# print("Raw YAML output:")
# for post in posts:
#     print(post)

# Uses BeautifulSoup (bs4) to parse HTML into a navigable tree (DOM-style), 
# Find every <img> tag in the post's HTML content and return a list of their src URLs (the actual images used, in the order they appear).
# https://beautiful-soup-4.readthedocs.io/en/latest/

def get_all_images(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    images = [img['src'] for img in soup.find_all('img') if img.get('src')]
    return images

# Use markdownify instead
# def strip_html(html):
#     return BeautifulSoup(html, "html.parser").get_text().strip() # get_text() extracts all the text from the HTML, and strip() removes leading/trailing whitespace.

# Use markdownify to convert HTML to Markdown format
def html_to_markdown(html):
    return md(html, heading_style="ATX").strip() # heading_style="ATX" controls how HTML headings get converted uses #

# Load category_rules.yaml to map category IDs to names
with open("category_rules.yaml") as f:
    config = yaml.safe_load(f)
category_rules = config["category_rules"]

def resolve_folder(category, rules):
    """
    Given a post's category ID list and the loaded rule set,
    return the matching output folder, or None if no rule matches.
    """
    for rule in rules:
        cats = rule["category"]
        if rule["match"] == "all":
            if all(cat in category for cat in cats):
                return rule["folder"]
        else:  # "any"
            if any(cat in category for cat in cats):
                return rule["folder"]
    return None

# # Loop through the posts and save them to Markdown files
# # YAML ausgeben 
for post in posts:
    post_id   = post['id']
    title     = post['title']['rendered']
    date      = post['date'][:10]  # just the YYYY-MM-DD part
    category  = post['categories']  # This is a list of category IDs
    content   = html_to_markdown(post['content']['rendered'])
    description = html_to_markdown(post['excerpt']['rendered'])  # Use the description field
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

    # Collect all the data into a dictionary for easier handling
    post_data = {
        "id": post_id,
        "title": title,
        "date": date,
        "category": category,
        "description": description,
        "link": link,
        "type": type,
        "tags": tags,
        "hero": hero,
        "gallery_images": gallery_images,
        "language": language,
        "author_name": author_name,
    }

    # Render YAML block from dictionary
    yaml_block = yaml.safe_dump(
        post_data,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
        )


     

    folder = resolve_folder(category, category_rules)

    if folder is None:
        print(f"Warning: Post {post_id} has an unrecognized category {category}.")
        continue
              

    docs_dir = Path(__file__).resolve().parent.parent / folder

    page_dir = docs_dir / f"page_wp_{post_id}"  # Use post ID for unique directory name
    page_dir.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist

    # Create the Markdown content yaml preamble
    # Dictionary erstellen auf den post 
    # YAML Renderer verwendne gebe Dictionary zu erstellen
    page_content = f"---\n{yaml_block}---\n{content}\n"

    # Save the Markdown file
    (page_dir / "index.md").write_text(page_content, encoding="utf-8")
    print(f"Saved post to {page_dir / 'index.md'}")
