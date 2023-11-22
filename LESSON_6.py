#TASK_1
# from random import randint
# def lst_1() -> list[int]:
#     '''Функция генерирует список из 10 чисел во второй степени'''
#     square = [randint(1,10)**2 for _ in range(10)]
#     print(square)
# lst_1()

#TASK_2
from random import randint
# def lst_1()-> list[int]:
#     '''Функция генерирует список из всех трехзначных чисел, которые кратны 3 и 5'''
#     nmb=[num for num in range(100,1000) if num%5 == 0 and num%3==0]
#     print(nmb)
# lst_1()

#TASK_3
# def numbers(a:int,b:int,c:int)-> list[int]:
#     '''Функция создает список чисел из промежутка от а до b в степени с'''
#     result=[]
#     for num in range(a,b+1):
#         result.append(num**c)
#     print(result)
# a,b,c=map(int,input('Введите a b c через пробел: ').split())
# numbers(a,b,c)

#TASK_4
# result=[]
# def lst_1()-> list[int]:
#     ''' Функция изменяет список целых чисел выводя для каждого элемента этого списка
#     сумму двух его соседей. Для элементов списка, являющихся крайними,
#     одним из соседей считается элемент, находящий на противоположном конце этого списка'''
#     global result
#     input_numbers=input('Enter numbers: ')
#     numbers=[int(x) for x in input_numbers.split()]
#     for i in range(len(numbers)):
#         if i==0:
#             result.append(numbers[-1] + numbers[1])
#         elif i == len(numbers)-1:
#             result.append(numbers[i-1] + numbers[0])
#         else:
#             result.append(numbers[i-1] + numbers[i+1])
#     print(result)
# lst_1()

#TASK_5
# def minimum(a:int,b:int)->int:
#     '''Функция принимает два аргумента a и b и возвращает минимальное из них'''
#     return (min(a,b))
# result=minimum(minimum(53,78),minimum(74,51))
# print(result)

#TASK_6
# from math import sqrt
# def distance(x1:float, y1:float, x2:float, y2:float) -> float:
#     '''Функция вычисляет расстояние между точками (х1,у1) и (х2,у2) и возвращает действительное число'''
#     print(sqrt((x2-x1)**2+(y2-y1)**2))
# distance(21.6,15.5,9.8,7.2)

#TASK_7
# def fib(n:int)->int:
#     '''Функция возвращает n-e число Фибоначчи '''
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     a,b=0,1
#     for _ in range(2,n+1):
#         a,b=b,a+b
#     return b
# n=int(input('enter n: '))
# result = fib(n)
# print(result)

#TASK_8
# def closest_mod_5(x:int)->int:
#     '''Функция возвращает минимальное число кратное 5'''
#     result = x if x%5==0 else x + (5 - x % 5)
#     return result
# print(closest_mod_5(18))

#TASK_9
# def modify_list(l:list[int]) -> None:
#     '''Функция считывает список чисел, удаляет все нечетные числа, а четные нацело делит на 2'''
#     i=0
#     while i < len(l):
#         if l[i]%2==0:
#             l[i]=l[i]//2
#             i+=1
#         else:
#             del l[i]
#     print(l)
# numbers_input = input('enter numbers: ')
# lst_1 = [int(x) for x in numbers_input.split()]
# modify_list(lst_1)