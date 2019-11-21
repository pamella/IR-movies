import json


with open('inverted_index/data/INVERTED_INDEX_UNCOMPRESSED.json') as f:
    inverted_index = json.load(f)
    f.close()

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

with open('inverted_index/data/html_docs_tokens_all.json') as f:
    html_docs_tokens_all = json.load(f)
    f.close()

with open('inverted_index/data/html_docs_tokens_true.json') as f:
    html_docs_tokens_true = json.load(f)
    f.close()

import ipdb ; ipdb.set_trace()
