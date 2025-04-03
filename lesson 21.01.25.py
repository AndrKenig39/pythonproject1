# обернуть function1 в класс( сделать методом класса, создать объект и тремя способами вызвать метод)



class Function1:
    def __init__(self,num1:int,num2:int):
     self.num1 = num1
     self.num2 = num2
     print(num1,num2)
obj1Function1 = Function1(4,9)
(obj1Function1. __dict__)
num1 = 4
num2 = 6
obj2Function1 = Function1(4,6)
(obj2Function1.__dict__)
n1 = 5
n2 = 8
obj3Function1 = Function1(5,8)
(obj3Function1.__dict__)



# вызов функции параметры передаём напрямую
# имя параметра и имя переменной при вызове функции могут отличаться а работать она будет
# function1(3,7)
# # вызов функции передаём параметры через переменные
# num1, num2 = 4,6
# function1(num1,num2)
# # вызов функции параметры передаём через переменные с другим именем
# n1, n2 = 2,7
# function1(n1,n2) # function1(2,7)
"""
Наследование - принцип объектно-ориентированого программирования есть класс родительский и дочерний

пример
человек это родительский класс, а студент будет дочерним
супер класс родитель а ребенок дочерний
"""



class Human:
    def __init__(self, full_name, age, gender):

        self.full_name = full_name
        self.age = age
        self.gender = gender

        print(f"Конструктор родительского класса")


class Student(Human): # дочерний класс, а Human родительский(суперкласс)

    def __init__(self,full_name, age, gender, university, course, faculty):

        # self.full_name = full_name # переменные из род класса к которым имеет доступ
        # self.age = age
        # self.gender = gender
        super().__init__(full_name, age, gender) # вызов родительского конструктура с параметрами
        print()
        self.university = university # атрибуты студента
        self.course = course
        self.faculty = faculty

        print(f"Конструктор дочернего класса")

class Student1(Human):
    def __init__(self,obj1Human,university, course, faculty):
        # вызов родительского конструктора передаём 3 параметра имя объекта.атрибут
        super().__init__(obj1Human.full_name, obj1Human.age, obj1Human.gender)
        self.university = university
        self.course = course
        self.faculty = faculty
        print(f"Конструктор дочернего класса Student1")

"""
Student2 дочерний класс Конструктор может принимать разное количество параметров
перегрузка метода(конструтора) когда можно создавать объект с разным количеством параметров
"""
class Student2(Human):
    # val3=None 2 1 # параметры которые не обязательно передавать
    def __init__(self,university, course, faculty, val1=None, val2=None, val3=None):
        self.university = university   # переменные это
        self.course = course
        self.faculty = faculty
        #  если мы передали объект в параметр val1
        # если создали человека, а он решил стать студентом

        if isinstance(val1,Human):
            super().__init__(val1.full_name, val1.age, val1.gender)
        elif isinstance(val1, str):
            super().__init__(val1, val2, val3)



obj1Human = Human("Fedorov Mikhail Sergeevich",19,1)

print(obj1Human.__dict__) # вывод информации об объекте

obj1Student = Student("Fedorov Mikhail Sergeevich",21,1,"Hogvards",
                      1,"sliserin")

print(obj1Student.__dict__)

obj2Student = Student1(obj1Human, "Hogvards",1, "Sliserin")
print(obj2Student.__dict__)

obj2Human = Human("Fedorov Mikhail Sergeevich", 31, 1) # создали его человеком
obj3Student = Student2("БФУ", 2, "Информатика", obj2Human) # сделали его студентом
print(obj3Student.__dict__)
print()
obj4Student = Student2("БФУ", 2, "Информатика", "Alexandr", 41, 1)
print(obj4Student.__dict__)