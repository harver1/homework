# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

# записываем числа в файл, если файла нету создастся. Режим выбран w, тоесть каждый запуск и ввод новых чисел будет
# затирать старые.
with open(file='task5.txt', mode='w+', encoding='UTF-8') as file:
    file.write(input('Введите числа через пробел') + '')  # пробел в конце, чтобы в режиме
    # дозаписи(если вдруг потредуется) первое число нового ввода не сливалось с последним числом

# Вертаем курсор в начало, считываем числа с файла, считаем сумму, выводим на экран.
    file.seek(0)
    numbers = [int(i) for i in file.read().split()]

    print(sum(numbers))

