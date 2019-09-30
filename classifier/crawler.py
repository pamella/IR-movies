import json

import requests

from links.links_list import (
    agoodmovietowatch_links,
    findamovie_links,
    flixboss_links,
    imdb_links,
    justwatch_links,
    metacritic_links,
    rottentomatoes_links,
    themoviedb_links,
    trakt_links,
    tvguide_links,
)


def get_html_text_or_none(link):
    r = requests.get(link)
    if r.ok:
        return r.text
    return None

def save_website_html_pages_as_json(website_name, website_links):
    data = []
    for link in website_links:
        html_text = get_html_text_or_none(link[0])
        data.append(html_text)

    with open(f'classifier/html_docs/{website_name}_html_docs.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.close()

def main():
    save_website_html_pages_as_json('imdb', imdb_links)
    save_website_html_pages_as_json('agoodmovietowatch', agoodmovietowatch_links)
    save_website_html_pages_as_json('findamovie', findamovie_links)
    save_website_html_pages_as_json('flixboss', flixboss_links)
    save_website_html_pages_as_json('justwatch', justwatch_links)
    save_website_html_pages_as_json('metacritic', metacritic_links)
    save_website_html_pages_as_json('rottentomatoes', rottentomatoes_links)
    save_website_html_pages_as_json('themoviedb', themoviedb_links)
    save_website_html_pages_as_json('trakt', trakt_links)
    save_website_html_pages_as_json('tvguide', tvguide_links)

if __name__ == "__main__":
    main()
