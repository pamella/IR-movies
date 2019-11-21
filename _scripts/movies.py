from _scripts.movies_links import rottentomatoes_links
from movies.models import Genre, Movie
from movies.utils.rottentomatoes_extractor import rottentomatoes_extractor


def create_movies():
    for link in rottentomatoes_links:
        if link[1] == True:
            movie = rottentomatoes_extractor(link[0])
            movieObj = Movie.objects.create(
                title=movie['title'],
                url=movie['url'],
                runtime=movie['runtime'],
                year=movie['year'],
            )
            for genre in movie['genres']:
                genreObj = Genre.objects.get(name=genre)
                movieObj.genres.add(genreObj)
