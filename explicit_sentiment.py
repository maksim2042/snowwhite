import csv
from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer


lexicons={}
spanish_lexicon = {}

path = '/Users/maksim/Desktop/dev/sentiment/'
in_file1='SpanishSentimentLexicons/fullStrengthLexicon.txt'
in_file2='SpanishSentimentLexicons/mediumStrengthLexicon.txt'
in_file3="english/AFINN-111.txt"

def _read_english_lexicon(filename):
    english_stemmer=SnowballStemmer('english')
    return dict(map(lambda (k,v): (english_stemmer.stem(k.decode('latin-1')),int(v)), [ line.split('\t') for line in open(filename) ]))
    

def _read_spanish_lexicon(filename):
    stemmer = SnowballStemmer('spanish')
    #f_in = csv.reader(open(filename,'rb'),delimiter='\t')
    f_in = open(filename,'rb')
    
    for line in f_in:
        row=line.split('\t')
        word = stemmer.stem(row[0].decode('latin-1'))
        
        if len(row) > 3:
            val=row[3]
        else:
            val=row[2]
        
        if val=='pos':
            spanish_lexicon[word]=1
        else:
            spanish_lexicon[word]=-1

_read_spanish_lexicon(path+in_file1)
_read_spanish_lexicon(path+in_file2)
english_lexicon=_read_english_lexicon(path+in_file3)

lexicons['english']=english_lexicon
lexicons['spanish']=spanish_lexicon




def sentiment_token(token, language='english'): ##or spanish
    """
    Compute sentiment for a token -- in this case, a stemmed word
    
    Args:
    token: (string) a stemmed word
    language: 'english' and 'spanish' are supported, all others will return 0
    
    Returns:
    sentiment : -5 to +5 
    """

    try:
        return(lexicons[language][token])
    except KeyError:
        return 0

def sentiment_sentence(text,language='english'): ## or spanish
    """
    Compute sentiment for text

    Args:
    text: (string) or a clean Unicode string. 
    language: 'english' and 'spanish' are supported, all others will return 0

    Returns:
    sentiment : -5 to +5 
    """
    tokens = word_tokenize(text)
    sent = [lexicons[language][t] for t in tokens if t in lexicons[language]]
    if len(sent)==0: return 0
    return (sum(sent)/float(len(sent)))
    