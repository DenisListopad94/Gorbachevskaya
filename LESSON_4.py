#TASK_1
# a = 7
# b = 6
# c = -7
# print(a<=0 or b<=0 or c<=0)

#TASK_2
# n=6
# k=3
# print('Оба числа четные? - ',(n%2) == (k%2))

#TASK_3
# int1 = 2
# int2 = 3
# int3 = 8
# even_int=0
# if int1%2==0:
#     even_int+=1
# if int2%2==0:
#     even_int+=1
# if int3%2==0:
#    even_int+=1
# print('Количество четных чисел = ',even_int)

#TASK_4
# number = 44
# number = str(number)
# if int(number[0])+int(number[1]) >= 10:
#     print('Да')
# else:
#     print('Нет')

#TASK_5
# number = 10
# for i in range(1,21):
#     print(i,'-',number)

#TASK_6
# n = 15
# for i in range(1,n+1):
#     print(i,'-',i**3,end=' ')

#TASK_7
# finish=1
# for i in range(5,21):
#     finish*=i
# print('Произведение всех чисел в промежутке от 5 до 20 = ', finish)

#TASK_8
# n=15
# for i in range(1,n+1):
#     if i**2<=15:
#         print(i ** 2,end=' ')

#TASK_9
# n=1645644044
# n=str(n)
# n_min=n.index(min(n))
# print('Минимальное число -',n[n_min])

#TASK_10
# year = int(input('Введите год: '))
# if year%4==0 and year%100!=0 or year%400==0:
#     print('Високосный год')
# else:
#     print('Не високосный год')

#TASK_11
# n = 7
# for i in range(1,n+1):
#     if i==1:
#         print('На лугу', i, 'коровa')
#     elif 2<=i<=4:
#         print('На лугу', i,'коровы')
#     else:
#         print('На лугу', i,'коров')