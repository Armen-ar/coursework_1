class Player:

    def __init__(self, user_name):
        """
        Магический метод с аргументом: имя игрока
        """

        self.user_name = user_name
        self.used_words = []

    def count_used_words(self):
        """
        Метод получения количества правильных ответов игрока
        """

        return len(self.used_words)

    def adding_words(self, word):
        """
        Метод добавления правильного ответа в список ответов self.used_word
        """
        self.used_words.append(word)

    def check_used_words(self, word):
        """
        Метод проверки использования данного слова
        """

        return word.lower() in self.used_words
