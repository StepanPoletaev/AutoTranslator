from googletrans import Translator
from typing import Any


def text_translator(text: str, src: str, dest: str) -> Any:
    try:
        translator = Translator()
        translation = translator.translate(text=text, src=src, dest=dest)
        return translation.text
    except Exception as ex:
        return ex


def main():
    print(text_translator(text='Привет! Как дела?', src='ru', dest='en'))


if __name__ == '__main__':
    main()

