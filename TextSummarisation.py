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