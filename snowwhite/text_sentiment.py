#!/usr/bin/env python
# encoding: utf-8
"""
text_sentiment.py

Created by Maksim Tsvetovat on 2013-01-19.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""
import linguist

def sentiment(text):
    """
    Takes a bunch of text, computes total sentiment for it. 
    
    Args:
    text: (string) or clean unicode
    
    Returns:
    sentiment: -5 ("fuck shit horrible awful death") to +5 ("awesome happy jumping for joy")
    """
    
    
    text=unicodedata.normalize('NFKD', text).encode('ascii','ignore')
    tokens = linguist.process(text)
    if len(tokens) == 0: return 0

    #dm.add_to_corpus('twitter', tokens)
    ts = sum([t[1] for t in tokens])/float(len(tokens))
    return ts
