#!/usr/bin/env python
# encoding: utf-8
"""
cunning_linguist.py

Created by Maksim Tsvetovat on 2011-12-08.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import english_stoplist
import spanish_stoplist
import re

from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer

import string
import guess_language as gl
import explicit_sentiment as senti

table=string.maketrans("","")

"""A couple of util functions for dealing with large dicts"""
def find_key(dic, val):
    """return the key of dictionary dic given the value"""
    return [k for k, v in dic.iteritems() if v == val][0]

def find_value(dic, key):
    """return the value of dictionary dic given the key"""
    return dic[key]
"""-------------------------------------------------------"""


def strip_punctuation(s):
    """Strip punctuation from a string"""
    return re.sub("[\.\t\,\:;\(\)\.]", "", s, 0, 0)
    #return s.translate(table, string.punctuation)


def process(text):
    """
    This somewhat of a complicated beast. Does all pre-processing for a chunk of text, including:
    
    * cleaning the string
    * Language detection
    * Tokenizing
    * Application of a stop-list (in English or Spanish)
    * Stemming (snowball in English or Spanish)
    
    Args:
    text : (string or clean Unicode) text to be processed
    
    Returns:
    tokens: a list of (token, sentiment) where token is a stemmed word, and sentiment is the explicit sentiment for the token (if found in the corpus)
    
    """
    
    
    try: 
        lang=gl.guessLanguageName(text).lower()
        #print lang
    except:
        return []
    
    tokens = word_tokenize(strip_punctuation(text.lower()))
    out_tokens=[]
        
    if lang == 'english':
        stoplist=english_stoplist.stoplist
        stemmer = SnowballStemmer('english')
    elif lang == 'spanish':
        stoplist=spanish_stoplist.stoplist
        stemmer = SnowballStemmer('spanish')
    else:
        return []
        
    for token in tokens:
        if (token not in stoplist) and (not token.startswith('http')) and (len(token) > 3):
            tt=stemmer.stem(token)
            out_tokens.append((tt, senti.sentiment_token(tt,language=lang)))
                    
    return out_tokens   
