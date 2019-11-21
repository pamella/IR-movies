import json
from movies.models import Genre


with open('inverted_index/data/INVERTED_INDEX_UNCOMPRESSED.json') as f:
    inverted_index = json.load(f)
    f.close()


def get_most_common_genres(dict):
    genres = []
    for key in dict['genre'].keys():
        genres.append(key)
    return genres


def create_genres():
    most_common_genres = get_most_common_genres(inverted_index)
    for genre in most_common_genres:
        Genre.objects.get_or_create(name=genre)
