# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class MyZerodivision(Exception):

    def __init__(self, error=''):
        self.error = error

    def __str__(self):
        return f'{self.error}'


while True:
    number = int(input('Веедите первое число, для выхода введите 0 '))
    if number == 0:
        break
    number_2 = int(input('Веедите двторое число '))
    try:
        number_3 = number/number_2
        print(number_3)
    except ZeroDivisionError:
        print(MyZerodivision('К сожалению, делить на 0 нельзя('))