# print("Hello world")
#
# print(round(11*2.5/3, 2))
# print(round(3.14159**2/2))
#
# pi = 31.4159265
# print ("%.4e" % (pi))
#
# year = int(input())
# #your code goes here
# if year%4 != 0:
#     print("Not a leap year")
# else:
#         if year%100 != 0:
#             print("Leap year")
#
#         else:
#                 if year%400 ==0:
#                     print("Leap year")
#
#                 else:
#                         print("Not a leap year")
#
#
#
#
# L = list(map(float, input().split()))
#
# L[0], L[-1] = L[-1], L[0]
#
# L.append(sum(L))
#
# print(L)
#
# d = {'day' : 22, 'month' : 6, 'year' : 2015}
#
# print("||".join(d.keys()))
#
# text = input()
# uniq = list(set(text))
#
# print(len(uniq))
#
# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
#
# a_set, b_set = set(a), set(b) # используем множественное присваивание
#-
# a_and_b = a_set.intersection(b_set)
#
# print(a_and_b)
#
# for i in (3):
# 	print(i)
#
# a = 5
# b = 3+2
# print(id(a))
# print(id(b))
#
# print("Перед исключением")
# # теперь пользователь сам вводит числа для деления
# a = int(input("a: "))
# b = int(input("b: "))
# c = a / b # здесь может возникнуть исключение деления на ноль
# print(c) # печатаем c = a / b если всё хорошо
# print(e) # Выводим информацию об ошибке
# print("После исключения")
#
# try:  # Добавляем конструкцию try-except для отлова нашей ошибки
#     print("Перед исключением")
#     # теперь пользователь сам вводит числа для деления
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = a / b  # здесь может возникнуть исключение деления на ноль
#     print(c)  # печатаем c = a / b если всё хорошо
# except ZeroDivisionError as e:  # Добавляем тип именно той ошибки которую хотим отловить.
#     print(e)  # Выводим информацию об ошибке
#     print("После исключения")
#
# print("После После исключения")
#
# try:
#     print("Перед исключением")
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = a / b
#     print(c)  # печатаем c = a / b, если всё хорошо
# except ZeroDivisionError as e:
#     print("После исключения")
# else:  # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т.е. не вылетело никакого исключения).
#     print("Всё ништяк")
# finally:  # код в блоке finally выполнится в любом случае при выходе из try-except
#     print("Finally на месте")
#
# print("После После исключения")
#
# age = int(input("How old are you?"))
#
# if age > 100 or age <= 0:
#     raise ValueError("Тебе не может быть столько лет")
#
# print(f"Тебе {age} лет!")  # Возраст выводится только в случае, если пользователь ввёл правильный возраст.
#
# try:
#     age = int(input("How old are you?"))
#     if age > 100 or age <= 0:
#         raise ValueError("Тебе не может быть столько лет")
# except ValueError as error:
#     print(error)
#     print("Неправильный возраст")
# else:
#     print(f"You are {age} years old!") # Возраст выводится только в случае, если пользователь ввёл правильный возраст.
#
# print(list(range(6)))
# print(list(range(1, 5)))
# print(list(range(1, 10, 2)))
#
# S = 0
# N = 5
#
# for i in range(1, N+1):
#     print(S)
#     print(i)
#     S = S + i
#     print(S)
#     print("---")
# print("End")
# print()
# print(S)
#
# P=1
# N=5
#
# for i in range(1, N+1):
#     P *= i
# print(P)
#
# n = 5
#
# for i in range(1, n+1):
#     print("*"*i)
#
# S = 0
# n = 1
#
# while S<500:
#     S = S + n
#     n = n + 1
#
# print(S)
# print(n)
#
# n = 1
# while n**2 < 1000:
#     n = n +1
#
# print(n)
#
# n = 1
# while n < 10:  # в данной программе это условие всегда True, цикл будет бесконечным
#     print("Hello World")
#
# squares = [i**2 for i in range(1,11)]
# print(squares)
#
# squares_2 = [i**2 for i in range(1,11) if i % 2 == 1]
# print(squares_2)
#
# list_tuples = [(i, i**2) for i in range(1,11)]
#
# M = [[i+j for j in range(5)] for i in range(5)]
#
# T = [[i*j for j in range(1,11)] for i in range(1,11)]
#
# bool
#
# def print_2_add_2():
#     sum = 2 + 2
#     print(sum)
#
# print_2_add_2()
#
# def hello_world():
#     print("Hello World")
#
# hello_world()
#
# def pow_func(base):
#     print(base**2)
#
# pow_func(2)
# pow_func(3)
# pow_func()
#
# def pow_func(base, n=2):
#    print(base ** n)
#
# pow_func(3)
# pow_func(5, 3)
#
# def devide_func(a,n):
#     if a% n == 0:
#         print(f"{a} is devided by {n}")
#     else:
#         print(f"{a} is not devided by {n}")
#
# devide_func(10,5)
# devide_func(10,6)
#
# def reverse_stair(n):
#    for i in range(n, 0, -1):
#        print("*" * i)
#
# reverse_stair(5)
#
# def pow_func(base, n=2):
#    print(base ** n)
#    return None
#
# print(pow_func(3))
#
# def pow_func(base, n=2):
#     inside_result = base ** n
#     return inside_result
#
# print(pow_func(3))
#
# outside_result = pow_func(3)
# print(outside_result)
#
# def get_multipliers(a):
#    count = 0
#    for n in range(1, a + 1):
#        if a % n == 0:
#            count += 1
#
#    return count
#
# print(get_multipliers(5))
# print(get_multipliers(4))
#
# def check_palindrome(str_):
#    str_ = str_.lower()
#    str_ = str_.replace(" ", "")
#
#    if str_ == str_[::-1]:
#        return True
#    else:
#        return False
#
# print(check_palindrome("test"))  # False
# check_palindrome("Кит на море не романтик")  # True
#
# def local():
#    x = 5  # локальная переменная
#    print(x)
#
# x = 10
# local()
# print(x)
#
# def local():
#   print(x)  # так как x нет в локальной области видимости, мы берем её из глобальной области
#
# x = 10
# local()
# print(x)
#
# x = 3
#
#
# def func():
#    global x # объявляем, что переменная является глобальной
#    print(x)
#    x = 5
#    x += 5
#    return x
#
#
# func()
# print(x)
#
# def get_my_func():
#    def hello_world():
#        print("Hello")
#    return hello_world
#
# hello_world_func = get_my_func()  # получить функцию в качестве результата
#
# print(type(hello_world_func))  # <class 'function'>
# hello_world_func()  # Hello
#
# def get_mul_func(m):
#     nonlocal_m = m
#     def local_mul(n):
#         return n * nonlocal_m
#
#     return local_mul
#
# two_mul = get_mul_func(2)
# two_mul(5)
#
# def func(a, b, c):
#     print('a =', a)
#     print('b =', b)
#     print('c =', c)
#
# func(1,2,3)
# func(3, 2, 1)
# func(a=1, b=2, c=3)
# func(c=3, b=2, a=1)
# func(a, b, c=3)
#
# a = [1,2,3]
# b = [a,4,5,6]
# print(b)
#
# a = [1,2,3]
# b = [*a,4,5,6]
# print(b)
#
# def my_func(*args, **kwargs):
#    print(type(args))
#    print(type(kwargs))
#
# my_func()
#
# def adder(*nums):
#     sum_ = 0
#     for n in nums:
#         sum_ += n
#
#     return sum_
#
# print(adder())
# print(adder(1))
# print(adder(1,2))
# print(adder(1,2,3))
#
# def multiplier(*nums):
#     mlt = 1
#     for n in nums:
#         mlt *= n
#
#     return mlt
#
# print(multiplier())
# print(multiplier(1))
# print(multiplier(1,2))
# print(multiplier(1,2,3))
#
# def incorrecr_func(name_arg=[]):
#     print(name_arg)
#     name_arg.append(1)
#     print(name_arg)
#
# incorrecr_func()
# incorrecr_func()
#
# def correct_func(name_arg=None):
#     if name_arg is None:
#         name_arg = []
#     print(name_arg)
#     name_arg.append(1)
#     print(name_arg)
#
# correct_func()
# correct_func()
# correct_func([123])
# correct_func(name_arg=[123])
#
# def rec_fibb(n):
#    if n == 1:
#        return 1
#    if n == 2:
#       return 1
#    return rec_fibb(n - 1) + rec_fibb(n - 2)
#
# rec_fibb(10)
#
# def rec_sum(n):
#     if n == 1:
#         return 1
#     return n + rec_sum(n - 1)
#
# rec_sum(5)
#
# def reverse_str(string):
#     if len(string) == 0:
#         return ''
#     else:
#         return string[-1] + reverse_str(string[:-1])
#
# reverse_str('test')
#
# def sum_digit(n):
#    if n < 10:
#        return n
#    else:
#        return n % 10 + sum_digit(n // 10)
#
# sum_digit(123)
#
# def fib():
#     a, b = 0, 1
#     yield a
#     yield b
#
#     while True:
#         a, b = b, a + b
#         yield b
#
# for num in fib():
#     print(num)
#
# def count(start=1,step=1):
#     counter = start
#     while True:
#         yield counter
#         counter += step
#
# def repeat_list(list_):
#     list_values = list_.copy()
#     while True:
#         value = list_values.pop(0)
#         list_values.append(value)
#         yield value
#
# for i in repeat_list([1,2,3,4,5]):
#     print(i)
#
# def twice_func(inside_func):
#     inside_func()
#     inside_func()
#
# def hello():
#     print("Hello")
#
# test = twice_func(hello)
#
# def make_adder(x):
#     def adder(n):
#         return x + n
#     return adder
#
# add_5 = make_adder(5)
# print(add_5(10))
# print(add_5(100))
#
# def linear_solve(a,b):
#     if a:
#         return b/a
#     else:
#         return "Net kornei"
#
# print(linear_solve(0,9))
#
# a = ["asd", "bbd", "ddfa", "mcsa"]
# print(list(map(len, a)))
# print(list(map()))
#
# myFile = open('myFile.txt', 'rt', encoding="utf8")
# print(myFile.read())
# print(myFile.read(20))
# print(myFile.readline())
# print(myFile.readlines())
#
# for line in myFile:
#     print(line)
#
# myFile = open('newfile.txt', 'w')
# myFile.write('ttttt')
# print('zzzzz', file=myFile)
#
# with open("newfile.txt") as myFile:
#     for line in myFile:
#         print(line)
#
# alpha = 'abcdefghijklmnopqrstuvwxyz'
# alphaUp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# number = int(input('Vvedite chislo na skolko sdvinut'))
#
# summary = ''
#
# def changeChar(char):
#     if char in alpha:
#         return alpha[(alpha.index(char) + number) % len(alpha)]
#     elif char in alphaUp:
#         return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
#     else:
#         return char
#
# with open("newfile.txt") as myFile:
#     for line in myFile:
#         for char in line:
#             summary += changeChar(char)
#
# with open("output.txt", 'w') as myFile:
#     myFile.write(summary)
#
# import os
#
# print(os.path.join('..', 'test', 'labirint.txt'))
#
#
# def found(pathArr, finPoint):
#     weight = 1
#     for i in range(len(pathArr) * len(pathArr[0])):
#         for y in range(len(pathArr)):
#             for x in range(len(pathArr[y])):
#                 if pathArr[y][x] == weight:
#                     # Вниз
#                     if y > 0 and pathArr[y - 1][x] == 0:
#                         pathArr[y - 1][x] = weight + 1
#
#                         # Вверх
#                     if y < (len(pathArr) - 1) and pathArr[y + 1][x] == 0:
#                         pathArr[y + 1][x] = weight + 1
#
#                     # Вправо
#                     if x > 0 and pathArr[y][x - 1] == 0:
#                         pathArr[y][x - 1] = weight + 1
#
#                     # Влево
#                     if x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == 0:
#                         pathArr[y][x + 1] = weight + 1
#
#                     # Конечная точка
#                     if (abs(y - finPoint[0]) + abs(x - finPoint[1])) == 1:
#                         pathArr[finPoint[0]][finPoint[1]] = weight + 1
#                         return True
#         weight += 1
#     return False
#
#
# def printPath(pathArr, finPoint):
#     y = finPoint[0]
#     x = finPoint[1]
#     weight = pathArr[y][x]
#     result = list(range(weight))
#     while (weight):
#         weight -= 1
#         if y > 0 and pathArr[y - 1][x] == weight:
#             result[weight] = 'Вниз'
#             y -= 1
#         elif y < (len(pathArr) - 1) and pathArr[y + 1][x] == weight:
#             result[weight] = 'Вверх'
#             y += 1
#         elif x > 0 and pathArr[y][x - 1] == weight:
#             result[weight] = 'Вправо'
#             x -= 1
#         elif x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == weight:
#             result[weight] = 'Влево'
#             x += 1
#
#     return result[1:]
#
#
# labirint = []
# with open("labirint.txt") as myFile:
#     for line in myFile:
#         labirint.append(line.replace('\n', '').split(' '))
#
# ii = 0
# for i in labirint:
#     jj = 0
#     for j in i:
#         if j == 'A':
#             labirint[ii][jj] = 1
#             pozIn = (ii, jj)
#         elif j == 'B':
#             labirint[ii][jj] = 0
#             pozOut = (ii, jj)
#         elif j == '1':
#             labirint[ii][jj] = -1
#         else:
#             labirint[ii][jj] = 0
#         jj += 1
#     ii += 1
#
# if not found(labirint, pozOut):
#     print("Путь не найден!")
# else:
#     result = printPath(labirint, pozOut)
#
#     for i in labirint:
#         for line in i:
#             print("{:^3}".format(line), end=" ")
#         print()
#     print(result)
#
# import json
#
# with open('json_example.json', encoding='utf8') as f:
#     templates = json.load(f)
#
# print(templates)
# print(type(templates))
#
# import json
#
# with open('json_example.json', encoding='utf8') as f:
#     strfile = f.read()
#     templates = json.loads(strfile)
#
# print(templates)
# print(type(templates))
#
# import json
#
# template = {
#     'firstname': 'Иван',
#     'lastname': 'Иванов',
#     'isAlive': True,
#     'age': 32,
#     'address': {
#         'streetAddress': 'Нейбута 32',
#         'city': 'Владивосток',
#         'state': '',
#         'postalcode': ''
#     },
#     'phoneNumbers': [
#         {
#             'type': 'mob',
#             'number': '123-333-4455'
#         },
#         {
#             'type': 'office',
#             'number': '123 111-4567'
#         }
#     ],
#     'children': [],
#     'spouse': None
# }
#
# with open('to_json_example.json', 'w', encoding='utf8') as f:
#     json.dump(template, f, ensure_ascii=False, indent=4)
#
# with open('to_json_example.json', encoding='utf8') as f:
#     print(f.read())
#
# def changeText(text):
#     """
#     Функция принимает строку с текстом.
#     Убирает все знаки препинания и возвращает
#     список, состоящий из слов текста.
#     """
#
#
# for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
#     text = text.replace(i, '')
#
# return text.split()
#
#
# def mostCommon(text, lenght=0):
#     """
#     Функция принимает список и ограничение по длине.
#     Возвращает самый часто встречающийся элемент.
#     Если есть несколько элементов с одинаковой самой большой частотой, то вернёт их все.
#     """
#
#
# most_common = []
# qty_most_common = 0
#
# for item in text:
#     if len(item) > lenght:
#         qty = text.count(item)
#         if qty > qty_most_common and qty > 2:
#             qty_most_common = qty
#             most_common = [item]
#         elif qty == qty_most_common:
#             most_common.append(item)
#
# return list(set(most_common))
#
#
# def mostLenght(text):
#     """
#     Функция принимает список.
#     Возвращает самый длинный элемент.
#     Если есть несколько элементов с одинаковой самой большой длиной, то вернёт их все.
#     """
#
#
# most_lenght = []
# qty_most_lenght = 0
# alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for item in text:
#     for char in item:
#         if char not in alphabet:
#             charEn = False
#         else:
#             charEn = True
#
#     if charEn:
#         qty = len(item)
#         if qty > qty_most_lenght:
#             qty_most_lenght = qty
#             most_lenght = [item]
#         elif qty == qty_most_lenght:
#             most_lenght.append(item)
#
# return list(set(most_lenght))
#
# nameFile = input('Название файла: ')
#
# with open(nameFile, encoding='utf8') as f:
#     fileText = f.read()
#
# fileText = changeText(fileText)
# print(f'Список самых частых слов длинной более трёх символов: {mostCommon(fileText, 3)}')
# print(f'Список самых длинных английских слов: {mostLenght(fileText)}')
#
# def say_hello(name):
#     return f"Hello {name}"
#
# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"
#
# def greet_bob(greeter_func):
#     return greeter_func("Bob")
#
# print(greet_bob(say_hello))
# print(greet_bob(be_awesome))
#
#
# def parent():
#     print("Printing from the parent() function")
#
#     def first_child():
#         print("Printing from the first_child() function")
#
#     def second_child():
#         print("Printing from the second_child() function")
#
#     second_child()
#     first_child()
# parent()
#
#
#
# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"
#
#     def second_child():
#         return "Call me Liam"
#
#     if num == 1:
#         return first_child
#     else:
#         return second_child
#
# first = parent(1)
# second = parent(2)
#
# print(first())
# print(second())


def my_decorator(func):
    def wrapper():
        print("Начало выполнения функции.")
        func()
        print("Конец выполнения функции.")

    return wrapper


def my_first_decorator():
    print("This is my first decorator")

my_first_decorator = my_decorator(my_first_decorator)

my_first_decorator()



def working_hours(func):
    def wrapper():
        from datetime import datetime
        if 9 <= datetime.now().hour < 18:
            func()
        else:
            pass  # Нерабочее время, выходим
    return wrapper

@working_hours
def writing_tests():
    print("Я пишу тесты на python!")

writing_tests()

















































