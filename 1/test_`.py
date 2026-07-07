class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Имя: {self.name} Лет: {self.age}"

test = Test("jj", 13)
print(test)