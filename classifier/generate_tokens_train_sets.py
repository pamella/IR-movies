import nlp
import json

X_TRAIN = []
Y_TRAIN = []

def get_website_html_pages_tokens(website_name):
    with open(f'classifier/html_docs/{website_name}_html_docs.json', 'r', encoding='utf-8') as f:
        html_docs_list = json.load(f)
        f.close()

    for html_doc in html_docs_list:
        if html_doc[0] and '<!DOCTYPE' in html_doc[0]:
            X_TRAIN.append(nlp.tokenize(html_doc[0]))
            Y_TRAIN.append(html_doc[1])

def save_tokes_to_train_sets():
    with open('classifier/train_sets/X_train.json', 'w') as f:
        json.dump(X_TRAIN, f)

    with open('classifier/train_sets/Y_train.json', 'w') as f:
        json.dump(Y_TRAIN, f)

def main():
    get_website_html_pages_tokens('imdb')
    get_website_html_pages_tokens('agoodmovietowatch')
    get_website_html_pages_tokens('findamovie')
    get_website_html_pages_tokens('flixboss')
    get_website_html_pages_tokens('justwatch')
    get_website_html_pages_tokens('metacritic')
    get_website_html_pages_tokens('rottentomatoes')
    get_website_html_pages_tokens('themoviedb')
    get_website_html_pages_tokens('trakt')
    get_website_html_pages_tokens('tvguide')
    save_tokes_to_train_sets()

if __name__ == "__main__":
    main()
