import os
from pprint import *
import googleapiclient.discovery
import pandas as pd
import numpy as np
import seaborn as sns
from dateutil import parser
import matplotlib.pyplot as plt
sns.set(rc={'figure.figsize':(11.7,8.27)})
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
import os
import sys
from tqdm import tqdm
import re
import pickle

STEMS_PATH = "./stemmed_no_duplicates.pckl"
STEMS_WITH_DUP = "./stemmed_tokens.pckl"

print("Loading pre-computed stems...")

with open(STEMS_PATH,"rb") as f:
    stemmed_no_duplicates = pickle.load(f)
    
with open(STEMS_WITH_DUP,"rb") as f:
    stemmed_tokens = pickle.load(f)

stem_counts = pd.Series(stemmed_tokens).value_counts()
frequent_stems_counts = stem_counts[stem_counts >= 20]

from gensim.models import KeyedVectors

# Load vectors directly from the file
model = KeyedVectors.load_word2vec_format('../../frwiki-20181020.treetag.2.ngram-pass2__2019-04-08_09.02__.s500_w5_skip.word2vec.bin', binary=True)

# available_stems = []
stems_embeddings = []
for word in list(frequent_stems_counts.index):
    if word in model.key_to_index:
        # available_stems.append(word) 
        stems_embeddings.append(model[word])

avail_freq_stems_counts = frequent_stems_counts[frequent_stems_counts.index.isin(model.key_to_index)]

stems_embeddings = np.array(stems_embeddings)
print("stems_embeddings shape =", stems_embeddings.shape)
print("their frequencies shape =", avail_freq_stems_counts.shape)