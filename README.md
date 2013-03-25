Sentiment analysis for English and Spanish (Implicit & Explicit)
=========

import discourse_mapper
import linguist

dm=discourse_mapper.discourse_mapper()


tweet={"text":'this is a test','user':'foobar'}

tokens=linguist.process(tweet['text'])
dm.add(tokens,tweet['user']


dm._get_sentiment('user1','user2')

