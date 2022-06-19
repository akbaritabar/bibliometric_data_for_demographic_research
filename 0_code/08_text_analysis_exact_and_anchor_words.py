import pandas as pd
import os
import importlib

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

# to see more pandas columns & not to use scientific notation
pd.set_option('max_colwidth',100)
pd.set_option('display.float_format', '{:.2f}'.format)

# ============================
#### More advanced (parallelization of search) DO NOT RUN, but ask if interested ####
# ============================

# to search for word pairs in parallel instead of one per row, as they are independent from each other
import dask.dataframe as dd
from dask.distributed import Client, as_completed
# workaround for windows import error from: (https://github.com/dask/distributed/issues/4168), if using jupyterlab, this is not needed
# import multiprocessing.popen_spawn_win32
# use these only inside jupyterlab to prevent errors with VSCode (if using vscode, add "processes=False")
client = Client(n_workers=10, memory_limit='5GB')


# ============================
#### In/Output folders for data/resutls/tables/images ####
# ============================
# data URLs
data_dir = os.path.join('..', '1_data')

# results
processed_data = os.path.join('..', '98_outputs')

# ============================
#### Functions ####
# ============================

# functions are being imported from module 9
fun2use = importlib.import_module(r"09_functions_to_import_for_text_analysis")
# to reload an already imported (but recently modified) module: importlib.reload(fun2use)


# ============================
#### sample abstracts ####
# ============================

abstracts = pd.read_csv(os.path.join(data_dir, 'sample_abstracts_table.csv'))

# ============================
#### Finding our word-pairs and anchor-words ####
# ============================

# search and add columns
abstracts['search_word_pairs'] = abstracts['abstract'].map(fun2use.search_word_pairs)
abstracts['search_word_pairs_strict'] = abstracts['abstract'].map(fun2use.search_word_pairs_strict)
abstracts['search_anchors'] = abstracts['abstract'].map(fun2use.find_target)
# let's change the anchor for the last abstract (which is demographic)
# it is important to choose anchor word wisely!
abstracts['search_anchors2'] = abstracts['abstract'].apply(lambda x: fun2use.find_target(x, target='factors'))

# compute these added columns (if using in parallelized mode! ask for more detail, if interested!)
# abstracts_res = abstracts.compute()

# add counts for each group of words we searched (using only for the lists here, i.e., word-pair searches, won't work for anchor searches)
abstracts['c_search_word_pairs'] = abstracts['search_word_pairs'].str.len()
abstracts['c_search_word_pairs_strict'] = abstracts['search_word_pairs_strict'].str.len()


# ============================
#### Further simplify found words (adjacent words used before/after anchor words) ####
# ============================
# apply function (adds new columns to compare)
abstracts['search_anchors_str'] = abstracts['search_anchors'].astype(str)

# exact words
abstracts_simplified = abstracts.apply(lambda row: fun2use.simplify_found_words(
    row.search_anchors_str), axis='columns', result_type='expand').rename(columns={0: 'words_before_abs', 1: 'words_after_abs'})

abstracts = pd.concat(
    [abstracts, abstracts_simplified], axis='columns')
