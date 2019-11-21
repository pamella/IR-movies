import requests
from bs4 import BeautifulSoup


class RottenTomatoesMovie:
    def __init__(self, url, title='', year='', runtime='', genres=[]):
        self.url = url

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        meta_values = soup.find_all('div', {'class': 'meta-value'})

        title = soup.find('h1').contents[0].lower()
        self.title = ' '.join(title.split()).strip()

        runtime = meta_values[len(meta_values)-2].text
        runtime = ' '.join(runtime.split())
        runtime = runtime.split(' ')
        self.runtime = runtime[0].strip()

        year = meta_values[4].text
        year = ' '.join(year.split())
        year = year.split(' ')
        if len(year) >= 4 :
            self.year = year[len(year) - 2].strip()
        else:
            self.year = year[len(year) - 1].strip()

        genres = meta_values[1].text.lower()
        genres = ' '.join(genres.split())
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
    # "https://www.rottentomatoes.com/m/the_perks_of_being_a_wallflower",
    # "https://www.rottentomatoes.com/m/breakfast_club",
    # "https://www.rottentomatoes.com/m/harry_potter_and_the_sorcerers_stone",
    # "https://www.rottentomatoes.com/m/harry_potter_and_the_chamber_of_secrets",
    # "https://www.rottentomatoes.com/m/1221547_alice_in_wonderland",
    # "https://www.rottentomatoes.com/m/iron_man",
    # "https://www.rottentomatoes.com/m/the_imitation_game",
    # "https://www.rottentomatoes.com/m/the_girl_with_the_dragon_tattoo_2009",
    # "https://www.rottentomatoes.com/m/avatar",
    # "https://www.rottentomatoes.com/m/shining",
    # "https://www.rottentomatoes.com/m/the_devil_wears_prada",
    "https://www.rottentomatoes.com/m/hustlers_2019",
    "https://www.rottentomatoes.com/m/1221547_alice_in_wonderland",
    "https://www.rottentomatoes.com/m/spider_man_far_from_home",
    "https://www.rottentomatoes.com/m/singin_in_the_rain",
    "https://www.rottentomatoes.com/m/1073037_hunchback_of_notre_dame",
    "https://www.rottentomatoes.com/m/aquarius",
    "https://www.rottentomatoes.com/m/the_girl_with_the_dragon_tattoo_2009",
    "https://www.rottentomatoes.com/m/breakfast_club",
    "https://www.rottentomatoes.com/m/the_imitation_game",
    "https://www.rottentomatoes.com/m/barbie_as_the_princess_and_the_pauper",
]

ROTTENTOMATOES_MOVIES = []

for movie_link in rottentomatoes_movies_links:
    ROTTENTOMATOES_MOVIES.append(RottenTomatoesMovie(url=movie_link))
