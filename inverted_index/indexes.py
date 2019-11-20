import json

import data
import utils


with open('classifier/train_sets/X_train.json') as f:
    docs_tokens = json.load(f)

MOVIES = data.ROTTENTOMATOES_MOVIES

INVERTED_INDEX_UNCOMPRESSED = {'title': {}, 'year': {}, 'genre': {}}
INVERTED_INDEX_COMPRESSED = {'title': {}, 'year': {}, 'genre': {}}

def generate_inverted_index():
    for movie in MOVIES:
        # TITLE
        movie_title_words = movie.title.split(' ')
        for movie_title_word in movie_title_words:
            if movie_title_word not in INVERTED_INDEX_UNCOMPRESSED['title'].keys():
                INVERTED_INDEX_UNCOMPRESSED['title'][movie_title_word] = {}
                INVERTED_INDEX_COMPRESSED['title'][movie_title_word] = []
        # YEAR
        if movie.year:
            INVERTED_INDEX_UNCOMPRESSED['year'][movie.year] = {}
            INVERTED_INDEX_COMPRESSED['year'][movie.year] = []
        # GENRES
        for genre in movie.genres:
            if genre not in INVERTED_INDEX_UNCOMPRESSED['genre'].keys():
                INVERTED_INDEX_UNCOMPRESSED['genre'][genre] = {}
                INVERTED_INDEX_COMPRESSED['genre'][genre] = []

    # UNCOMPRESSED
    for doc_id, doc_tokens in enumerate(docs_tokens):
        for token in doc_tokens:
            for key in INVERTED_INDEX_UNCOMPRESSED.keys():
                if token in INVERTED_INDEX_UNCOMPRESSED[key]:
                    if str(doc_id) not in INVERTED_INDEX_UNCOMPRESSED[key][token].keys():
                        INVERTED_INDEX_UNCOMPRESSED[key][token][str(doc_id)] = 1
                    else:
                        INVERTED_INDEX_UNCOMPRESSED[key][token][str(doc_id)] += 1

    # COMPRESSED
    for doc_id, doc_tokens in enumerate(docs_tokens):
        for token in doc_tokens:
            for key in INVERTED_INDEX_UNCOMPRESSED.keys():
                if token in INVERTED_INDEX_COMPRESSED[key]:
                    if not INVERTED_INDEX_COMPRESSED[key][token]:
                        INVERTED_INDEX_COMPRESSED[key][token].append([doc_id])
                        INVERTED_INDEX_COMPRESSED[key][token].append([1])
                    else:
                        aux = len(INVERTED_INDEX_COMPRESSED[key][token][0])
                        first_doc = INVERTED_INDEX_COMPRESSED[key][token][0][0]
                        diff_interval = doc_id - first_doc
                        if diff_interval == 0 or diff_interval == INVERTED_INDEX_COMPRESSED[key][token][0][aux-1]:
                            INVERTED_INDEX_COMPRESSED[key][token][1][aux-1] += 1
                        else:
                            INVERTED_INDEX_COMPRESSED[key][token][0].append(diff_interval)
                            INVERTED_INDEX_COMPRESSED[key][token][1].append(1)

def save_inverted_indexes():
    with open('inverted_index/data/INVERTED_INDEX_UNCOMPRESSED.json', 'w') as f:
        json.dump(INVERTED_INDEX_UNCOMPRESSED, f)

    with open('inverted_index/data/INVERTED_INDEX_COMPRESSED.json', 'w') as f:
        json.dump(INVERTED_INDEX_COMPRESSED, f)

generate_inverted_index()
# print(INVERTED_INDEX_UNCOMPRESSED)
print (f"Size of INVERTED_INDEX_UNCOMPRESSED object in bytes: {utils.get_size(INVERTED_INDEX_UNCOMPRESSED)}")
# print(INVERTED_INDEX_COMPRESSED)
print (f"Size of INVERTED_INDEX_COMPRESSED object in bytes: {utils.get_size(INVERTED_INDEX_COMPRESSED)}")
print(f"Compressed inverted index takes {utils.get_size(INVERTED_INDEX_COMPRESSED) * 100/utils.get_size(INVERTED_INDEX_UNCOMPRESSED)}% less space.")

save_inverted_indexes()
