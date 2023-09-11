from wizzard import Wizzard

if __name__ == '__main__':
    wizzard = Wizzard()
    wizzard.initialize()

    example = "O rato roeu a roupa do rei de roma"
    tokens = wizzard.getTokens(example)
    print(tokens)