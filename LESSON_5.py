#TASK_1
# tpl = (6,2,7,8)
# for nmb in tpl:
#     deliteli = 0
#     for i in range(1,nmb):
#         if nmb%i==0:
#             deliteli+=i
#     if deliteli==nmb:
#         print(nmb,'совершенное число')

#TASK_2
# tpl=(5,2,-2,7,-8,-9,1)
# counter=0
# str_tpl=str(tpl)
# for ind in range(len(tpl)-1):
#     if tpl[ind]>0 and tpl[ind+1]<0 or tpl[ind+1]>0 and tpl[ind]<0:
#         counter+=1
# print(counter)

#TASK_3
# lst_1=[4,1,6,9]
# lst_2=[8,1,2,4,9,5,7,6]
# min_elements = []
# for min_el in lst_1:
#     if min_el not in lst_2:
#         min_elements.append(min_elin)
# if min_elements:
#     print(min_elements)
# else:
#     print('Нет такого элемента')

#TASK_4
# lst=[15,64,43,28,89]
# new_lst=[]
# for el in lst:
#     new_lst.append(el)
#     if el%2==0:
#         el=int(str(el)[::-1])
#         new_lst.append(el)
# print(new_lst)

#TASK_5
# lst=[5,2,4,5,1,2]
# unicle_lst=set(lst)
# counter=0
# for el in unicle_lst:
#    counter=lst.count(el)
#    print(el,counter)

#TASK_6
# lst=[7,4,1]
# new_lst=[]
# for el in lst:
#    new_lst.append(el)
#    new_lst.append(0)
# print(new_lst)

#TASK_7
# str_1='1 4 5 1 4 7'
# new_str=set()
# numbers = str_1.split()
# for nmb in numbers:
#     if nmb in new_str:
#         print("YES")
#     else:
#        new_str.add(nmb)
#        print("NO")

#TASK_8
# n = int(input())
# ans = set(range(1, n + 1))
# q = 0
# while True:
#     q = input()
#     if q == "HELP":
#         break
#     else:
#         a = set(list(map(int, q.split())))
#         q = input()
#         if q == "YES":
#             ans = ans & a
#         else:
#             ans = ans - a
# ans = sorted(ans)
# print(*ans)

#TASK_9
# dictionary = {'good':'well','bad':'ill','beautiful':'handsome'}
# word=input('Enter a word to find a synonym for: ')
# if word in dictionary:
#     synonim=dictionary[word]
#     print('synonym of the word',word,' - ',synonim)
# else:
#     print('synonym of the word not found')

#TASK_10
