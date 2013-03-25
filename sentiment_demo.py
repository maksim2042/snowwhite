import simplejson as json
import re
from collections import defaultdict

import linguist
import discourse_mapper
import explicit_sentiment

from media import media

import requests
import multimode as mm


dm=discourse_mapper.discourse_mapper()

def clean_text(text):
    s=re.sub('<[^<]+?>', '', text).lower()
    try: 
        return str(s).decode('utf8',errors='ignore')
    except:
        return ""


def get_tweets(screenname):
    url = 'http://api.twitter.com/1/statuses/user_timeline.json?include_entities=false&include_rts=false&count=200&screen_name='+screenname   
    try :
        tweets=json.loads(requests.get(url).content)
        return [clean_text(t['text']) for t in tweets]
    except:
        print ';('
        return []
        

direct_speech = defaultdict(list)

for cid,c in can.iteritems():
    for sn in c:
        tweets=get_tweets(sn)
        direct_speech[cid].extend(tweets)

for cid,names in media.iteritems():
    for sn in names:
        tweets=get_tweets(sn)
        direct_speech[cid].extend(tweets)
    
for cid,tweets in direct_speech.iteritems():
    for tweet in tweets:
        #sent = explicit_sentiment.sentiment_sentence(tweet)
        tokens = linguist.process(tweet)
        if len(tokens) == 0: continue
        
        dm.add_to_corpus(cid, tokens)
        ts = sum([t[1] for t in tokens])/float(len(tokens))
        print ts,'>>>',tweet
        
        
    
mm.plot_multimode    
    
"""zdata=zipfile.ZipFile(open('data/idf.json.zip','rb'))
jfile=zdata.namelist()[0]

for i,tweet in enumerate(zdata.open(jfile)):
    if i > 10000: break
    
    js=json.loads(tweet)
    
    author=js['author'][0]['name'].lower()
    try:
        text = clean_text(js['object']['content']['text'])
    except:
        continue
    
    tokens=linguist.process(text)
    print author
    dm.add(tokens,author)
"""
    
 
