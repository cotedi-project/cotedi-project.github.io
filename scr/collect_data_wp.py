from wp_api import WPClient
from html.parser import HTMLParser
from wp_api.auth import ApplicationPasswordAuth
from wp_api.exceptions import WPAPIBadRequestError
from pathlib import Path
from urllib.parse import urlparse
import os
import requests
from bs4 import BeautifulSoup
import yaml
from markdownify import markdownify as md # https://pypi.org/project/markdownify/


def download_image(url, dest_dir):
    """
    Download an image from `url` and save it into `dest_dir`, using the
    filename from the URL itself.

    Returns the saved filename on success, or None if the download failed
    (e.g. bad status code or a network/timeout error) - the caller can then
    decide to fall back to the remote URL instead.
    """
    if not url:
        return None

    try:
        response = requests.get(url, timeout=20)
    except requests.RequestException as e:
        print(f"  [image] FAILED to fetch {url}: {e}")
        return None

    if response.status_code != 200:
        print(f"  [image] FAILED ({response.status_code}) fetching {url}")
        return None

    filename = os.path.basename(urlparse(url).path)
    dest_dir.mkdir(parents=True, exist_ok=True)
    filepath = dest_dir / filename

    with open(filepath, "wb") as f:
        f.write(response.content)

    print(f"  [image] saved {filepath}")
    return filename


