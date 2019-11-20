import requests
from bs4 import BeautifulSoup


class RottenTomatoesMovie:
    def __init__(self, url, title='', year='', runtime='', genres=[]):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        meta_values = soup.find_all('div', {'class': 'meta-value'})
        self.url = url
        title = soup.find('h1').contents[0].lower()
        self.title = ' '.join(title.split())
        runtime = meta_values[len(meta_values)-2].text
        self.runtime = ' '.join(runtime.split())
        if soup.find('span', {'class':'year'}):
            year = soup.find('span', {'class':'year'}).text
            self.year = ' '.join(year.split())
        else:
            self.year = year
        genres = meta_values[1].text.lower()
        genres = ' '.join(genres.split())
        # import ipdb ; ipdb.set_trace()
        genres = [genre.strip() for genre in genres.split(',')]
        self.genres = []
        for genre in genres:
            if '&' in genre:
                multiple_genres = genre.split('&')
                for g in multiple_genres:
                    self.genres.append(g.strip())
            else:
                self.genres.append(genre)


rottentomatoes_movies_links = [
    "https://www.rottentomatoes.com/m/the_perks_of_being_a_wallflower",
    "https://www.rottentomatoes.com/m/breakfast_club",
    "https://www.rottentomatoes.com/m/harry_potter_and_the_sorcerers_stone",
    "https://www.rottentomatoes.com/m/harry_potter_and_the_chamber_of_secrets",
    "https://www.rottentomatoes.com/m/1221547_alice_in_wonderland",
    "https://www.rottentomatoes.com/m/iron_man",
    "https://www.rottentomatoes.com/m/the_imitation_game",
    "https://www.rottentomatoes.com/m/the_girl_with_the_dragon_tattoo_2009",
    "https://www.rottentomatoes.com/m/avatar",
    "https://www.rottentomatoes.com/m/shining",
    "https://www.rottentomatoes.com/m/the_devil_wears_prada",
]

ROTTENTOMATOES_MOVIES = []

for movie_link in rottentomatoes_movies_links:
    ROTTENTOMATOES_MOVIES.append(RottenTomatoesMovie(url=movie_link))
