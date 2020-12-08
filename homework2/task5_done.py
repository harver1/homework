#  5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
#  У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
#  значениями, то новый элемент с тем же значением должен разместиться после них.


my_list = [99, 50, 10]
number = int(input('Введите число: >'))

# Через циклы
while number > 0:
    for i in range(len(my_list)-1, -1, -1):
        if number == my_list[i]:
            my_list.insert(i+1, number)
            print(my_list)
            break
        elif number < my_list[i]:
            my_list.insert(i+1, number)
            print(my_list)
            break
    number = int(input('Введите число, для выхода введите 0 или отрицательное число: >'))

print(my_list)

# можно ли сделать так? По крайней мере результат подходит. А как посмотреть какой из объектов попал раньше в память,
# я пока не знаю
# while number > 0:
#     my_list.append(number)
#     my_list.sort()
#     my_list.reverse()
#     print(my_list)
#     number = int(input('Введите число, для выхода введите 0 или отрицательное число: >'))
#
# print(my_list)
