try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
from bs4 import BeautifulSoup

def getRelevantText(url): 
    page = urllib2.urlopen(url).read().decode('utf8', 'ignore')
    soup = BeautifulSoup(page, "lxml")
    text = ' '.join(map(lambda p:p.text, soup.find_all('article')))
    relevantText = text.replace("?", " ")
    return relevantText

url = "https://www.washingtonpost.com/news/the-switch/wp/2016/10/18/the-pentagons-massive-new-telescope-is-designed-to-track-space-junk-and-watch-out-for-killer-asteroids/?noredirect=on"
text = getRelevantText(url)
print(text)

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation

sentences = sent_tokenize(text.lower())

words = word_tokenize(text.lower())
words
_stopwords = set(stopwords.words('english') + list(punctuation))
unwanted_words = set(('“', '”', '’'))
relevant_words = [word for word in words if word not in _stopwords and word not in unwanted_words]

from nltk.probability import FreqDist
freq = FreqDist(relevant_words)
from heapq import nlargest
nlargest(10, freq, key=freq.get)

from collections import defaultdict
ranking=defaultdict(int)

for i, sent in enumerate(sentences):
    for w in word_tokenize(sent.lower()):
        if w in freq:
            ranking[i] += freq[w]
            
sents_idx = nlargest(4, ranking, key=ranking.get)
sents_idx