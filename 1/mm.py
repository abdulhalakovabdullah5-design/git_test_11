# 1 - Виртуальное окружение позволяет создать отдельную копию которая не влияет на другие проекты

# 2 -  Правила 1 - 4 - Пробела, 2 - Длина строки - 79 символов не должно превышать, 3 - Отступы

# 3 - lambda отличается от обычной функции, lambda работает без return :-Двое точие работает как return, и функция lambda создаеться с переменой, ниже приведу пример!

# Пример из обычной функци 👇
def main(a, b):
    return a + b

print(main(2, 3))

# Пример с lambda 👇

main = lambda a, b: a + b
print(main(1, 2))


# 4

# Мод - w - Запись файла если файла нет то создает!
# Мод - r - Читает содержимое файла!
# Мод - a - Дописывает файл!
# Мод - x - Создает файл!


# 5
#print("Возможные действие: (+, -)")
#while True:
    #try:
#        user_menu = input("Выберите действие: (+|-|/): ")

#        if user_menu == "+":
 #           user_input_1 = float(input("Введите первое число: "))
  #          user_input_2 = float(input("Введите второе число: "))
   #         result = user_input_1 + user_input_2
    #        print(f"Результат сложение: {result}")

     #   elif user_menu == "-":
      #      user_input_1 = float(input("Введите первое число: "))
       #     user_input_2 = float(input("Введите второе число: "))
        #    result = user_input_1 - user_input_2
         #   print(f"Результат: {result}")

        #elif user_menu == "/":
         #   user_input_1 = float(input("Введите первое число: "))
          #  user_input_2 = float(input("Введите второе число: "))
#
 #           result = user_input_1 / user_input_2
  #          print(f"Результат: {result}")

    # Исключение ZeroDivisionError сработает если пользователь хочет делить число на 0

    # except ZeroDivisionError - деление на ноль!
    # except ValueError - Если пользователь вел строку а не число!
    # else Сработает если в блоку try не было ошибок
    # try except используется для обработки ошибок!


result = []
lst = [i for i in range(1, 5+1)]
result.append(lst)
print(result)

# 6
# оператор == сравнивает значение
# оператор is проверяет одинаковое значение или нет

# 7

# конструкция with при октрытие файла автоматические закрывает файл

# with open("main.py", "w", encoding='utf-8') as e:
#     e.write("uu")
#     print(e)

# 8
# user_name = input("Введите имя: ")
# user_age = int(input("Введите возраст: "))

# print(f"Привет {user_name} тебе через 5 лет будет {user_age + 5} лет")

# 9

lst = ['c#', 'java', ['rust', 'python'], 'js']

n = lst[2][1]
print(n)

# 10

total_sum = 0
while True:
    user_input = int(input("Введите число или 0 для выхода: "))

    total_sum += user_input

    if user_input == 0:
        print("Пока")
        break
print(f"Сумма: {total_sum}")


# 11

print("Возможные действие + - * /")

while True:
    user_input = input("Ввыберите действие: ")

    match user_input:
        case "+":
            user_input_1 = int(input("Введите первоe число: "))
            user_input_2 = int(input("Введите второе число: "))

            result = user_input_1 + user_input_2
            print(f"Результат: {result}")

        case "-":
            user_input_1 = int(input("Введите первое число: "))
            user_input_2 = int(input("Введите второе число: "))

            result = user_input_1 - user_input_2
            print(f"Результат: {result}")
        case "*":
            user_input_1 = int(input("Введите первое число: "))
            user_input_2 = int(input("Введите второе число: "))

            result = user_input_1 * user_input_2
            print(f"Результат: {result}")

        case "/":
            user_input_1 = int(input("Введите перво число: "))
            user_input_2 = int(input("Введите второе число: "))

            result = user_input_1 / user_input_2
            if result % 2 == 0:
                print("Ошибка!")
            else:
                print(f"Результат: {result}")

        case _:
            print("Ошибка!")



# 12

