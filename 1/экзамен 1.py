# Теория!

# 1 - С

# 2 - A

# 3 - A

# 4 - B

# 5 - B

# 6 - B


# Задание 1
def main(text: int) -> str:
    match text:
        case 1:
            print("Один")
        case 2:
            print("Два")
        case 3:
            print("Три")
        case 4:
            print("Четыри")
        case 5:
            print("Пять")
        case _:
            print("Ошибка")

main(1)

# Задание 2
lst = [i for i in range(1, 20) if i % 2 == 0]
print(lst)

# Задание 3

#Создание source имя_окружения/bin/activate

#Активация - pip install -m venv venv



# Задание 6
l = lambda a, b: a ** b
print(l(22, 2))

# Задание 7
with open("../log.txt", "a", encoding='utf-8') as e:
    e.write("Hello World")

# Задание 5
def main(a: int, b: int) -> int:
    return a + b

print(main(2, 3))

# Задание 8
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ll = list(filter(lambda a: a % 2 == 0, numbers))
print(ll)

# Задание 9
lst = [i ** 2 for i in range(1, 10)]
print(lst)

# Задание 10
def text(word1: str, word2: str):
    return word1 + word2
print(text("Привет", "Мир"))





