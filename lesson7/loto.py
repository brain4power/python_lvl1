#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random


class Card:
    def __init__(self):
        self._count = 15
        self._fill_card()

    def _fill_card(self):
        self._card_content = [[], [], []]
        for i in range(3):
            for j in range(9):
                self._card_content[i].append(None)
        number_pull = [[n for n in range(1, 10)], [n for n in range(10, 20)], [n for n in range(20, 30)],
                       [n for n in range(30, 40)], [n for n in range(40, 50)], [n for n in range(50, 60)],
                       [n for n in range(60, 70)], [n for n in range(70, 80)], [n for n in range(80, 90)]]
        for each in number_pull:
            random.shuffle(each)
        for i in range(3):
            choose_5 = [n for n in range(9)]
            random.shuffle(choose_5)
            choose_5 = choose_5[0:5]
            for ixd, element in enumerate(choose_5):
                self._card_content[i][element] = number_pull[element].pop()

    @property
    def draw_card(self):
        return_string = ""
        for i in range(3):
            for j in range(9):
                if self._card_content[i][j] is None:
                    return_string += "  "
                elif self._card_content[i][j] < 0:
                    return_string += "--"
                else:
                    if self._card_content[i][j] < 10:
                        return_string += " " + str(self._card_content[i][j])
                    else:
                        return_string += str(self._card_content[i][j])
                return_string += " "
            if i is not 2:
                return_string += "\n"
        return print(return_string)


class Game:
    def __init__(self, user_card, computer_card):
        self.user_card = user_card
        self.computer_card = computer_card
        self.pocket = [n for n in range(1, 91)]
        random.shuffle(self.pocket)


    def draw_playing_field(self):
        print("------ Ваша карточка -----")
        self.user_card.draw_card
        print("--------------------------")
        print("-- Карточка компьютера ---")
        self.computer_card.draw_card
        print("--------------------------")

    def play_game(self):
        while self.computer_card._count != 0 or self.user_card._count != 0:
            label = False
            new_barrel = self.pocket.pop()
            print("Новый боченок: {}, осталось боченков: {}".format(new_barrel, len(self.pocket)))
            self.draw_playing_field()
            user_input = str(input('Зачеркнуть цифру? (y/n): '))
            if user_input not in ['y', 'n']:
                print("Надо было вводить только y или n. Вы проиграли!")
                exit()
            for i in range(3):
                for j in range(9):
                    if self.user_card._card_content[i][j] == new_barrel:
                        label = True
                        if user_input == "y":
                            self.user_card._card_content[i][j] -= 100
                            self.user_card._count -= 1
                        if user_input == "n":
                            print("У Вас было такое число в карточке! Вы проиграли!")
                            exit()
                    if self.computer_card._card_content[i][j] == new_barrel:
                        self.computer_card._card_content[i][j] -= 100
                        self.computer_card._count -= 1
            if not label and user_input == "y":
                print("У Вас не было такого числа в карточке! Вы проиграли!")
                exit()
            if self.computer_card._count == 0 and self.user_card._count == 0:
                print("Ничья вышла!")
                exit()
            if self.computer_card._count == 0:
                print("Вы проиграли, а компьютер выйграл")
                exit()
            if self.user_card._count == 0:
                print("Вы выйграли.")
                exit()


if __name__ == "__main__":
    u_card = Card()
    c_card = Card()
    g = Game(u_card, c_card)
    g.play_game()
