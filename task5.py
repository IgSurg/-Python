#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.



name = 'my_file.txt'

try:
    with open(name,'w') as myfile:
        while True:
            s = input('Введите строку для записи в файл либо введите \'\', чтобы прекратить:')
            if s == '': break
            s = s +'\n'
            myfile.writelines(s)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    myfile.close()



my_f = open(name, "r")
for line in my_f:
    print(line)
my_f.close()



#2 . Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

name = 'my_file2.txt'

try:
    with open(name,'r') as myfile:
        content = myfile.readlines()
        print('Количество сторок - ', len(content))
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    myfile.close()

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

name = 'file-FIO.txt'
med = 0

try:
    with open(name,'r') as myfile:
        content = myfile.readlines()
        n = len(content)
        myfile.seek(0)
        print('Выводим ФИО менее 20 тыс рублей')
        for i in range(n):
            content = myfile.readline()
            s = content.split()
            if int(s[1]) < 20:
                print(s[0],'оклад',s[1],'тысяч рублей')
            med += int(s[1])
        print('Средний оклад - ', med/n, 'тысяч рублей')

except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    myfile.close()


# 4 Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
# Two — 2
# Three — 3
# Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

name = 'my_file_count.txt'
new_str = []

try:
    with open(name,'r') as myfile:
        content = myfile.readlines()
        n = len(content)
        myfile.seek(0)
        for i in range(n):
            content = myfile.readline()
            s = content.split()
            if s[0] == 'One':
                s[0] = 'Один'
            elif s[0] == 'Two':
                s[0] = 'Два'
            elif s[0] == 'Three':
                s[0] = 'Три'
            elif s[0] == 'Four':
                s[0] = 'Четыре'
            new_str.append(s)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    myfile.close()

# write new content

new_content = ''
for i in range(n):
    new_content = new_content + ' '.join(new_str[i]) +'\n'

name = 'new_my_file_count.txt'
try:
    with open(name,'w') as myfile:
            myfile.write(new_content)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    myfile.close()


#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

new_str = ['1','2','3','4','66','77','88']

new_content = ' '.join(new_str)

name = 'new_my_file_5.txt'
try:
    with open(name,'w') as myfile:
            myfile.write(new_content)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    myfile.close()

# считываем  числа в файле и подсчитываем сумму по всем строкам

med = 0

try:
    with open(name, 'r') as myfile:
        while True:
            content = myfile.readline()
            if content == '':
                break
            s = content.split()
            for k in range(len(s)):
                med += int(s[k])
        print('Sum  =', med)


except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    myfile.close()


#6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно,
# чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
#
#Примеры строк файла:
#
#Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —
#Пример словаря:
#
#{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

# читаем файл

name = 'my_file5_6.txt'
s = []
try:
    with open(name, 'r') as myfile:
        while True:
            content = myfile.readline()
            if content == '':
                break
            s.append(content.split())
        print('S  =', s)

except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    myfile.close()

# формируем справочник

dict = {}
for i in range(len(s)):
    sum = 0
    key = s[i][0]
    for k in range(1,len(s[i])):
        x = s[i][k]
        it = x.split('(')[0]
        if it == '-':
            it = '0'
        sum += int(it)
    dict.update({key: sum})


for key, value in dict.items():
     print(f"{key} - {value}")



