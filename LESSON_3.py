#TASK_1
# str = 'Домашнее задание'
# print(str[2])       #3 символ строки
# print(str[-2])      #предпоследний символ строки
# print(str[0:5])     #первые 5 символов
# print(str[:-2])     #вся строка, кроме последних 2 символов
# print(str[::2])     #все символы с четными индексами
# print(str[1::2])    #все сиволы с нечетными индексами, начиная со 2 символа
# print(str[::-1])    #все символы в обратном порядке
# print(str[::-2])    #все символы в обратном порядке через 1, начиная с последнего
# print(len(str))     #длина строки

#TASK_2
# word = 'Собака'
# print(word[0]==word[-1])

#TASK_3
#word='Тетрадь'
#print(word[1]+word[2]+word[3])

#TASK_4
# word = 'яблоко'
# print(word[1:5])
# print(word[-3]+word[-2]+word[-1])

#TASK_5
# str='Ivanou Ivan'
# print(str[-4:]+' '+str[:6])

#TASK_6
# word='шалаш'
# print(word==word[::-1])

#TASK_7
# lst=(1,'Hello',3,4,5)
# print(lst[1])

#TASK_8
# str_1='газ'
# str_2='газировка'
# print(str_1 in str_2)

#TASK_9
# str = 'forfor'
# first_f=str.index('f')
# second_f=str.index('f',first_f+1)
# print(second_f)

#TASK_10
#school={'class_1':20,'class_2':15,'class_3':18,'class_4':14,'class_5':16,
#       'class_6':19,'class_7':23,'class_8':25,'class_9':15,'class_10':11,'class_11':9}
#school['class_10']=13       #в 10 класс пришли 2 ученика
#print('В 10 класс пришли 2 ученика',school)
#school['class_7A']=12       #в школе открыли 7А класс
#print('В школе открыли 7А класс',school)
#del school['class_10']        #в школе закрыли 10 класс
#print('В школе закрыли 10 класс',school)
#print(school)
#summa=(school['class_1']+school['class_2']+school['class_3']+
#       school['class_4']+school['class_5']+school['class_6']+
#       school['class_7']+school['class_8']+school['class_9'])
#print('Сумма учеников с 1 по 9 классы: ',summa)
