# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    if a < b and a < c:
        return b + c
    elif b < a and b < c:
        return a + c
    else:
        return a + b
print(my_func(12, 7, 9))


# тоже самое с использованием встроенных функций и намного короче
def my_func1(*args):
    return sum(args) - min(args)
# print(my_func1(12, 7, 9))


# Просто для тренировки
# def my_func2(*args):
#     lst = list(args)
#     lst.remove(min(lst))
#     return sum(lst)
#
# print(my_func2(1,5,6))


