from Classes.class_player import Player
from utils import load_random_words

WAY = 'https://jsonkeeper.com/b/12I7'

print("Введите имя игрока")
user_name = input()
player = Player(user_name)

basic_word = load_random_words(WAY)
basic_word_ = basic_word.word.upper()
basic_word_count = basic_word.count_sub_words()
print(f"Привет, {user_name}!")
print(f"Составьте {basic_word_count} слов из слова '{basic_word_}'")
print("Слова должны быть не короче 3 букв\nПоехали, ваше первое слово?\nЧтобы закончить игру, угадайте все"
      " слова или напишите 'stop'")

total_correct_answers = 0

while player.count_used_words() < basic_word_count:
    """
    Запускаем бесконечный цикл, пока угаданные слова игрока
     по количеству меньше чем количество подслов
     """
    user_input = input().lower()
    if user_input == "stop":
        print("игра завершена!")
        break
    elif not basic_word.check_sub_words(user_input):
        print("неверно")
        continue
    elif player.check_used_words(user_input):
        print("неверно")
        continue
    player.adding_words(user_input)
    total_correct_answers += 1
    print("верно")

print(f"слова закончились, игра завершена!\nвы угадали {total_correct_answers} слов")
