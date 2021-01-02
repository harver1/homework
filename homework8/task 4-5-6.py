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

class WareHouse():

    _registry = {}

    def __init__(self):
        self._box = _registry

# Метод для ручного добавления на склад
    @classmethod
    def manual_input(cls):
        try:
            name = input("введите нименование")
            quantity = int(input("введите количество"))
            price = int(input("введите цену"))
            my_dict = {name: {'name': name, 'quantity': quantity, 'price': price}}
            cls._registry.update(my_dict)
        except:
            return print(f'Где то вы напутали')
            # return f'Где то вы напутали'

# метод для добавления объектов на склад
    @classmethod
    def reception(cls, obj):
        my_dict = {obj.name: {'name': obj.name, 'quantity': obj.quantity, 'price': obj.price }}
        cls._registry.update(my_dict)

# метод для перемещения со склада в другой отдел
    @classmethod
    def move(cls, name):
        if name in cls._registry.keys():
            print(f'{cls._registry.pop(name)} перемещен в другой отдел')
            # print(f'удален со склада и перемещен {cls._registry.get(name)} в другой отдел')
            # cls._registry.pop(name)
        else:
            print (f'такого на складе нету')

class Equipment():

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


class Printer(Equipment):

    _my_type = 'printer'

    def __init__(self, name, quantity, price, color):
        # self.my_type = my_type
        self.color = color
        super().__init__(name, quantity, price)
        self.dict = {'name': name, 'quantity': quantity, 'price': price }


class Scanner(Equipment):

    _my_type = 'scanner'

    def __init__(self, name, quantity, price, rezolution):
        # self.my_type = my_type
        self.rezolution = rezolution
        super().__init__(name, quantity, price)
        self.dict = {'name': name, 'quantity': quantity, 'price': price }

class Xerox(Equipment):

    _my_type = 'Xerox'

    def __init__(self, name, quantity, price, speed):
        # self.my_type = my_type
        self.speed = speed
        super().__init__(name, quantity, price)
        self.dict = {'name': name, 'quantity': quantity, 'price': price}


# создаем объекты
t = WareHouse
print(t._registry)  # склад пуст тк ничего не добавляли

scan = Scanner('Epson', 2, 10, 1200)
printer = Printer('Canon', 5, 10, 3)
xeroks = Xerox('hp', 3, 5, 100)

# методы добавления объектов на склад
t.reception(scan)
t.reception(printer)
t.reception(xeroks)

# проверим что изменилось
print(t._registry) # объекты на склад добавляются

# перемещаем в другой отдел
t.move('Canon')
print(t._registry)  # объект из словаря удалился, видимо перемещение произошло успешно)

# Ручное добавление объекта на склад, с проеркой вводимых значений
t.manual_input()
print(t._registry)