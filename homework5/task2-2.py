# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

file = open(file="task2.txt", mode='rt', encoding='UTF8')

# количество строк
counter = len([i for i in file])

# вертаемся назад, считаем количество слов в файле добавляем в список
file.seek(0)
ttt = []
for line in file:
    ttt.append(len(line.split()))

file.close()


