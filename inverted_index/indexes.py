import json

import RottenTomatoesMovie
import utils


with open('inverted_index/data/html_docs_tokens_all.json') as f:
    docs_tokens = json.load(f)
    f.close()

MOVIES = RottenTomatoesMovie.ROTTENTOMATOES_MOVIES

INVERTED_INDEX_UNCOMPRESSED = {'title': {}, 'year': {}, 'genre': {}}
INVERTED_INDEX_UNCOMPRESSED_NO_FREQ = {'title': {}, 'year': {}, 'genre': {}}
INVERTED_INDEX_COMPRESSED = {'title': {}, 'year': {}, 'genre': {}}
INVERTED_INDEX_COMPRESSED_NO_FREQ = {'title': {}, 'year': {}, 'genre': {}}

def generate_inverted_index():
    for movie in MOVIES:
        # TITLE
        movie_title_words = movie.title.split(' ')
        for movie_title_word in movie_title_words:
            if movie_title_word not in INVERTED_INDEX_UNCOMPRESSED['title'].keys():
                INVERTED_INDEX_UNCOMPRESSED['title'][movie_title_word] = {}
                INVERTED_INDEX_UNCOMPRESSED_NO_FREQ['title'][movie_title_word] = {}
                INVERTED_INDEX_COMPRESSED['title'][movie_title_word] = []
                INVERTED_INDEX_COMPRESSED_NO_FREQ['title'][movie_title_word] = []
        # YEAR
        if movie.year:
            INVERTED_INDEX_UNCOMPRESSED['year'][movie.year] = {}
            INVERTED_INDEX_UNCOMPRESSED_NO_FREQ['year'][movie.year] = {}
            INVERTED_INDEX_COMPRESSED['year'][movie.year] = []
            INVERTED_INDEX_COMPRESSED_NO_FREQ['year'][movie.year] = []
        # GENRES
        for genre in movie.genres:
            if genre not in INVERTED_INDEX_UNCOMPRESSED['genre'].keys():
                INVERTED_INDEX_UNCOMPRESSED['genre'][genre] = {}
                INVERTED_INDEX_UNCOMPRESSED_NO_FREQ['genre'][genre] = {}
                INVERTED_INDEX_COMPRESSED['genre'][genre] = []
                INVERTED_INDEX_COMPRESSED_NO_FREQ['genre'][genre] = []

    # UNCOMPRESSED
    for doc_tokens in docs_tokens.items():
        doc_id = doc_tokens[0]
        for token in doc_tokens[1][2]:
            for key in INVERTED_INDEX_UNCOMPRESSED.keys():
                if token in INVERTED_INDEX_UNCOMPRESSED[key]:
                    if str(doc_id) not in INVERTED_INDEX_UNCOMPRESSED[key][token].keys():
                        INVERTED_INDEX_UNCOMPRESSED[key][token][str(doc_id)] = 1
                    else:
                        INVERTED_INDEX_UNCOMPRESSED[key][token][str(doc_id)] += 1
    print("Processed inverted index uncompressed.")

    # COMPRESSED
    for doc_tokens in docs_tokens.items():
        doc_id = doc_tokens[0]
        for token in doc_tokens[1][2]:
            for key in INVERTED_INDEX_UNCOMPRESSED.keys():
                if token in INVERTED_INDEX_COMPRESSED[key]:
                    if not INVERTED_INDEX_COMPRESSED[key][token]:
                        INVERTED_INDEX_COMPRESSED[key][token].append([doc_id])
                        INVERTED_INDEX_COMPRESSED[key][token].append([1])
                    else:
                        aux = len(INVERTED_INDEX_COMPRESSED[key][token][0])
                        first_doc = INVERTED_INDEX_COMPRESSED[key][token][0][0]
                        diff_interval = int(doc_id) - int(first_doc)
                        if diff_interval == 0 or diff_interval == INVERTED_INDEX_COMPRESSED[key][token][0][aux-1]:
                            INVERTED_INDEX_COMPRESSED[key][token][1][aux-1] += 1
                        else:
                            INVERTED_INDEX_COMPRESSED[key][token][0].append(diff_interval)
                            INVERTED_INDEX_COMPRESSED[key][token][1].append(1)
    print("Processed inverted index compressed.")

def save_inverted_indexes():
    with open('inverted_index/data/INVERTED_INDEX_UNCOMPRESSED.json', 'w') as f:
        json.dump(INVERTED_INDEX_UNCOMPRESSED, f)
        f.close()

    with open('inverted_index/data/INVERTED_INDEX_COMPRESSED.json', 'w') as f:
        json.dump(INVERTED_INDEX_COMPRESSED, f)
        f.close()

generate_inverted_index()
# print(INVERTED_INDEX_UNCOMPRESSED)
print (f"Size of INVERTED_INDEX_UNCOMPRESSED object in bytes: {utils.get_size(INVERTED_INDEX_UNCOMPRESSED)}")
# print(INVERTED_INDEX_COMPRESSED)
print (f"Size of INVERTED_INDEX_COMPRESSED object in bytes: {utils.get_size(INVERTED_INDEX_COMPRESSED)}")
print(f"Compressed inverted index takes {utils.get_size(INVERTED_INDEX_COMPRESSED) * 100/utils.get_size(INVERTED_INDEX_UNCOMPRESSED)}% less space.")

save_inverted_indexes()
