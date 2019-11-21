import requests
from bs4 import BeautifulSoup


def rottentomatoes_extractor(url):
    movie = {}
    movie['url'] = url

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    meta_values = soup.find_all('div', {'class': 'meta-value'})

    title = soup.find('h1').contents[0].lower()
    movie['title'] = ' '.join(title.split()).strip()

    runtime = meta_values[len(meta_values)-2].text
    runtime = ' '.join(runtime.split())
    runtime = runtime.split(' ')
    movie['runtime'] = runtime[0].strip()

    year = meta_values[len(meta_values)-3].text
    year = ' '.join(year.split())
    year = year.split(',')
    movie['year'] = year[len(year) -1].strip()

    genres = meta_values[1].text.lower()
    genres = ' '.join(genres.split())
    genres = [genre.strip() for genre in genres.split(',')]
    movie['genres'] = []
    for genre in genres:
        if '&' in genre:
            multiple_genres = genre.split('&')
            for g in multiple_genres:
                movie['genres'].append(g.strip())
        else:
            movie['genres'].append(genre)

    return movie
