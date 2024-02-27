import requests
from bs4 import BeautifulSoup


def fetch_webpage_content(url):
    response = requests.get(url)
    if response.ok:
        return response.text
    else:
        response.raise_for_status()


def extract_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs = soup.find_all('p')
    print(' '.join(p.text for p in paragraphs))
    return ' '.join(p.text for p in paragraphs)
