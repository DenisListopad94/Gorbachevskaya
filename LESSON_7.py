#TASK_1
# str_1='Это были прекрасные выходные!'
# result=lambda x: x in str_1
# print(result('выходные'))

#TASK_2
# nmb=lambda x:x%2==0
# print(nmb(int(input('Введите число: '))))

#TASK_3
# name_hello=lambda name:print(f'Hello {name}') if name.istitle() else print('Имя введено неверно')
# name_hello(input('Enter name: '))

#TASK_4
# def digits(n: int) -> str:
#     '''A function that takes a number and returns a string with
#     numbers from right to left separated by a space'''
#     if n < 10:
#         return str(n)
#     else:
#         last_digit = n % 10
#         rest_digits = n // 10
#         return f'{digits(rest_digits)} {last_digit}'
#
# result = digits(14623)
# print(result)

#TASK_5
# def is_power(n:int)->bool:
#     '''A function that checks whether a number is a power of two'''
#     if n==1:
#         return True
#     elif n%2==0 and n>1:
#         return is_power(n//2)
#     else:
#         return False
# result=is_power(1048576)
# print(result)

#TASK_6
# def sum_digits(n: int) -> int:
#     '''A function that calculates the sum of all digits of the number n'''
#     if n == 0:
#         return 0
#     else:
#         last_digit = n % 10
#         rest_digits = n // 10
#         return last_digit + sum_digits(rest_digits)
#
# result = sum_digits(14623)
# print(result)

#TASK_7
# from time import time
# def time_decorator(func):
#     def wrapper():
#         start_time = time()
#         func()
#         end_time = time()
#         finaly_time = end_time - start_time
#
#         print(f"Execution time: {finaly_time} seconds")
#
#     return wrapper
#
# @time_decorator
# def print_primes():
#     ''' Prints all prime numbers in the range from 2 to 100'''
#     for num in range(2, 101):
#         is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
#         if is_prime:
#             print(num)
# print_primes()

#TASK_8
# from typing import Tuple
# def decorator_fun(func) -> None:
#     def wrapper(password: str) -> None:
#         result=func(password)
#         if result:
#             print(f' Hello user with password {password}')
#         else:
#             print('Password check failed')
#
#     return wrapper
# @decorator_fun
# def check_password(password: str) -> Tuple[bool, str]:
#     '''A function that checks the password entered by the user'''
#     if len(password) < 8:
#         return False, "Пароль должен содержать не менее 8 символов"
#     if not any(char.isdigit() for char in password):
#         return False, "Пароль должен содержать хотя бы одну цифру"
#     if not any(char.isalpha() for char in password):
#         return False, "Пароль должен содержать хотя бы одну букву"
#
#     return "Пароль введен верно"
# check_password('IT67589Sone')


