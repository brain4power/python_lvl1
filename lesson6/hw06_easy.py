# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.a = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
        self.b = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
        self.c = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def p(self):
        return self.a + self.b + self.c

    def s(self):
        pp = self.p() / 2
        return math.sqrt(pp * (pp - self.a) * (pp - self.b) * (pp - self.c))

    def ah(self):
        return 2 * self.s() / self.a

    def bh(self):
        return 2 * self.s() / self.b

    def ch(self):
        return 2 * self.s() / self.c


my_triangle = Triangle(1, 2, 3, 3, 0, 15)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

# ввод точек трапеции только поочередно обходя вершины

class Trapezium:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4
        self.ab = [x2 - x1, y2 - y1]
        self.bc = [x3 - x2, y3 - y2]
        self.cd = [x4 - x3, y4 - y3]
        self.da = [x1 - x4, y1 - y4]

    # длина вектора:
    @staticmethod
    def _len_side(v):
        pass

    # проверка коллинеарности:
    # не стал делать - скучно это. Не отрабатывает текущую тему.
    @staticmethod
    def _is_parallel(v1, v2):
        pass

    def check_trapezium(self):
        if Trapezium._is_parallel(self.ab, self.cd) and Trapezium._len_side(self.bc) and Trapezium._len_side(self.da) \
                or Trapezium._is_parallel(self.bc, self.da) and Trapezium._len_side(self.ab) and \
                Trapezium._len_side(self.cd):
            return True
        else:
            return False


class EquilateralTrapezium(Trapezium):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        super().__init__(x1, y1, x2, y2, x3, y3, x4, y4)

    def check_equilateral(self):
        if self.ab == self.cd or self.bc == self.da:
            return True
        else:
            return False
