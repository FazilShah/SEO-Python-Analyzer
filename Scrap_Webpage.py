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
        try:
            title = text.find('title')
            return str(title.string)
        except:
            return None


    @staticmethod
    def get_meta_description():
        text = scrape.page
        for tag in text.find_all('meta'):
            if tag.get('name', None) == 'description':
                return tag.get('content', None)

    @staticmethod
    def get_h1_tags():
        text = scrape.page
        h1 = text.find_all('h1')
        h1s = [item.text for item in h1]
        return h1s

    @staticmethod
    def get_canonical():
        text = scrape.page
        can = text.find('link', rel='canonical')
        try:
            return can['href']
        except:
            return None

    @staticmethod
    def get_viewports():
        text = scrape.page
        for tag in text.find_all(attrs={"name":"viewport"}):
            if tag.get('name') == 'viewport':
                return True
            else:
                return False









