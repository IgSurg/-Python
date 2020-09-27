#1
import pygame

class TrafficLight:

    def __init__(self):
        self.WHITE = (255, 255, 255)
        self.GRAY = (125, 125, 125)
        self.GREEN = (0, 255, 64)
        self.YELLOW = (225, 225, 0)
        self.RED = (255, 0, 0)

        self.clr = [self.RED, self.YELLOW, self.GREEN, self.YELLOW]
        self.act_time = [2, 7, 2, 7]

    def switch_on(self):


        FPS = 60
        WIN_WIDTH = 120
        WIN_HEIGHT = 400

        pygame.init()
        clock = pygame.time.Clock()

        sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        # радиус и координаты круга
        r = WIN_WIDTH // 4
        x = WIN_WIDTH // 2
        y = WIN_HEIGHT // 2  # выравнивание по центру по вертикали

        k = 0

        while 1:
            sc.fill(self.GRAY)
            pygame.draw.circle(sc, self.WHITE, (x, y - 100), r)
            pygame.draw.circle(sc, self.WHITE, (x, y), r)
            pygame.draw.circle(sc, self.WHITE, (x, y + 100), r)

            for i in pygame.event.get():
                if i.type == pygame.QUIT: exit()

            if k == 0:
                pygame.draw.circle(sc, self.clr[k], (x, y - 100), r)
            elif k == 1 or k == 3:
                pygame.draw.circle(sc, self.clr[k], (x, y), r)
            elif k == 2:
                pygame.draw.circle(sc, self.clr[k], (x, y + 100), r)

            pygame.display.update()
            pygame.time.wait(self.act_time[k] * 1000)

            if k >= 3:
                k = 0
            else:
                k += 1

            clock.tick(FPS)

###########

a = TrafficLight()
a.switch_on()



# 2Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
#Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    _dens = 0.025
    _hei = 0.05

    def __init__(self,length, width):
        self._length = length
        self._width = width


    def count(self):
        return self._length * self._width * self._dens * self._hei


street_Lenina = Road(20,5000)
print(f'Требуется асфальта - {street_Lenina.count()} тонн')


#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе
# класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры
# класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        return (self.name+' '+self.surname)

    def get_total_income(self):
        return (sum (i for i in self._income.values()))



my_income = {'wage':100,'bonus':51}
a = Position('Иван','Иванов','менеджер', my_income)
print(a.get_full_name())
print(a.get_total_income())


# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
# PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


class Car:

    speed = 0
    direction = 'north'
    is_police = False
    def __init__(self, color, name):
        self.color = color
        self.name = name


    def go(self, speed):
        self.speed = speed
        print(f'Машина поехала со скоростью {self.speed} км/ч')

    def stop(self):
        self.speed = 0
        print(f'Машина остановилась')

    def turn(self, direction):
        self.direction = direction

    def show_speed(self):
        print(f'Скорость машины - {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        print(f'Скорость машины - {self.speed} км/ч')
        if self.speed > 60:
            print(f'Вы превышаете разрешенную скорость')


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость машины - {self.speed} км/ч')
        if self.speed > 40:
            print(f'Вы превышаете разрешенную скорость')

class PoliceCar(Car):
    is_police = True


t = TownCar('white','Mazda')
s = SportCar('red','Ferrari')
w = WorkCar('yellow','lorry')
p = PoliceCar('blue','ford')

s.show_speed()
s.go(400)
s.turn('west')
print(s.direction)
print(s.is_police)

t.go(100)
t.show_speed()

print(p.is_police)


#5 Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
   def draw(self):
       Stationery.draw(self)
       print(f'Инструмент отрисовки {self.title}')

class Pencil(Stationery):
   def draw(self):
       Stationery.draw(self)
       print(f'Инструмент отрисовки Pencil')

class Handle(Stationery):
   def draw(self):
       Stationery.draw(self)
       print(f'Инструмент отрисовки Handle')



p = Pen('Pen')
c = Pencil('Red Pencil')
h = Handle('Purple')

p.draw()
c.draw()
h.draw()





























































































































































































































