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



# def my_decorator(func):
#     def wrapper():
#         print("Начало выполнения функции.")
#         func()
#         print("Конец выполнения функции.")
#
#     return wrapper
#
#
# def my_first_decorator():
#     print("This is my first decorator")
#
# my_first_decorator = my_decorator(my_first_decorator)
#
# my_first_decorator()
#
#
#
# def working_hours(func):
#     def wrapper():
#         from datetime import datetime
#         if 9 <= datetime.now().hour < 18:
#             func()
#         else:
#             pass  # Нерабочее время, выходим
#     return wrapper
#
# @working_hours
# def writing_tests():
#     print("Я пишу тесты на python!")
#
# writing_tests()


from practice_21.decorators import do_twice, debug


# @do_twice
# def do_test_twice():
#     print("Eto vizov functsii test_twice")
#
# do_test_twice()

#
# @do_twice
# def do_test_twice(str):
#     print("Этот вызов возвращает строку {0}".format(str))
#
# do_test_twice("Попытаемся вызвать функцию с аргументом")
#
#
# @do_twice
# def do_test_twice_without_params():
#     print("Этот вызов без параметров")
#
#
# @do_twice
# def do_test_twice_2_params(str1, str2):
#     print("В этой функции 2 параметра - {0} и {1}".format(str1, str2))
#
# @do_twice
# def do_test_twice(str):
#     print("Этот вызов возвращает строку {0}".format(str))
#
# do_test_twice_without_params()
# do_test_twice_2_params("1", "2")
# do_test_twice("single")

#
# @do_twice
# def do_test_twice(str):
#     print("Этот вызов возвращает строку {0}".format(str))
#     return "Done"
#
# # decorated_value = do_test_twice("single")
# # print(decorated_value)
#
# print(do_test_twice.__name__)



@debug
def age_passed(name, age=None):
  if age is None:
    return "Необходимо передать значение age"
  else:
    return "Аргументы по умолчанию заданы!"

age_passed("Роман")
age_passed("Роман", age=21)









































