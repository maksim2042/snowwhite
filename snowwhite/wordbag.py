#!/usr/bin/env python
# encoding: utf-8
"""
wordbag.py

Created by Maksim Tsvetovat on 2011-12-08.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

from itertools import islice
import networkx as net
import logging
#import s3writer as s3
#import settings

from hottie import hot

l=logging.getLogger("WORDBAG")
corpusPath='data/'

@hot
class wordbag(object):

    def __init__(self,interval=1000):
        self.word_graph=net.DiGraph()
        self.term_graph=net.Graph()
        self.counter=0
        self.interval=interval
        self.keys=set()

    def add_or_inc_edge(self,g,f,t):
        """
        Adds an edge to the graph IF the edge does not exist already. 
        If it does exist, increment the edge weight.
        Used for quick-and-dirty calculation of projected graphs from 2-mode networks.
        """
        
        if g.has_edge(f,t):
            g[f][t]['weight']+=1
        else:
            g.add_edge(f,t,weight=1)
 
    def trim_edges(self, g, weight=1):
        """
        Remove edges with weights less then a threshold parameter ("weight")
        """
        g2=net.Graph()
        for f, to, edata in g.edges(data=True):
            if edata['weight'] > weight:
                g2.add_edge(f,to,edata)
        return g2       

    def _window(self, seq, n=2):
        "Returns a sliding window (of width n) over data from the iterable"
        " s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ... "
        it = iter(seq)
        result = tuple(islice(it, n))
        if len(result) == n:
            yield result
        for elem in it:
            result = result[1:] + (elem,)
            yield result

    def _add_to_term_graph(self,tokens):
        """
        Takes a linguistic network (NetworkX Graph()) and text;
        converts text to stemmed tokens
        runs a sliding window over the tokens, adding edges to the graph as it goes along
        """
        for pair in self._window(tokens,n=4):
            self.add_or_inc_edge(self.term_graph,pair[0][0],pair[1][0])
            self.add_or_inc_edge(self.term_graph,pair[0][0],pair[2][0])
            self.add_or_inc_edge(self.term_graph,pair[0][0],pair[3][0])


    def add_tokens(self,key, tokens): 
        """
        Adds a list of tokens -- either string or pair (string, sentiment) -- to the corpus
        
        Arguments:
        key : anything hashable
        tokens : a list of (string) or pairs (string number)
        """
        self.keys.add(key)    
        for token in tokens:
            self.add_word(key,token) 
            
        self._add_to_term_graph(tokens)         


    def add_word(self,key,word):
        """
        Add a single word to the corpus
        
        Arguments:
        key : anything hashable
        word : a  (string) or pair (string number)       
        """
        if type(word)== tuple:
            ww=word[0]
            sent = word[1]
            word=ww
        
        try:    
            a_word=word.encode('ascii').strip()
        except :
            return

        if word=="": return
        
        self.counter+=1
        self.word_graph.add_node(key, type='k')
        self.word_graph.add_node(a_word, type='w', sentiment=sent)
        self.add_or_inc_edge(self.word_graph,key,a_word)

        if self.counter>self.interval:
            self.prune()
            self.save()
            self.counter=0
    
    def prune(self):
        """
        Prunes the graph, removing single occurrences
        """
        self.word_graph=self.trim_edges(self.word_graph)
        self.term_graph=self.trim_edges(self.term_graph)
    
    def save(self):
        """
        Saves itself to a file. The data structure could get quite large, caching to disk is a good idea
        
        ** note ** replace with Redis in production -- Redis dependency is removed for Open Source release to decrease complexity
        """
        l.info("<<<<<<< SAVING WORD-GRAPH >>>>>>>")
        net.write_weighted_edgelist(self.word_graph,"wordgraph_edgelist.txt")
    
    def load(self):
        """
        Loads itself from a file. The data structure could get quite large, caching to disk is a good idea
        
        ** note ** replace with Redis in production -- Redis dependency is removed for Open Source release to decrease complexity
        """
        l.info("<<<<<<<< Loading Word-Graph>>>>>>>")
        self.word_graph=net.read_weighted_edgelist("wordgraph_edgelist.txt")
