# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в
# новый текстовый файл.

translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

# Открываем файл и считываем его
with open(file='task4.txt', mode='rt', encoding='UTF-8') as task4:
    text = task4.readlines()

# список для нового блока строк
list_input = []

# меняем английские на русские и добавляем в список который будем записывать в новый файл
param = [lst.split() for lst in text]
for lst in param:
    lst[0] = translate.get(lst[0])
    list_input.append(' '.join(lst))  # добавляем строки в список
    # list_input.append(' '.join(lst) + '\n') # добавляем в список строки с символом \n



with open(file='task4_input.txt', mode='w+', encoding='UTF-8') as task4_input:
    task4_input.write('\n'.join(list_input))  # Если список не содержит \n
    # task4_input.writelines(list_input) # Если в списке строки содержат символ \n
    task4_input.seek(0)
    print(task4_input.read())

