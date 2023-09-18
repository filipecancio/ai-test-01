import nltk
from nltk import word_tokenize, corpus
from nltk.corpus import floresta
from nltk.stem import RSLPStemmer

class PhraseProcessor:
    def __init__(self):
        nltk.download('rslp')
        nltk.download('floresta')
        nltk.download('stopwords')
        nltk.download('punkt')

        self.stopwords = set(corpus.stopwords.words('portuguese'))
        self.stemmer = RSLPStemmer()
    
    def getTokens(self, text):
        token_list = word_tokenize(text)
        for token in token_list:
            if token in self.stopwords:
                token_list.remove(token)
        return token_list