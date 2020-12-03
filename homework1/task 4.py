number = int(input("Введите целое число: > "))
max_num = 0
some_num = 0

while max_num < number:
    number = number // 10
    if max_num < number % 10:
        max_num = number % 10

#  тоже самое, но сравнение с конкретной переменной, а не выражением

# while number !=0:
#     number = number // 10
#     some_num = number % 10
#     if max_num < some_num:
#         max_num = some_num

print(f'Самая большая цифра в введенном вами числе это - {max_num}')