def download_and_localize_images(html_content, dest_dir, url_prefix):
    """
    Parse `html_content`, download every <img> found, and rewrite that
    image's `src` attribute to an absolute, site-rooted path
    (f"{url_prefix}/{filename}"). This must be absolute (not a bare
    filename) because body content gets re-embedded verbatim on other
    pages (e.g. publications.njk embeds full post.content into the
    publications listing page) - a bare filename would only resolve
    correctly on the post's own detail page.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    image_refs = []

    for img in soup.find_all("img"):
        src = img.get("src")
        if not src:
            continue

        local_name = download_image(src, dest_dir)
        if local_name:
            local_ref = f"{url_prefix}/{local_name}"
            img["src"] = local_ref
            image_refs.append(local_ref)
        else:
            image_refs.append(src)

    return str(soup), image_refs


# Uses BeautifulSoup (bs4) to parse HTML into a navigable tree (DOM-style), 
# Find every <img> tag in the post's HTML content and return a list of their src URLs (the actual images used, in the order they appear).
# https://beautiful-soup-4.readthedocs.io/en/latest/

def get_all_images(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    images = [img['src'] for img in soup.find_all('img') if img.get('src')]
    return images

# Use markdownify to convert HTML to Markdown format
def html_to_markdown(html):
    return md(html, heading_style="ATX").strip() # heading_style="ATX" controls how HTML headings get converted uses #

def resolve_folder(category, rules):
    """
    Given a post's category ID list and the loaded rule set,
    return the matching output folder, or None if no rule matches.
    """
    for rule in rules:
        cats = rule["category"]
        if rule["match"] == "all":
            if all(cat in category for cat in cats):
                return rule["folder"], rule.get("tags", [])
        else:  # "any"
            if any(cat in category for cat in cats):
                return rule["folder"], rule.get("tags", [])
    return None, None

def fetch_all_posts(client):
    """Fetch every published post across all pages, not just the first one."""
    all_posts = []
    page = 1
    while True:
        try:
            batch = client.posts.list(status="publish", per_page=100, page=page, orderby="date")
        except WPAPIBadRequestError:
            # WordPress returns a 400 error (not an empty list) once you go past the last page
            break
        if not batch:
            break
        all_posts.extend(batch)
        page += 1
    return all_posts

def get_existing_post_ids(docs_root):
    """
    Scan all output folders under docs_root for existing page_wp_{id} folders
    and return the set of post IDs already saved.
    """
    existing_ids = set()
    for folder in docs_root.glob("**/page_wp_*"):
        if folder.is_dir():
            try:
                post_id = int(folder.name.replace("page_wp_", ""))
                existing_ids.add(post_id)
            except ValueError:
                continue  # skip anything that doesn't match the expected naming pattern
    return existing_ids



# Main function to fetch posts, process them, and save as Markdown files with YAML front matter
def main():
    # https://stackoverflow.com/questions/76390320/how-do-i-include-github-secrets-in-a-python-script
    # Include GitHub secrets in a Python script by reading them from environment variables.
    username = os.environ.get("WP_USERNAME")
    password = os.environ.get("WP_PASSWORD")

    # Authenticate with WordPress using application password
    auth = ApplicationPasswordAuth(username=username, app_password=password)
    client = WPClient(base_url="https://imaginatic.es", auth=auth)

    # Load path to category_rule.yaml from environment variable
    config_path = os.environ.get("CATEGORY_RULE") # Read from environment variable

    with open(config_path) as f: # Open the YAML file and load its contents into a Python dictionary
        config = yaml.safe_load(f)

    category_rules = config["category_rules"] # Pull the list of category rules from the loaded configuration

    # --- Block 1: scan what's already saved locally ---
    docs_root = Path(__file__).resolve().parent.parent / "docs"
    print("Scanning:", docs_root, "| exists:", docs_root.exists())

    existing_ids = get_existing_post_ids(docs_root)
    print(f"Found {len(existing_ids)} posts already saved locally.")
    print("IDs found:", sorted(existing_ids))

    # --- Block 2: fetch everything from WordPress ---
    posts = fetch_all_posts(client)
    print(f"Fetched {len(posts)} published posts from WordPress.")
    
    
    for post in posts:
        post_id   = post['id']
        if post_id == 1464:
            continue  # Skip post with ID 1464
        if post_id in existing_ids:
            continue  # Skip posts that are already saved locally
        title     = post['title']['rendered']
        date      = post['date'][:10]  # just the YYYY-MM-DD part
        category  = post['categories']  # This is a list of category IDs
        description = html_to_markdown(post['excerpt']['rendered'])  # Use the description field
        link      = post['link']
        type      = post['type']
        

        featured_media_id = post['featured_media'] # This is the media ID
        hero_url = None
        if featured_media_id: # Check if there is a featured media ID
            media = client.media.get(featured_media_id) # Fetch the media item using the ID
            hero_url = media['source_url'] # Get the URL of the media item

        language = post['yoast_head_json'].get('og_locale', None)
        # Fetch author name
        author_id = post['author']
        author    = client.users.get(author_id)
        author_name = author['name']

        # Determine the output folder based on the post's category and the loaded rules
        folder, site_tags = resolve_folder(category, category_rules)

        if folder is None:
            print(f"Warning: Post {post_id} has an unrecognized category {category}.")
            continue

        # Create the output directory based on the resolved folder and the post ID
        docs_dir = Path(__file__).resolve().parent.parent / folder

        page_dir = docs_dir / f"page_wp_{post_id}"  # Use post ID for unique directory name
        page_dir.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist

        image_url_prefix = "/" + page_dir.relative_to(docs_root).as_posix()

        # Saved directly in page_dir, alongside index.md (no subfolder).
        # Hero and gallery images are referenced by BARE FILENAME in the
        # markdown/front matter — not a path. Eleventy's post.njk detail
        # page uses the filename as-is (resolves relative to the post's own
        # folder), and listing templates like news.njk/materials.njk prepend
        # post.url themselves before the filename. Baking the folder path in
        # here would double up with that prepend on listing pages.
        hero = "No image available"
        if hero_url:
            local_name = download_image(hero_url, page_dir)
            hero = local_name if local_name else hero_url

        # --- Download every image embedded in the post body and rewrite its
        # src attribute directly in the HTML (before markdown conversion),
        # so the markdown ends up with the correct local reference
        # unconditionally - no string-matching against markdownify's output
        # required.
        localized_html, gallery_images = download_and_localize_images(
            post['content']['rendered'], page_dir, image_url_prefix
        )
        content = html_to_markdown(localized_html)

        # Collect all the data into a dictionary for easier handling
        post_data = {
            "title": title,
            "author_name": author_name,
            "date": date,
            "tags": site_tags,
            "type": type,
            "hero": hero,
            "link": link,
            "language": language,
            "category": category,
            "description": description,
            "gallery_images": gallery_images,
        }

        # Render YAML block from dictionary
        yaml_block = yaml.safe_dump(
            post_data,
            sort_keys=False, # Do not sort keys alphabetically, keep the original order
            allow_unicode=True, # Allow Unicode characters in the output
            default_flow_style=False, # Block style throughout
            )

        # Create the Markdown content with rendered YAML front matter and the post content
        page_content = f"---\n{yaml_block}---\n{content}\n"

        # Save the Markdown file
        (page_dir / "index.md").write_text(page_content, encoding="utf-8")
        print(f"Saved post to {page_dir / 'index.md'}")

if __name__ == "__main__":
    main()