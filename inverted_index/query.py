import json


with open('inverted_index/data/INVERTED_INDEX_UNCOMPRESSED.json') as f:
    inverted_index = json.load(f)

def search(field, value):
    value_words = value.split(' ')
    result_docs_id = {}
    for word in value_words:
        if not result_docs_id:
            result_docs_id = inverted_index[field][word].keys()
        else:
            result_docs_id = result_docs_id & inverted_index[field][word].keys()

    return result_docs_id


result_docs = search('title', 'harry potter')
print(result_docs)
import ipdb ; ipdb.set_trace()
