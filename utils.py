import random

import requests

from Classes.class_basicword import BasicWord


def load_random_words_json(way):
    """
    Функция получает список слов из файла внешнего ресурса и возвращает в формате Json
    """
    list_words = requests.get(way)
    list_words_json = list_words.json()

    return list_words_json


def load_random_words(way):
    """
    Функция получает список слов в формате Json и возвращает случайное слово
    """

    list_words_json = load_random_words_json(way)
    word_data = random.choice(list_words_json)
    word = BasicWord(word_data["word"], word_data["subwords"])

    return word
