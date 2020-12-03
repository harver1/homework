'''Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.'''

n = int(input("Введите число: >"))

#  коряво, не красиво, можно запутаться
print(n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))

# через сложение
nn = int(str(n) + str(n))
nnn = int(str(nn) + str(n))
print(n + nn + nnn)

# через умножение
nn = int(str(n)*2)
nnn = int(str(n)*3)
print(n + nn + nnn)
