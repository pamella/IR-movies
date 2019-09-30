#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup


url = 'https://www.metacritic.com/movie/iron-man'
r = requests.get(url)
print(f'Status code: {r.status_code}\n')
soup = BeautifulSoup(r.text, 'html.parser')

title = soup.find('h1').text
print(f'Title: {title}\n')

year = soup.find('span', {'class': ['release_year', 'lighter']}).text
print(f'Year: {year}\n')

runtime = soup.find('div', {'class': 'runtime'}).contents[1].text
print(f'Runtime: {runtime}\n')
