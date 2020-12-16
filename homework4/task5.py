# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


# функция перемножения 2 чисел
def multiplication(a, b):
    return a*b


my_list = [el for el in range(10, 1001) if el % 2 == 0]

# используем reduce для вычисления произведения всех элементов сформированного списка
rezult = reduce(multiplication, my_list)  # какое то ужасно большое число
print(rezult)

