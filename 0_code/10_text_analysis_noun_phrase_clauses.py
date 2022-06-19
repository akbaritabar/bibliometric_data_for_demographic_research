# adopted and modified from getting started into in "https://spacy.io/" (as of April 2022)

# Spacy is installed, but you need to open an anaconda prompt (or a terminal) then "activate bibliodemography" environment, and call the following to download the pre-trained models for English
# python -m spacy download en_core_web_sm
import spacy
import pandas as pd
import os

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")


# ============================
#### In/Output folders for data/resutls/tables/images ####
# ============================
# data URLs
data_dir = os.path.join('..', '1_data')

# results
processed_data = os.path.join('..', '98_outputs')


# ============================
#### sample abstracts ####
# ============================

abstracts = pd.read_csv(os.path.join(data_dir, 'sample_abstracts_table.csv'))

# ============================
#### Functions ####
# ============================

# we define a custom function to run it on pandas dataframe column including abstracts

def nlp_custom(doc2use):
    doc = nlp(doc2use)
    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
    entity_labels = []
    for entity in doc.ents:
        entity_labels.append((entity.text, entity.label_))
        
    return (noun_phrases, verbs, entity_labels)

# ============================
#### Extracting noun-phrase-clauses ####
# ============================

# apply custom function and add a new column 
# (you can parallelize this step too! how?! using dask dataframes)
abstracts = abstracts.assign(spacy_res=abstracts.loc[:, 'abstract'].apply(nlp_custom))

# see some results
abstracts.spacy_res[0]
abstracts.spacy_res[1]
abstracts.spacy_res[2]

# Potential next steps (feel free to extend!):
#   remove English stopwords? (you have one example in script 8)
#   lowercase, then deduplicate by groupby and count occurrences?
#   or consider calculating some sort of relevance score (TFIDF?)
