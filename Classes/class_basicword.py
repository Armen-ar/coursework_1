class BasicWord:

    def __init__(self, word, sub_words):
        """
        Магический метод с аргументами: исходное слово и набор допустимых подслов
        """
        self.word = word
        self.sub_words = sub_words

    def __repr__(self):
        """
        Магический метод возвращает текст с вопросом
        """

        return f"из '{self.word}' можно составить {len(self.sub_words)} слов"

    def check_sub_words(self, sub_word):
        """
        Метод проверяет вхождения введенного слова в список подслов
        """

        return sub_word.lower() in self.sub_words

    def count_sub_words(self):
        """
        Метод подсчёта количества подслов, правильных ответов
        """

        return len(self.sub_words)
