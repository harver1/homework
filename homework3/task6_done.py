# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


#реализация функции для 1 слова
def int_func(word):
    return word.capitalize()

a1 = 'ben'
a2 = 'tom'
print(int_func(a1))
print(int_func(a2))

# функция для строки
def my_func(letter):
    text = letter.split()
    for i in range(len(text)):
        text[i] = int_func(text[i])
    letter = ' '.join(text)
    return letter

text = 'name word city country abc cd e a asdad gfdg fgh'
text1 = 'python can be easy'
print(my_func(text))
print(my_func(text1))

