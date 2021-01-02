# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date():

    def __init__(self, some_date):
        self.some_date = some_date

    @classmethod
    def converter(cls, some_date):
        day, month, year = [int(i) for i in some_date.split('-')]
        # return day, month, year
        return f'{day}.{month}.{year}г.'

    @staticmethod
    def validation(some_date):
        day, month, year = [int(i) for i in some_date.split('-')]
        if day < 31 and month < 12 and 0 < year < 2100:
            return f'дата соответсвует параметрам'
        else:
            return f'Где то ошибочка'


print(Date.converter('12-01-15'))
print(Date.validation('12-01-15'))
print(Date.validation('34-01-15'))
dt = Date('12-02-15')

print(dt.converter('12-02-15'))
# print(Date.validation('12-01-15'))
# print(Date.validation('34-01-15'))
