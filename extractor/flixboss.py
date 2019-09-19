#!/usr/bin/python3
import json
import requests

from bs4 import BeautifulSoup
from time import sleep

url = 'https://flixboss.com/movie/a-i-artificial-intelligence-60020748'
r = requests.get(url)
print(f'Status code: {r.status_code}\n')
soup = BeautifulSoup(r.text, 'html.parser')

title = soup.find('h1').text
print(f'Title: {title}\n')

year = soup.find('ul', {'class': 'sub-title'}).find('li').text
print(f'Year: {year}\n')

genres_raw = soup.find('ul', {'class': 'sub-title'}).find_all('li', {'class': 'genre'})
genres = []
for genre in genres_raw:
    genres.append(genre.text)
print(f'Genres: {genres}\n')


meta_additional = soup.find_all('div', {'class': 'additional'})

runtime = meta_additional[0].find_all('span')[1].text
print(f'Runtime: {runtime}\n')

director = meta_additional[2].find('a').text
print(f'Director: {director}\n')
