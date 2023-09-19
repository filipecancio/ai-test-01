from phrase_processor import PhraseProcessor
from audio_catcher import AudioCatcher
import os

def getDirectory(rel_dir):
    script_dir = os.path.dirname(__file__)
    complete_dir = script_dir + rel_dir
    return complete_dir

if __name__ == '__main__':
    audio_catcher = AudioCatcher()
    familia_chita = getDirectory("/util/audio/familia_chita.wav")

    example = audio_catcher.play_recorded_audio(familia_chita)
    print(example)