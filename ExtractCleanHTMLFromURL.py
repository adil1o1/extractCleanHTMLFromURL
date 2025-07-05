import requests
from bs4 import BeautifulSoup
import pyperclip

def extract_clean_html(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch: {url}")

    soup = BeautifulSoup(response.text, 'html.parser')

    # Removing Everything from Header and Footer Tags
    for tag in soup.find_all(['header', 'footer']):
        tag.decompose()

    # <body>
    body = soup.find('body')
    if not body:
        raise Exception("Body tag not found.")

    # Cleanup all HTML Tags Except the one mentioned below
    allowed_tags = ['a', 'br', 'p', 'ul', 'ol', 'li', 'b', 'strong', 'i', 'em', 'u']
    for tag in body.find_all(True):
        if tag.name not in allowed_tags:
            tag.unwrap()
        else:
            if tag.name == 'a':
                tag.attrs = {k: v for k, v in tag.attrs.items() if k == 'href'}
            else:
                tag.attrs = {}

    html_code = body.decode_contents()

    # Once All Done, A File is Created with clean HTML content.
    with open("simpleHTMLText.html", "w", encoding="utf-8") as f:
        f.write(html_code)

    pyperclip.copy(html_code)
    print(" Clean HTML saved to 'simpleHTMLText.html' and copied to clipboard!")

# Example usage
url = "https://example.com/post-name"
extract_clean_html(url)
