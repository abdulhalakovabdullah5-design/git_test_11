def main(n):
    nums = []
    for i in n:
        if i % 2 == 0:
            nums.append(i)

        return nums

main([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l = [i for i in lst if i % 2 == 0]
print(l)

def main(lst: list):
    return [i for i in lst if i % 2 == 0]

main([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def main(a, b):
    return a + b

print(main(1, 2))

main = lambda: "Abdullah"
print(main())

main = lambda a, b: a + b
print(main(1, 3))

main = lambda a, b: a - b
print(main(4, 1))

main = lambda a, b: a / b
print(main(6, 2))

main = lambda a, b: a ** b
print(main(3, 55))

main = lambda a, b: a % b
print(main(3, 4))


# map() - Применяет  наше выражение x ** 2  к нашим элементам
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = list(map(lambda x: x ** 2, lst))
print(a)


# filter() - Будет оставлять в списке только то что проходит по нашему выражению
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = list(filter(lambda x: x ** 2, lst))
print(a)


# reduce() - Складывает послудуюшщие элементы из списка!
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = list(filter(lambda x: x ** 2, lst))
print(a)



lst = [1, 2, 3, 4, 5]
n = list(map(lambda a: a ** 2, lst))
print(n)