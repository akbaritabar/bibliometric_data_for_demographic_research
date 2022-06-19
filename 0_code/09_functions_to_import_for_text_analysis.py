import pandas as pd
# for text analysis
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pydash
import ast
from collections import Counter
# to have a better search of words used with 'anchor words'
import string
# for complementing using regex
import re

# ============================
#### Functions ####
# ============================


def clean_txt(txt2clean):
    if isinstance(txt2clean, str):
        txt2clean = txt2clean.lower(
        ).strip()
        txt2clean = re.sub(r"[^a-z0-9 ]", "", txt2clean)
        return txt2clean
    else:
        try:
            txt2clean = txt2clean.str.lower(
            ).str.strip()
            txt2clean = re.sub(r"[^a-z0-9 ]", "", txt2clean.str)
            return txt2clean
        except AttributeError:
            return txt2clean

# Find keyword pairs in the corpus
# # using regex to search for EXACT PHRASEs
# function to search title, abstract, keywords with regex

# ALL word pairs
def search_word_pairs(x):
    keywords = [
        # add your intended word pairs here
        r'adult neurogenesis',
        r'synaptic plasticity',
        r'cortical plasticity',
        r'cortical map plasticity',
        r'receptive field plasticity',
        r'heterosynaptic plasticity',
        r'hebbian plasticity',
        r'structural plasticity',
        r'neuronal responses',
        r'plasticity of neuronal responses',
        r'bidirectional plasticity',
        r'functional plasticity',
        r'developmental plasticity',
        r'critical period plasticity',
        r'adult brain plasticity',
        r'ocular dominance plasticity',
        r'neuronanatomical plasticity',
        r'cross modal plasticity',
        r'survival'
    ]

    p = re.compile(r'(?:%s)' % '|'.join(keywords), flags=re.IGNORECASE)
    try:
        res2return = p.findall(x)
        if any(res2return):
            return [x.lower() for x in res2return if x]
        else:
            return None
    except TypeError:
        return None

# strict, because it considers word boundaries (e.g., only exact word "king" is taken, "kings" is excluded)
def search_word_pairs_strict(x):
    keywords = [
        # add your intended word pairs here
        r'adult neurogenesis',
        r'synaptic plasticity',
        r'cortical plasticity',
        r'cortical map plasticity',
        r'receptive field plasticity',
        r'heterosynaptic plasticity',
        r'hebbian plasticity',
        r'structural plasticity',
        r'neuronal responses',
        r'plasticity of neuronal responses',
        r'bidirectional plasticity',
        r'functional plasticity',
        r'developmental plasticity',
        r'critical period plasticity',
        r'adult brain plasticity',
        r'ocular dominance plasticity',
        r'neuronanatomical plasticity',
        r'cross modal plasticity',
        r'survival'        
    ]

    p = re.compile(r'\b(?:%s)\b' % '|'.join(keywords), flags=re.IGNORECASE)
    try:
        res2return = p.findall(x)
        if any(res2return):
            return [x.lower() for x in res2return if x]
        else:
            return None
    except TypeError:
        return None



# ============================
#### Functions for anchor word search ####
# ============================

# another function that tokenizes words with nltk then finds first/second words
# before/after our anchor words


def find_target(text, target='plasticity'):
    if isinstance(text, str) and len(text) > 0:
        text = word_tokenize(text)
        text = list(filter(lambda token: token not in string.punctuation, text))
        text = [lowtext.lower() for lowtext in text]
        results = {
            'word_before': [],
            'target_word': [],
            'word_after': []
        }
        index = -1
        for word in text:
            if target in word:
                index = text.index(word, index+1)
                results['target_word'].append(text[index])
                try:
                    results['word_before'].append(text[index-1])
                except IndexError:
                    results['word_before'].append(None)
                try:
                    results['word_after'].append(text[index+1])
                except IndexError:
                    results['word_after'].append(None)
        return results


# first simplify found-words to exclude stopwords, etc.


def simplify_found_words(found_words):
    if isinstance(found_words, str):
        found_words = ast.literal_eval(found_words)
        words_before = pydash.get(found_words, 'word_before', default=[])
        words_after = pydash.get(found_words, 'word_after', default=[])
        # remove STOPWORDS
        words_before = [
            word for word in words_before if not word in stopwords.words('english')]
        words_before = dict(Counter(words_before))
        keys2return = []
        for key, _ in words_before.items():
            keys2return.append(key)
        words_after = [
            word for word in words_after if not word in stopwords.words('english')]
        words_after = dict(Counter(words_after))
        keys2return2 = []
        for key2, _ in words_after.items():
            keys2return2.append(key2)

        # control empty lists and exclude
        if len(keys2return) == 0:
            keys2return = None
        if len(keys2return2) == 0:
            keys2return2 = None
        return str(keys2return), str(keys2return2)
