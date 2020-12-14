# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# через ф строку
# def my_func(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{value}', end=' ')

# без ф строки
def my_func(**kwargs):
    for key, value in kwargs.items():
        print(value, end=' ')


my_func(name='Иванушка', last_name='Иванов', year=1111, city='Сказочный', mail='ivan@durak.tk', phone=123)