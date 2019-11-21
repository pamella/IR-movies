import json


with open('inverted_index/data/INVERTED_INDEX_UNCOMPRESSED.json') as f:
    inverted_index = json.load(f)
    f.close()

def search(field, value):
    """
        Allowed fields: title, year, genre
    """
    value_words = value.split(' ')
    result_docs_id = {}
    for word in value_words:
        if not result_docs_id:
            result_docs_id = inverted_index[field][word].keys()
        else:
            result_docs_id = result_docs_id & inverted_index[field][word].keys()

    return result_docs_id


with open('inverted_index/data/html_docs_tokens_all.json') as f:
    html_docs_tokens_all = json.load(f)
    f.close()


with open('inverted_index/data/html_docs_tokens_true.json') as f:
    html_docs_tokens_true = json.load(f)
    f.close()


def get_websites_list(html_docs, ids_list):
    links = []
    for id in ids_list:
        if html_docs.get(id):
            links.append(html_docs.get(id)[1])
    return links

import ipdb ; ipdb.set_trace()

# result_docs = search('title', 'breakfast club')
search_field = input('Digite o field que deseja buscar (title, year, genre)\n')
search_value = input('Digite o valor que deseja buscar (ex.: imitation game)\n')

result_docs = search(search_field, search_value)
result_links_all = get_websites_list(html_docs_tokens_all, result_docs)
result_links_true = get_websites_list(html_docs_tokens_true, result_docs)

print(f'Docs id:\n {result_docs}\n')
print(f'All:\n {result_links_all}\n')
print(f'True:\n {result_links_true}\n')
