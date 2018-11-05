# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    first = 1
    second = 1
    number = 1
    while number != n:
        number += 1
        second += first
        first = second - first
    fibo_cut = []
    for i in range(n, m + 1):
        fibo_cut.append(first)
        second += first
        first = second - first
    return fibo_cut

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    if not origin_list:
        return origin_list
    pivot = origin_list.pop()
    left_array = list(filter(lambda x: x < pivot, origin_list))
    right_array = list(filter(lambda x: x >= pivot, origin_list))
    return sort_to_max(left_array) + [pivot] + sort_to_max(right_array)


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(input_func, input_list):
    output_list = []
    for element in input_list:
        if input_func(element):
            output_list.append(element)
    return output_list

#только эта функция возвращает список, а не объект. Как сделать так, чтобы она возвращала объект, а после применения
# list() к этому объекту получался список?


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# решаем по по критерию параллелограмма: диагонали пересекаются и точкой пересечения делятся пополам


def middle_of_diagonal(x_middle, y_middle):
    return [round(x_middle, 2), round(y_middle, 2)]


def parallelogram_check(x1, y1, x2, y2, x3, y3, x4, y4):
    if [x1, y1] == [x2, y2] or [x1, y1] == [x3, y3] or [x1, y1] == [x4, y4] or [x2, y2] == [x3, y3]\
            or [x2, y2] == [x4, y4] or [x3, y3] == [x4, y4]:
        return "Нет, не являются"
    elif middle_of_diagonal((x1 + x4)/2, (y1 + y4)/2) == middle_of_diagonal((x2 + x3)/2, (y2 + y3)/2)\
        or middle_of_diagonal((x1 + x2)/2, (y1 + y2)/2) == middle_of_diagonal((x4 + x3)/2, (y4 + y3)/2)\
        or middle_of_diagonal((x1 + x3)/2, (y1 + y3)/2) == middle_of_diagonal((x2 + x4)/2, (y2 + y4)/2):
        return "Да, являются"
    else:
        return "Нет, не являются"


print(parallelogram_check(1, 3, 3, 3, 2, 1, 4, 1))
print(parallelogram_check(2, 1, 4, 1, 2, 1, 4, 1))
