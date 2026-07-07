# def my_sum(*args):
#     result = 0
#     for arg in args:
#         result += arg
#     return result
#
# lst_1 = [1, 2, 3, 4, 5]
# lst_2 = [3, 4, 8, 2]
#
# print(my_sum(*lst_1, *lst_2))

# Как создать виртуальное окружение

# python -m venv myvenv

# Теория №1

# 1-int
# 2-float
# 3-Bool
# 4-str
# 5-list
# 6-tuple
# 7-set
# 8-None
# 9-frozenset
# 10-dict

# Теория №2

# Тип данных list и tuple отличаються от того что, list Изменяемый, Индексация доступна в list и typle, также обоим доступна срезы строк. Также отличаються от создание list[] typle()


# Теория №3
#set() - Это тип данных пайтон

#Теория №4
# list[] - Изменяемый
# dict{} - Изменяемые только ключи

# Теория №2 #1
# Ответ - B - list[]


# Теория №2 #2
# Ответ - С - Строки поддерживают срезы, строки поддерживают индексацию тоже


# Теория №2 #3
# Ответ - А - def func(*args):

# Теория №2 #5
# __init__() - Это Конструктор для инициализации обьекта после его создание

# Теория №3 #1
lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
result = lst_1 + lst_2
print(result)

# Теория №3 #2
lst = [1, 2, 3, 4, 5]
user_input = int(input("Введите чтото: "))

if user_input in lst:
    print("Имееться")
else:
    print("Нету")

# Теория №3 #3
dct = {
    "a": 1,
    "b": 2,
    "c": 3
}
result = dct["a"]
print(result)

# Теория №3 #5
class MyClass:
    pass
class ClassP(MyClass):
    pass



# Теория №5
# Абстракция
# Полиморфизм
# Наследование
# Инкапсуляция
# Композиция

# Практика №1
lst = [5, 3, 6, 3, 1, 8]
ll = list(map(lambda x: x ** 2, lst))
print(ll)

# Практика №2
world = "Python"
print(world[::-1])

# Практика №3
def min_max_diference(numbers):
    if len(numbers):
        print(f"Максимальное число:", max(numbers))

    if len(numbers):
        print("Минимальное число:", min(numbers))


print(min_max_diference([1, 2, 3, 4, 5]))

# Практика №5
class AirPort:
    def __init__(self):
        self.passengers = []

    def check_in(self, name):
        if name not in self.passengers:
            return "Такого пасажира нет"
            self.passengers.append(name)
        else:
            return "Такой пасажир уже есть"

    def check_out(self, name):
        if name in self.passengers:
            self.passengers.remove(name)
            return "Пассажир удален"

    def list_passengers(self):
        return f"Список пасажиров: {self.passengers}"

airport = AirPort()
print(airport.check_in("Adam"))
print(airport.check_in("Rasul"))

airport.list_passengers()
airport.check_out("Rasul")
airport.list_passengers()
print(airport.list_passengers())




