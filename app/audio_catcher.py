import SpeechRecognition as SR
from phrase_processor import PhraseProcessor

class AudioCatcher:
    def __init__(self):
        self.recognizer = SR.Recognizer()
        self.microphone = SR.Microphone()
        self.phrase_processor = PhraseProcessor()

    def listen(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source, timeout = 3)

            try:
                text = self.recognizer.recognize_google(audio, language = 'pt-BR')
                tokens = self.phrase_processor.getTokens(text)
                return tokens
            except SR.UnknownValueError:
                return ["ERROR: Não entendi o que você disse"]