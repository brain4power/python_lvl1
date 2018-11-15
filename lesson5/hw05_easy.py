# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil


def make_dir(dir_path):
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')
    else:
        print("Папка создана!")


def make_dir_1_9():
    for idx in range(1, 10):
        dir_path = os.path.join(os.getcwd(), 'dir_' + str(idx))
        make_dir(dir_path)


def del_dir(dir_path):
    try:
        os.rmdir(dir_path)
    except FileNotFoundError:
        print('Такая директория не существует')


def del_dir_1_9():
    for idx in range(1, 10):
        dir_path = os.path.join(os.getcwd(), 'dir_' + str(idx))
        del_dir(dir_path)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def dir_list():
    return print(next(os.walk('.'))[1])


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_current_file():
    shutil.copyfile(__file__, __file__ + '.copy.py')

