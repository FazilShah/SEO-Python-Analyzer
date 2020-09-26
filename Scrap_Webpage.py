from bs4 import BeautifulSoup
import requests


class scrape:

    def __init__(self, url):
        scrape.url = url
        scrape.response = requests.get(scrape.url, allow_redirects=False)
        scrape.page = BeautifulSoup(scrape.response.text, 'html.parser')

    @staticmethod
    def get_title():
        text = scrape.page
        title = text.title

        return str(title)

    @staticmethod
    def get_meta_description():
        text = scrape.page
        for tag in text.find_all('meta'):
            if tag.get('name', None) == 'description':
                return tag.get('content', None)

    @staticmethod
    def get_h1_tags():
        text = scrape.page
        h1 = text.h1.text
        return str(h1)
