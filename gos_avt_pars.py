from bs4 import BeautifulSoup
import requests


def parse():
    URL = 'https://xn--90adear.xn--p1ai/r/65/'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    }

    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_='sl-item-title')
    news = []

    for item in items:
        news.append({
            'title': item.find('a', class_='news-popup e-popup').get_text(strip=True),
            'text': item.find('div', class_='sl-item-text').get_text(strip=True),
            'link': item.find('a', class_='news-popup e-popup').get('href')
        })
        for now in news:
            print(
                f'{now["title"]} -> Text: {now["text"]} -> link: {now["link"]}')


parse()
