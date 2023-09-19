import nltk
from nltk import word_tokenize, corpus
from nltk.corpus import floresta
from nltk.stem import RSLPStemmer

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class PhraseProcessor(metaclass=SingletonMeta):
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