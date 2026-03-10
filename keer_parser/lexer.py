import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)
    return text

def tokenize(text):
    text = clean_text(text)
    tokens = text.split()
    return tokens