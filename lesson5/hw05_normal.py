# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import hw05_easy as easy
import os


def cls(): print("\n" * 100)


def status(add_path):
    print("Вы тут: " + os.path.join(os.getcwd()) + add_path)


menu_dict = {
    1: "Перейти в папку",
    2: "Просмотреть содержимое текущей папки",
    3: "Удалить папку",
    4: "Создать папку",
    5: "Выход"
}


def menu():
    for item in list(menu_dict.keys()):
        print("{}. {}".format(item, menu_dict[item]))


def my_view(input_path):
    if input_path == "":
        path = "."
    else:
        path = os.path.join(os.getcwd()) + input_path
    if not next(os.walk(path))[1] and not next(os.walk(path))[2]:
        print("Папка пуста!")
    else:
        if next(os.walk(path))[1]:
            print("Папки: {}".format(next(os.walk(path))[1]))
        if next(os.walk(path))[2]:
            print("Файлы: {}".format(next(os.walk(path))[2]))


def move_to_dir():
    pass


add_path = ""
exit_program = False
while not exit_program:
    status(add_path)
    menu()
    try:
        user_choice = int(input("Выберите пункт: "))
    except ValueError:
        print("Что-то не то выбрали, до свидания!")
        exit()
    if user_choice not in range(1, 6):
        print("Выбор неверен. До свидания, попробуйте позже еще раз.")
        exit()
    if user_choice == 1:
        user_input = str(input("Введите имя папки, в которую перейти: "))
        if add_path == "":
            path = "."
        else:
            path = os.path.join(os.getcwd()) + add_path
        if user_input in next(os.walk(path))[1]:
            add_path = add_path + "/" + user_input
        else:
            cls()
            print("Такой папки тут нет")
    if user_choice == 2:
        cls()
        my_view(add_path)
    if user_choice == 3:
        user_input_dir_name = str(input("Введите имя папки, котурую надо удалить: "))
        cls()
        easy.del_dir(os.path.join(os.getcwd(), add_path + user_input_dir_name))
    if user_choice == 4:
        user_input_dir_name = str(input("Введите имя папки, котурую надо создать: "))
        cls()
        easy.make_dir(os.path.join(os.getcwd(), add_path + user_input_dir_name))
    if user_choice == 5:
        exit_program = 1
        cls()
        print("До скорых встреч!")
