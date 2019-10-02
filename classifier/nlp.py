import heapq
import re


# Tokenization to all sentences (html docs)
def tokenize(html):
    # regex = r'[\\\n\t\"\'\,\.\!\(\)\*\+\-\/\:\;\<\=\>\|\&\@\%\?\[\]\^\_\`\{\|\}\~]'
    # regex = "[^\w]"
    regex = "[^a-z]" # only letters, no numbers
    html = re.sub(regex, ' ', html).lower()
    html = html.split()
    words = sorted(list(set(html)))
    return words

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
