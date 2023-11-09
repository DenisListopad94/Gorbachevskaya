# # #TASK_1
# #         #VAR1
# number=1234
# number=str(number)
# print(number[0]==number[1]==number[2]==number[3])
# #         #VAR2
# number=1234
# number=str(number)
# print(number[::]==number[::-1])
# #         #VAR3
# number=1234
# number=str(number)
# print(1 == int(number[0])/int(number[1]))

#TASK_3
# adress='192.168.0.1'
# str=(adress[:3]+' '+adress[4:7]+' '+adress[8]+' '+adress[-1])
# print('Код без точек через пробел:', str)
# number_1=int(adress[:3])
# number_2=int(adress[4:7])
# number_3=int(adress[8])
# number_4=int(adress[-1])
# summa = number_1+number_2+number_3+number_4
# print('Сумма чисел',summa)


#TASK_4
#str = 'Cложный уровеень'
#str=tuple(str)
#print('Преобразование строки в кортеж = ',str)
#print('Количество букв е - ',str.count('е'))

#TASK_5
# test_tuple = ('7','3','2','1')
# index_max=test_tuple.index(max(test_tuple))
# index_min=test_tuple.index(min(test_tuple))
# quantity = abs(index_min-index_max-1)
# print('Количество элементов между мах и min: ',quantity)
