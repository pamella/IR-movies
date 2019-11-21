import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:/Users/pammb/Documents/projects/cin/IR-movies/classifier')
import nlp
import json


def get_website_html_pages_tokens(website_names, filter_type):
    result = []
    html_doc_id = 0

    for website_name in website_names:
        with open(f'classifier/html_docs/{website_name}_html_docs_complete.json', 'r', encoding='utf-8') as f:
            html_docs_list = json.load(f)
            f.close()

        for html_doc in html_docs_list:
            if filter_type == 'true' and html_doc[0] and '<!DOCTYPE' in html_doc[0] and (html_doc[1] == True):
                    result.append([html_doc_id, html_doc[2], html_doc[3], nlp.tokenize(html_doc[0])])
                    html_doc_id = html_doc_id + 1
            elif filter_type == 'all' and html_doc[0] and '<!DOCTYPE' in html_doc[0]:
                    result.append([html_doc_id, html_doc[2], html_doc[3], nlp.tokenize(html_doc[0])])
                    html_doc_id = html_doc_id + 1
        print(f'Get {website_name.upper()} tokens.')
    print(html_doc_id)
    return result


def save_object_as_json(obj, filename):
    with open(f'inverted_index/data/{filename}.json', 'w') as f:
        json.dump(obj, f)
    print (f'Save {filename.upper()} as json.')


###

website_names = [
    'imdb',
    'agoodmovietowatch',
    'findamovie',
    'flixboss',
    'justwatch',
    'metacritic',
    'rottentomatoes',
    'themoviedb',
    'trakt',
    'tvguide',
]

html_docs_list_all = get_website_html_pages_tokens(website_names, 'all')
save_object_as_json(html_docs_list_all, 'html_docs_tokens_all')

html_docs_list_true = get_website_html_pages_tokens(website_names, 'true')
save_object_as_json(html_docs_list_true, 'html_docs_tokens_true')
