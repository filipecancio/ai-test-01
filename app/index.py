from text_catcher import TextCatcher

if __name__ == '__main__':
    text_catcher = TextCatcher()

    example = text_catcher.listen("O rato roeu a roupa do rei de roma")
    print(example)