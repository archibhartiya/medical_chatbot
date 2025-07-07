import requests
from bs4 import BeautifulSoup

def fetch_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find_all(['p'])
    return "\n".join(p.text for p in content)

def save_articles():
    urls = [
        "https://www.mayoclinic.org/diseases-conditions/coronavirus/symptoms-causes/syc-20479963",
        "https://medlineplus.gov/flu.html"
    ]
    for i, url in enumerate(urls):
        content = fetch_article(url)
        with open(f'articles_{i}.txt', 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == "__main__":
    save_articles()
