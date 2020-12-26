# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом
# премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker():

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Имя - {self.name}, Фамилия - {self.surname}'

    def get_total_income(self):
        total = self._income['wage'] + self._income['bonus']
        return f'Доход - {total}'
        # return f'Доход - {sum(self._income.values())}'


ivan = Position('Иван', 'Иванов', 'Сотрудник', 20, 10)
tom = Position('Tom', 'Jhonson', 'manager', 30, 15)

print(ivan.name, ivan.surname, ivan.position, ivan._income)
print(ivan.get_full_name())
print(ivan.get_total_income())

print(tom.name, tom.surname, tom.position, tom._income)
print(tom.get_full_name())
print(tom.get_total_income())