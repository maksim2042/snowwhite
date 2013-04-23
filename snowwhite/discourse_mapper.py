#!/usr/bin/env python
# encoding: utf-8
"""
discourse_mapper.py

Created by Maksim Tsvetovat on 2011-12-20.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import simplejson as json
from collections import defaultdict
import logging 

import linguist as cl
#import candidates as can
#import media

from wordbag import wordbag
from hottie import hot

import networkx as net
from itertools import permutations

l=logging.getLogger("DMAP")

@hot
class discourse_mapper(object):
    """
    Discourse mapper takes text produced by various *speakers* and computes amount of mirroring betweent the speakers. Mirroring (repeating words and short phrases
    is thought to correspond to the affinity two speakers feel for each other or some alters.
    
    This is a partial replacement for-- but more of an add-on to -- sentiment analysis
    """

    def __init__(self,interval=100):
        #self.s3=s3writer.s3writer()
        self.wb=wordbag()
        self.interval=interval
        self.counter=0
        self.gauges=net.Graph()
        
    def load_corpus(self, key, filename):
        """
        If we have an initial corpus of text for the speakers, pre-load it from a file. 
        
        Using an initial corpus is highly recommended for highly vociforous speakers -- journalists, media outlets, politicians, etc. 
        Using corporate press releases for initial corpus will leave you rather disappointed. 
        
        Arguments:
        key: name of the speaker, or Twitter handle, or unique ID for a speaker (any hashable type)
        filename: name or fully qualified path for a file containing text for this speaker (string)
        """
        l.debug("Loading corpus")
        text=open(filename,'rb').read()    
        tokens=cl.process(text)
        self.wb.add_tokens(key,tokens)
        self.wb.prune()
    
    def add_text(self,key,text):
        """
        Add text to the corpus, computing explicit sentiment of tokens along the way.
        
        Arguments
        key: name of the speaker, or Twitter handle, or unique ID for a speaker (any hashable type) 
        text: just that, text. Plain-old (str) is best, but it will handle reasonable Unicode. Unreasonable Unicode shall be mangled into submission before adding.
        """
        tokens=cl.process(text)
        self.wb.add_tokens(key,tokens)
        
    def add_tokens(self,key,tokens):
        """
        Add token-metric to the corpus. This is useful if (instead of built-in explicit sentiment dictionaries) one wants to use some other sentiment metric.
        
        Arguments
        key: name of the speaker, or Twitter handle, or unique ID for a speaker (any hashable type) 
        tokens: list of pairs [(token, metric)]
        """
        #tokens=cl.process(text)
        #print tokens
        self.wb.add_tokens(key,tokens)

    def compute_metrics(self):
        """
        Computes an "affinity graph" between speakers -- a graph whose nodes are speakers, and value of the edges corresponds to the amount of mirroring detected between speaksers
        
        Note: mirroring numbers can be quite low, usually below 0.01; don't be alarmed -- this is natural. Consider that mirroring=1 means a straight cut-n-paste.
        
        Returns:
        NetworkX affinity graph
        """
        ## for every state, every candidate, compute a linguistic match
        for k1,k2 in permutations(self.wb.keys):
            sent=self._get_sentiment(k1,k2)               
            self.gauges.add_edge(k1,k2, weight=sent)
        return gauges
            
            
    def _get_sentiment(self,key1, key2):
        cs= set(self.wb.word_graph[key1].keys())
        ss = set(self.wb.word_graph[key2].keys())
        p=cs & ss
        return(float(len(p))/float(len(ss)+len(cs)))

"""                
    def _normalize(self):
        for state in self.gauges.keys():
            total=sum(self.gauges[state].values())
            if total==0: continue
            for can in self.gauges[state].keys():
                self.gauges[state][can]=self.gauges[state][can]/total
"""



        
