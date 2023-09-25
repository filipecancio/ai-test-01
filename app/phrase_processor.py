import nltk
from nltk import word_tokenize, corpus
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
        self.LANGUAGE_CORPUS = "portuguese"
        self.LANGUAGE_TALK = "pt-BR"

        self.getDepencies()
        self.stopwords = set(corpus.stopwords.words(LANGUAGE_CORPUS))
        self.stemmer = RSLPStemmer()
    
    def removeStopWords(self, text):
        token_list = word_tokenize(text)
        for token in token_list:
            if token in self.stopwords:
                token_list.remove(token)
        return token_list
    
    def getDepencies(self):
        try:
            nltk.data.find('punkt.zip')
        except:
            nltk.download('punkt')
        try:
            nltk.data.find('rslp.zip')
        except:
            nltk.download('rslp')
        try:
            nltk.data.find('floresta.zip')
        except:
            nltk.download('floresta')
        try:
            nltk.data.find('stopwords.zip')
        except:
            nltk.download('stopwords')