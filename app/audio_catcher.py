import speech_recognition as SR
from general_functions import getDirectory
from phrase_processor import PhraseProcessor

class AudioCatcher:
    def __init__(self):
        self.recognizer = SR.Recognizer()
        self.microphone = SR.Microphone()
        self.phrase_processor = PhraseProcessor()

    def listen(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("🎤 fale alguma coisa 🎤")
            text = self.recognizer.listen(source, timeout = 3)
            print("🚧 processando audio 🚧")

            return self.process_audio(text)
        
    def play_recorded_audio(self, audio_path):
        audio = getDirectory(audio_path)
        with SR.AudioFile(audio) as source:
            text = self.recognizer.listen(source)
            return self.process_audio(text)
            
    def process_audio(self,audio):
        try:
            text = self.recognizer.recognize_google(audio, language = 'pt-BR')
            tokens = self.phrase_processor.getTokens(text)
            return tokens
        except SR.UnknownValueError:
            return ["ERROR: Não entendi o que você disse"]