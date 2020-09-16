#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.



def my_dev(x,y):
    try:
        z = x / y
    except ZeroDivisionError:
        return
    return z

x = int(input('Введите числитель:'))
y = int(input('Введите знаменатель:'))
print(my_dev(x,y))



# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя,
# фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def infant_school(surname, name, born_year, town, email, phone):
    print(f"Имя - {name}, Фамилия - {surname}. Год рождения - {born_year}, город - {town}, Email {email}, номер телефона {phone}")

infant_school(surname="Иванов", name="Иван", born_year=1999, town="Москва", email="abra@kadabra.com", phone="987-765-4321")



# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    return (x + y + z - min(x, y, z))

print(my_func(3, 4, 5))

# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
    z = x
    for i in range(1, -y):
        z *= x
    return 1 / z

print(my_func(2, -5))

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже
# подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.


def infant():
    summa = 0
    while True:
        x = input('Введите cтроку чисел, разделенных пробелом, для завершения введите \'q\':')
        if x == 'q':
            print('Сумма равна ', summa)
            return summa
        y = x.split()

        for i in range(len(y)):
            if y[i] == 'q':
                print('Сумма равна ', summa)
                return summa
            summa += int(y[i])
        print('Сумма равна ', summa)
        print('Продолжим данное увлекательное занятие')


sum = infant()




# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.


int_func = lambda p: p.capitalize()


# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состо
# ит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться
# с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

s = 'hello guy how are you'
ss = s.split()
cap_s = ''
for i in range(len(ss)):
    cap_s = cap_s + int_func(ss[i]) +' '

print(cap_s)


###


