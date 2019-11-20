import json

import data
import utils


with open('classifier/train_sets/X_train.json') as f:
    docs_tokens = json.load(f)

rt0 = data.RottenTomatoesMovie(url='https://www.rottentomatoes.com/m/the_perks_of_being_a_wallflower')
rt1 = data.RottenTomatoesMovie(url='https://www.rottentomatoes.com/m/breakfast_club')
rt2 = data.RottenTomatoesMovie(url='https://www.rottentomatoes.com/m/harry_potter_and_the_sorcerers_stone')
rt3 = data.RottenTomatoesMovie(url='https://www.rottentomatoes.com/m/harry_potter_and_the_chamber_of_secrets')

MOVIES = [rt0, rt1, rt2, rt3]

INVERTED_INDEX_UNCOMPRESSED = {'title': {}}
INVERTED_INDEX_COMPRESSED = {'title': {}}

for movie in MOVIES:
    # TITLE
    movie_title_words = movie.title.split(' ')
    for movie_title_word in movie_title_words:
        if movie_title_word not in INVERTED_INDEX_UNCOMPRESSED['title'].keys():
            INVERTED_INDEX_UNCOMPRESSED['title'][movie_title_word] = []
            INVERTED_INDEX_COMPRESSED['title'][movie_title_word] = []

for doc_id, doc_tokens in enumerate(docs_tokens):
    for token in doc_tokens:
        freq = 0
        if token in INVERTED_INDEX_UNCOMPRESSED['title']:
            freq = freq + 1
            INVERTED_INDEX_UNCOMPRESSED['title'][token].append([doc_id, freq])

# print(INVERTED_INDEX_UNCOMPRESSED)
print (f"Size of INVERTED_INDEX_UNCOMPRESSED object in bytes: {utils.get_size(INVERTED_INDEX_UNCOMPRESSED)}")

for doc_id, doc_tokens in enumerate(docs_tokens):
    for token in doc_tokens:
        if token in INVERTED_INDEX_COMPRESSED['title']:
            if len(INVERTED_INDEX_COMPRESSED['title'][token]) == 0:
                INVERTED_INDEX_COMPRESSED['title'][token].append(doc_id)
            else:
                first_doc = INVERTED_INDEX_COMPRESSED['title'][token][0]
                INVERTED_INDEX_COMPRESSED['title'][token].append(doc_id - first_doc)

# print(INVERTED_INDEX_COMPRESSED)
print (f"Size of INVERTED_INDEX_COMPRESSED object in bytes: {utils.get_size(INVERTED_INDEX_COMPRESSED)}")
