import nltk
from nltk import word_tokenize, corpus
from nltk.corpus import floresta
from nltk.stem import RSLPStemmer

class Wizzard:
    def __init__(self):
        nltk.download()

        self.stopwords = set(corpus.stopwords.words('portuguese'))
        self.stemmer = RSLPStemmer()

    def initialize(self):
        for(word,classifications) in floresta.tagged_words():
            classifications.append(word.lower(),classifications)

        return{
            "stop_words":self.stopwords,
            "classificacoes":classifications
        }
    
    def getTokens(self, text):
        tokens = word_tokenize(text)
        return tokens