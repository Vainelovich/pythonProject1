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






















































































