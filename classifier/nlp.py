import heapq
import re

from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from stop_words import get_stop_words


# Tokenization to all sentences (html docs)
def tokenize(html):
    # regex = r'[\\\n\t\"\'\,\.\!\(\)\*\+\-\/\:\;\<\=\>\|\&\@\%\?\[\]\^\_\`\{\|\}\~]'
    # regex = "[^\w]"
    regex = "[^a-z]" # only letters, no numbers
    html = re.sub(regex, ' ', html).lower()
    html = html.split()
    words = sorted(list(set(html)))
    return words

# Stemize
# ex.: stemmer = PorterStemmer || stemmer = SnowballStemmer('english')
def stemize(stemmer, data):
    data_stemize = []
    for d in data:
        ste = stemmer.stem(d)
        if ste not in data_stemize:
            data_stemize.append(ste)
    return data_stemize

# Stop-words
def remove_stop_words(data):
    stop_words = get_stop_words('english')
    for sw in stop_words:
        if sw in data:
            data.remove(sw)
    return data

# Build vocabulary and generate vectors
def generate_vocab(all_htmls_tokens):
    vocab = []
    for html_tokens in all_htmls_tokens:
        for token in html_tokens:
            if token not in vocab:
                vocab.append(token)
    return vocab

# Words frequency
def get_words_frequency(all_htmls_tokens):
    words_freq = {}
    for html_tokens in all_htmls_tokens:
        for token in html_tokens:
            if token not in words_freq.keys():
                words_freq[token] = 1
            else:
                words_freq[token] += 1
    return words_freq

# Most freq tokens
def get_most_freq_tokens(words_freq, size):
    most_freq = heapq.nlargest(size, words_freq, key=words_freq.get)
    return most_freq

# Vectorize all html tokens
def vectorize(all_htmls_tokens, most_freq_tokens):
    all_htmls_vec = []
    for html_tokens in all_htmls_tokens:
        html_vec = []
        for token in most_freq_tokens:
            if token in html_tokens:
                html_vec.append(1)
            else:
                html_vec.append(0)
        all_htmls_vec.append(html_vec)
    return all_htmls_vec
