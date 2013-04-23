Sentiment analysis for English and Spanish (Implicit & Explicit)
=========

Sentiment analysis is a “hot topic” in the analysis of social media, blogosphere and news sources. 
Marketers, journalists and government officials routinely ask questions along the lines of “What 
does the Blogosphere think” about a certain subject. In many ways analysis of online sentiment is 
replacing more labor-intensive methods such as focus groups and polling.

However, Internet sentiment analysis suffers from a num- ber of inherent problems. As a replacement 
for polling, it has a significant selection bias – results are heavily biased toward large urban 
centers as the concentration of social media users is significantly higher in urban areas. As a 
replacement for focus groups, sentiment analysis lacks in-depth inspection of con- tents of discourse – 
thus missing the reasons why sentiment tends to take a specific direction.

Sentiment analysis itself is rather inaccurate. Even human coders perform badly in randomized trials, 
as sentiment is a subjective metric. For example, a phrase “I bought a Honda yesterday” was perceived 
by 45 percent as sentiment-neutral and 50 percent as positive (i).

Finally, it is rather distasteful that the entire rich, varied, poetic spectrum of human emotions 
gets reduced to a number between -1 and 1. It is an inelegant approach to a complex problem, throwing 
out too much good information too early in the process.

*SnowWhite* attempts to remedy that with a new approach to sentiment analysis -- *Implicit Sentiment*.

Impicit Sentiment
-----------------

Rather then compute how many positive or negative words one used, we look at how much two speakers have
in common. This rate of -mirroring- is directly related to expressed sentiment and seems to be a better
predictor of what the speaker has actually said then pure word-counting.

How to run SnowWhite
--------------------

```from snowwhite import discourse_mapper

dm=discourse_mapper.discourse_mapper()

###for all tweets containing ['user'] and ['text']:
  dm.add_text(tweet['user'],tweet['text'])`
```

### get a sentiment graph:
sentiment_graph=dm.compute_metrics()

### get pair-wise sentiment for any pair of users
dm._get_sentiment('user1','user2')`

