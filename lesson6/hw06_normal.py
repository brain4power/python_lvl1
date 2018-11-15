# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class School:
    def __init__(self):
        self._school_classes = []
        self._lessons_and_teachers = {}

    def add_school_class(self, new_school_class):
        if isinstance(new_school_class, SchoolClass):
            if new_school_class not in self._school_classes:
                self._school_classes.append(new_school_class)
            else:
                print("Такой класс уже есть в школе")
        else:
            print("Ошибка! передаваемы класс должен быть классом SchoolClass")

    @property
    def get_all_classes(self):
        result = []
        for each in self._school_classes:
            result.append(each.class_name)
        return result

    def add_lesson(self, new_lesson):
        if isinstance(new_lesson, Lesson):
            if new_lesson not in self._lessons_and_teachers:
                self._lessons_and_teachers[new_lesson] = ""
            else:
                print("Такой предмет в школе уже существует")
        else:
            print("Ошибка! Передаваемый предмет должен быть классом Lesson")

    def add_lesson_and_teacher(self, for_lesson, new_teacher):
        if isinstance(new_teacher, Teacher) and isinstance(for_lesson, Lesson):
            self._lessons_and_teachers[for_lesson] = new_teacher
        else:
            print("Ошибка! Передаваемые предмет и преподаватель должны быть классами Lesson & Teacher")


class SchoolClass:
    def __init__(self, class_name):
        self.class_name = class_name
        self._lessons_and_teachers = {}
        self._pupils = []

    def add_pupil(self, new_pupil):
        if isinstance(new_pupil, Pupil):
            if new_pupil not in self._pupils:
                self._pupils.append(new_pupil)
                new_pupil._class = self
            else:
                print("Такой ученик уже есть в этом классе!")
        else:
            print("Ошибка! Передаваемый ученик должен быть классом Pupil")

    @property
    def get_all_pupils(self):
        result = []
        for each in self._pupils:
            result.append(each.full_name)
        return result

    def add_lesson_and_teacher(self, add_lesson, add_teacher, school_for_check):
        if isinstance(school_for_check, School) and isinstance(add_lesson, Lesson):
            if add_teacher:
                if not isinstance(add_teacher, Teacher):
                    print("передаваемый учитель должен быть объектом Teacher или отсутствовать")
                    exit(function)
            if add_lesson in school_for_check._lessons_and_teachers:
                if add_teacher:
                    if school_for_check.add_lesson(add_lesson) == add_teacher:
                        self._lessons_and_teachers[add_lesson] = add_teacher
                    else:
                        print("Учитель некорректно назначен на предмет в школе")
                        exit(function)
                else:
                    self._lessons_and_teachers[add_lesson] = add_teacher
            else:
                print("Сначала добавьте предмет в Школу")
        else:
            print("Ошибка! Передаваемые предмет и школа должны быть классами Lesson & School")

    @property
    def get_all_teachers_of_class(self):
        result = []
        for each in self._lessons_and_teachers:
            if self._lessons_and_teachers[each]:
                result.append(self._lessons_and_teachers[each])
        return result

    @property
    def get_all_lessons(self):
        return self._lessons_and_teachers.keys()


class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self._father = None
        self._mother = None

    @property
    def full_name(self):
        return self.name + " " + self.surname

    def set_parent(self, parent_type, parent_obj):
        if isinstance(parent_obj, Human):
            if parent_type == "father":
                self._father = parent_obj
            elif parent_type == "mother":
                self._mother = parent_obj
            else:
                print("Ошибка передаваемого типа родителей")
        else:
            print("Ощибка! Родитель должен быть объектом класса Human")

    @property
    def get_parents(self):
        return "Отец: {}, мать: {}".format(self._father.full_name, self._mother.full_name)


class Pupil(Human):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self._class = None

    @property
    def get_all_lessons_of_pupil(self):
        try:
            return self._class.get_all_lessons
        except AttributeError:
            print("Ученик не назначен в класс")


class Teacher:
    def __init__(self, teacher_name):
        self.teacher_name = teacher_name


class Lesson:
    def __init__(self, lesson_name):
        self.lesson_name = lesson_name


if __name__ == "__main__":
    p1 = Pupil("Женя", "Овчинников")
    p2 = Pupil("Катя", "Безбожных",)
    p3 = Pupil("Олег", "Игнатов")
    class1 = SchoolClass("1F")
    SchoolClass.add_pupil(class1, p1)
    # print(class1.get_all_pupils)
    # print(p1.get_all_lessons_of_pupil)

