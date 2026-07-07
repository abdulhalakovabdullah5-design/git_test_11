# from abc import ABC, abstractmethod
#
#
# def simple_dicorator(func):
#     def wrapper():
#         print("Начало функции")
#         func()
#         print("Конец функции")
#     return wrapper
#
# @simple_dicorator
# def greet():
#     print("Привет")
#
# greet()
# greet()
#
# import time
#
# def times(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#
#     return wrapper
#
#
# @times
# def fr():
#     start_time = time.time()
#     for i in range(1, 1_000_000):
#         print(i)
#
#     end_time = time.time()
#     result_time = end_time - start_time
#     print(f"Цикл завершился: {result_time}")
#
# fr()


def greet_decoratot(func):
    def wrapper(*args):
        print("До начала функции")
        func(*args)
        print("Конец функции")
    return wrapper

@greet_decoratot
def greet(name, age, surname):
    print(f"Привет: {name} вам: {age} {surname}")

print(greet("Мовсар", 17))

