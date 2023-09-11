from nltk import word_tokenize, corpus
from nltk.corpus import floresta
from nltk.stem import RSLPStemmer

class PreProcessing:
    def __init__(self):
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

    def preprocess(self, text):
        tokens = word_tokenize(text)
        tokens = [token.lower() for token in tokens if token.isalpha()]
        tokens = [token for token in tokens if token not in self.stopwords]
        tokens = [self.stemmer.stem(token) for token in tokens]
        return tokens
