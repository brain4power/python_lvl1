# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random


def squared(input_list):
    return list(map(lambda x: x**2, input_list))


# print(squared([random.randint(-10, 10) for _ in range(10)]))

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
first = ['apple', 'orange', 'pear']
second = ['pear', 'persimmon']


def fruit_intersection(first_list, second_list):
    return [element for element in first_list if element in second_list]


print(fruit_intersection(first, second))


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4


def new_list(input_list):
    return [element for element in input_list if element % 3 == 0 and element >= 0 and not element % 4 == 0]


print(new_list([3, 4, -3, 12]))
