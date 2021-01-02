# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
# на склад и передачу в определенное подразделение компании. Для хранения данных
# о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
# любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных
# на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.


class Store():

    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_dict = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            names = input(f'Введите наименование ')
            prices = int(input(f'Введите цену за ед '))
            numbers = int(input(f'Введите количество '))
            unique = {'Модель устройства': names, 'Цена за ед': prices, 'Количество': numbers}
            self.my_dict.update(unique)
            self.my_store.append(self.my_dict)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        q = input(f'Для выхода введите Q')
        if q == 'Q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
        else:
            return Store.reception(self)


class Printer(Store):
    def to_print(self):
        return f'to print {self.numb} times'


class Scanner(Store):
    def to_scan(self):
        return f'to scan {self.numb} times'


class Copier(Store):
    def to_copier(self):
        return f'to copier {self.numb} times'


first = Printer('hp', 2000, 5, 10)
second = Scanner('Canon', 1200, 5, 10)
third = Copier('Xerox', 1500, 1, 15)
print(first.reception())
# print(second.reception())
# print(third.reception())
