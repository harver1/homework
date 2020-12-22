# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


# открываем файл на дозапись, если файл отсутсвует, то он будет создан
new_file = open(file='task1.txt', mode='at', encoding='UTF-8')
tmp = []


# записываем в файл построчно, после ввода каждой строки
while True:
    insert_line = input("Введите данные, для выхода ничего не вводите и нажмите enter : >")
    if insert_line == '':
        break
    new_file.write(insert_line + '\n')


# запись с помощью writelines
# while True:
#     insert_line = input("Введите данные, для выхода, ничего не вводите и нажмите enter : >")
#     if insert_line == '':
#         break
#     tmp.append(insert_line + '\n')
#
# new_file.writelines(tmp)


new_file.close()

