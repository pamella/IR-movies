from _scripts.genres import create_genres
from _scripts.movies import create_movies
from movies.models import Genre, Movie


# Delete all
Genre.objects.all().delete()
Movie.objects.all().delete()

# Create
create_genres()
create_movies()
