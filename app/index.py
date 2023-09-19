from audio_catcher import AudioCatcher

if __name__ == '__main__':
    audio_catcher = AudioCatcher()

    example = audio_catcher.play_recorded_audio("/util/audio/familia_chita.wav")
    print(example)