from phrase_processor import PhraseProcessor

class TextCatcher:
    def __init__(self):
        self.phrase_processor = PhraseProcessor()

    def listen(self,text):
        return self.phrase_processor.getTokens(text)