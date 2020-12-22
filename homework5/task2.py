# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

file = open(file="task2.txt", mode='rt', encoding='UTF8')

# считаем количество слов
count_str = len([i for i in file])

# тк файл уже прочитан циклом и курсор в конце, отматываем назад считаем и выводим количество слов в каждой строке
file.seek(0)
for line in file:
    print(f'в строке {line.strip()}, количество слов - {len(line.split())} шт.')


text = file.readlines()  # считываем строки из файла в переменную


#количество строк в файле
# count_str = len(text)
# print(count_str)

# количество слов с троке
# count_wrd = []
# for i in text:
#     t = i.split()
#     count_wrd.append(len(t))
#
# for i in range(1, len(text)+1):
#     print(f'на {i} строке, количество слов - {count_wrd[i-1]}')
#
#
#
# print("количество строк", count_str)
# print('количество слов в строках', count_wrd)
file.close()