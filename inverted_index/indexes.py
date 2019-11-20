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
            INVERTED_INDEX_UNCOMPRESSED['title'][movie_title_word] = {}
            INVERTED_INDEX_COMPRESSED['title'][movie_title_word] = []

for doc_id, doc_tokens in enumerate(docs_tokens):
    for token in doc_tokens:
        if token in INVERTED_INDEX_UNCOMPRESSED['title']:
            if str(doc_id) not in INVERTED_INDEX_UNCOMPRESSED['title'][token].keys():
                INVERTED_INDEX_UNCOMPRESSED['title'][token][str(doc_id)] = 1
            else:
                INVERTED_INDEX_UNCOMPRESSED['title'][token][str(doc_id)] += 1

# print(INVERTED_INDEX_UNCOMPRESSED)
print (f"Size of INVERTED_INDEX_UNCOMPRESSED object in bytes: {utils.get_size(INVERTED_INDEX_UNCOMPRESSED)}")

for doc_id, doc_tokens in enumerate(docs_tokens):
    for token in doc_tokens:
        if token in INVERTED_INDEX_COMPRESSED['title']:
            if not INVERTED_INDEX_COMPRESSED['title'][token]:
                INVERTED_INDEX_COMPRESSED['title'][token].append([doc_id])
                INVERTED_INDEX_COMPRESSED['title'][token].append([1])
            else:
                aux = len(INVERTED_INDEX_COMPRESSED['title'][token][0])
                first_doc = INVERTED_INDEX_COMPRESSED['title'][token][0][0]
                diff_interval = doc_id - first_doc
                if diff_interval == 0 or diff_interval == INVERTED_INDEX_COMPRESSED['title'][token][0][aux-1]:
                    INVERTED_INDEX_COMPRESSED['title'][token][1][aux-1] += 1
                else:
                    INVERTED_INDEX_COMPRESSED['title'][token][0].append(diff_interval)
                    INVERTED_INDEX_COMPRESSED['title'][token][1].append(1)

# print(INVERTED_INDEX_COMPRESSED)
print (f"Size of INVERTED_INDEX_COMPRESSED object in bytes: {utils.get_size(INVERTED_INDEX_COMPRESSED)}")
