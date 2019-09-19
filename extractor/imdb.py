#!/usr/bin/python3
import json
import requests

from bs4 import BeautifulSoup
from time import sleep

url = 'https://www.imdb.com/title/tt0816692'
r = requests.get(url)
print(f'Status code: {r.status_code}\n')
soup = BeautifulSoup(r.text, 'html.parser')

title = soup.find('h1').contents[0][:-1]
print(f'Title: {title}\n')

year = soup.find('h1').find('span', id='titleYear').find('a').text
print(f'Year: {year}\n')

runtime = soup.find('div', {'class': 'subtext'}).contents[3].text
runtime = ' '.join(runtime.split())
print(f'Runtime: {runtime}\n')

genres_raw =  soup.find('div', {'class': 'subtext'}).find_all('a')[:-1]
genres = []
for genre in genres_raw:
    genres.append(genre.text);
print(f'Genres: {genres}\n')

director = soup.find('div', {'class': 'credit_summary_item'}).contents[3].text
print(f'Director: {director}\n')
