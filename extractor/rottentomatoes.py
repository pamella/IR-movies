#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup


url = 'https://www.rottentomatoes.com/m/the_perks_of_being_a_wallflower'
r = requests.get(url)
# print(f'Status code: {r.status_code}\n')
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

title = soup.find('h1', {'class':'title'}).text
title = ' '.join(title.split())
print(f'Title: {title}\n')

year = soup.find('span', {'class':'year'}).text
year = ' '.join(year.split())
print(f'Year: {year}\n')

meta_values = soup.find_all('div', {'class': 'meta-value'})

genres =  meta_values[1].text
genres = ' '.join(genres.split())
genres = genres.split(',')
print(f'Genres: {genres}\n')

director = meta_values[2].text
director = ' '.join(director.split())
print(f'Director: {director}\n')

runtime = meta_values[len(meta_values)-2].text
runtime = ' '.join(runtime.split())
print(f'Runtime: {runtime}\n')

studio = meta_values[len(meta_values)-1].text
studio = ' '.join(studio.split())
print(f'Studio: {studio}\n')
