import requests
from bs4 import BeautifulSoup


class RottenTomatoesMovie:
    def __init__(self, url, title='', year='', runtime=''):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        meta_values = soup.find_all('div', {'class': 'meta-value'})
        self.url = url
        title = soup.find('h1').contents[0][:-1].lower()
        self.title = ' '.join(title.split())
        year = soup.find('span', {'class':'year'}).text
        self.year = ' '.join(year.split())
        runtime = meta_values[len(meta_values)-2].text
        self.runtime = ' '.join(runtime.split())
