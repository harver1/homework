# Функция сложения(та же самая)
def my_func(text):
    lst = text.split()
    count = 0
    for i in range(len(lst)):
        try:
            lst[i] = int(lst[i])
            count += lst[i]
        except:
            return count, lst[len(lst)-1]
    return count


# реализация функцией а не циклом
def my_super_func():
    counter = 0
    while True:
        text = input('Введите числа через пробел')
        if text == 'd':
            break
        try:
            counter +=my_func(text)
        except:
            counter += my_func(text)[0]
            print(counter)
            # break    # если раскоментировать программа будет завершать работу по любому символу.
            if my_func(text)[1] != 'd':
                continue
            else:
                break
        print(counter)

my_super_func()