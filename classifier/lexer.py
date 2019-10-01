import re

def tokenize(data):
    return data.split()

def normalize(data):
    regex = r'[\\\n\t\"\'\,\.\!\(\)\*\+\-\/\:\;\<\=\>\|\&\@\%\?\[\]\^\_\`\{\|\}\~]'
    data = re.sub(regex, ' ', data)
    data = data.lower()
    return data

def preprocess(data):
    data = normalize(data)
    data = tokenize(data)
    return data
