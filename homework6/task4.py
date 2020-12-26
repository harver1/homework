# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
# метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car():

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала со скоростью - {self.speed}')

    def stop(self):
        print(f'Машина{self.name} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина {self.name} повернула на {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобился {self.speed}')


class TownCar(Car):

    def __init__(self, name, color, speed):
        Car.__init__(self, name, color, speed)

    def show_speed(self):
        if self.speed > 60:
            print('превышение скорости, ограничение 60')
        else:
            print('Скоростной режим не нарушается')


class SportCar(Car):
    pass


# так как атрибуты у всех классов неизменны и цепляются из родительского, можно ли не переопределять параметры?
class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('превышение скорости, ограничение 40')
        else:
            print('Скоростной режим не нарушается')


class PoliceCar(Car):
    pass


town = TownCar('Городской автомобиль', 'Красный', 70)
sport = SportCar('Спортивный автомобиль', 'Желтый', 200)
work = WorkCar('Рабочий автомобиль', 'Белый', 60)
police = PoliceCar('Полицейский автомобиль', 'Голубой', 220, True)


print(f'{town.name} '
      f'скорость - {town.speed} '
      f'цвет - {town.color} '
      f'это машина полиции? - {town.is_police}')
town.go()
town.show_speed()
town.speed = 50
town.show_speed()
town.turn('влево')
town.stop()

print(f'\n{sport.name} '
      f'скорость - {sport.speed} '
      f'цвет - {sport.color} '
      f'это машина полиции? - {sport.is_police}')
sport.go()
sport.show_speed()
sport.turn('вправо')
sport.stop()

print(f'\n{work.name} '
      f'скорость - {work.speed} '
      f'цвет - {work.color} '
      f'это машина полиции? - {work.is_police}')
work.go()
work.show_speed()
work.turn('назад')
work.stop()

print(f'{police.name} '
      f'скорость - {police.speed} '
      f'цвет - {police.color} '
      f'это машина полиции? - {police.is_police}')
police.go()
police.show_speed()
police.turn('разворот')
police.stop()
