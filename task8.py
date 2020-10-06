
#1 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
# структуры на реальных данных.

from datetime import datetime

class Data:

    def __init__(self, str):
        self.str = str
        pass

    def __str__(self):
        return str(self.str)

    @classmethod
    def to_int(cls, str):
        dline = datetime.strptime(str, "%d-%m-%Y")
        d = dline.day
        m = dline.month
        y = dline.year
        cls.d = d
        cls.m = m
        cls.y = y
        return d, m, y


    @staticmethod
    def to_valid(param1, param2, param3):
        if (param1 in range(1,31)) and (param2 in range(1,12)):
            return True
        else:
            return False



s = "15-06-2020"
dat = Data(s)

print(dat)
print(dat.to_int(s))
print(dat.d)

x,y,z = dat.to_int(s)
print('данные ',x,y,z)
print(dat.to_valid(x,y,z))

##############################################
#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    try:
        pass
#        x = int(input('Введите числитель:'))
#        y = int(input('Введите знаменатель:'))
#        if y == 0:
#            raise MyError('Знаменатель не может быть равен нулю')
    except MyError as err:
        print(err)
    else:
        break
######################################################
#7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
#методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
#и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex:
    def __init__(self, real, mnim):
        self.z = complex(real, mnim)

    def __str__(self):
        return str(f'{self.z.real} + {self.z.imag} j')


    def __mul__(self, other):
        r = self.z.real * other.z.real - self.z.imag * other.z.imag
        m = self.z.imag * other.z.real + self.z.real * other.z.imag
        return Complex(r,m)

    def __add__(self, other):
        return Complex((self.z.real + other.z.real),(self.z.imag + other.z.imag))


a = Complex(2,2)
b = Complex(3,4)
print(a + b)
print(a * b)

################################################
#3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
#Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
#Класс-исключение должен контролировать типы данных элементов списка.

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt
"""

a = []
while True:
    try:
        x = input('Введите натуральное число либо нажмите Enter, чтобы прекратить:')
        if x == '': break
        if x.isnumeric():
            print('numeric ',x)
            a.append(int(x))
        elif x[0] == '-':
            if x[1:].isnumeric():
                print('negative - ',x[1:])
                a.append(int(x))
        else:
            raise MyError('Ты что вводишь? Это не цифры. Смотреть надо...')

    except MyError as err:
        print(err)

print(a)

"""

#####################################################
#4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

from datetime import datetime

class Depot:
    def __init__(self, title):
        self.title = title
        self.lists = {}
        self.give_lists = {}

    def take_to_depot(self, equipment):
# внесение в словарь название оборудования, серийный номер и время передачи на склад
        t = datetime.now()
        self.lists.update({equipment.serial_number:[equipment.title, self,t]})
        print('На склад '+self.title+' получено оборудование:'+ '' +equipment.title+' ,серийный номер - '+ str(equipment.serial_number)+', Дата:'
              + str(t.day)+'.'+str(t.month)+'.'+str(t.year))


    def give_to_depot(self, equipment, other):
# передача оборудование на другой склад или подразделение
        t = datetime.now()
        self.give_lists.update({equipment.serial_number: [equipment.title,other, t]})
        print('Передано оборудование:' + '' + equipment.title + ' ,серийный номер - ' + str(
            equipment.serial_number) + ', Дата:'
              + str(t.day) + '.' + str(t.month) + '.' + str(t.year))
        other.take_to_depot(equipment)


    def list_equipments(self):
        print('На склад '+self.title + ' получено оборудование:')
        print(self.lists)
        print('Общее количество: ', len(self.lists))
        print('Со склада '+self.title + ' выдано оборудование:')
        print(self.give_lists)
        print('Общее количество: ', len(self.give_lists))




class Office_equipment:
    def __init__(self, title, serial_number):
        self.title = title
        self.serial_number = serial_number

    def __str__(self):
        return str(self.title)

class Printer(Office_equipment):
    def __init__(self,title,serial_number, print_velocity):
        Office_equipment.__init__(self,title, serial_number)
        self.print_velocity = print_velocity

    def __str__(self):
        return  'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.print_velocity)


class Scanner(Office_equipment):
    def __init__(self, title,serial_number,resolution):
        Office_equipment.__init__(self,title, serial_number)
        self.resolution = resolution

    def __str__(self):
        return  'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.resolution)

class Copier(Office_equipment):
    def __init__(self, title,serial_number, addit):
        Office_equipment.__init__(self, title, serial_number)
        self.addit = addit

    def __str__(self):
        return  'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.addit)



store1 = Depot('Main warehouse')
store2 = Depot('Small warehouse')
a = Printer('HP',345678,100)
b = Scanner('Epson',123456,4000)
c = Copier('Brother',987654, 50)
d = Printer('HP',245678,200)

print(a)
print(b)
print(c)

store1.take_to_depot(a)
store1.take_to_depot(b)
store1.take_to_depot(c)
store1.take_to_depot(d)

store1.give_to_depot(a,store2)

store1.list_equipments()
store2.list_equipments()


#######################################
# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

