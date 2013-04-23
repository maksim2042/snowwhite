import simplejson as json
import string
import re
import networkx as net

def trim_degrees(g, degree=1):
    """
    Trim the graph by removing nodes with degree less then value of the degree parameter
    Returns a copy of the graph, so it's non-destructive.
    """
    g2=g.copy()
    d=net.degree(g2)
    for n in g2.nodes():
        if d[n]<=degree: g2.remove_node(n)
    return g2

def sorted_degree(g):
    d=net.degree(g)
    ds = sorted(d.iteritems(), key=lambda (k,v): (-v,k))
    return ds

def sorted_dict(d):
    ds = sorted(d.iteritems(), key=lambda (k,v): (-v,k))
    return ds

def add_or_inc_edge(g,f,t):
    """
    Adds an edge to the graph IF the edge does not exist already. 
    If it does exist, increment the edge weight.
    Used for quick-and-dirty calculation of projected graphs from 2-mode networks.
    """
    if g.has_edge(f,t):
        g[f][t]['weight']+=1
    else:
        g.add_edge(f,t,weight=1)
        
def trim_edges(g, weight=1):
    """
    Remove edges with weights less then a threshold parameter ("weight")
    """
    g2=net.Graph()
    for f, to, edata in g.edges(data=True):
        if edata['weight'] > weight:
            g2.add_edge(f,to,edata)
    return g2

from collections import Counter
def bucketize(seq):
    """
    Produce a bucket histogram 
    """
    hist=Counter(seq)
    return hist

punct_re = re.compile('[%s]' % re.escape(string.punctuation))
def remove_punctuation(text):
    return punct_re.sub('', text)

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    p2=re.compile(r'\[ .*? \]')
    return p2.sub('',p.sub('', data))

def match_words(text,match):
    text_words = set(text.lower().replace(':','').replace('#','').replace('.','').replace('@','').replace('?','').split())
    match_words= set(match.lower().replace(':','').replace('#','').replace('.','').replace('@','').replace('?','').split())
    if len(match_words.intersection(text_words)) == len(match_words):
        return True
    else :
        return False
        
        
def norm(text):
     return(unicodedata.normalize('NFKD', text).encode('ascii','ignore'))