#TASK_1
# with open('name.txt', 'r') as file:
#     for line in file:
#         if line.rstrip().endswith('!'):
#             print(line.rstrip())

#TASK_2
# with open('input.txt','w') as file:
#     file.write(input('Введите числа через пробел: '))
# with open('input.txt','r') as file:
#     content=file.read()
#     numbers=list(map(int,content.split()))
# num_1=1
# for num in numbers:
#     num_1*=num
# with open('output.txt','w') as file:
#     file.write(f'Произведение чисел:{num_1}')
# print(f'Произведение чисел:{num_1}')

#TASK_3
# from datetime import datetime, timedelta
# today=datetime.now()
# shop = [
#     {
#     'наименование': 'Товар 1',
#     'количество': 4,
#     'цена_единицы': 999.99,
#     'дата_поступления': '2023-01-01'
#     },
#     {
#     'наименование': 'Товар 2',
#     'количество': 550,
#     'цена_единицы': 10.99,
#     'дата_поступления': '2023-12-03'
#     },
#     {
#     'наименование': 'Товар 3',
#     'количество': 2,
#     'цена_единицы': 550000,
#     'дата_поступления': '2023-11-01'
#     }
#     ]
# for product in shop:
#     data_in_shop=datetime.strptime(product['дата_поступления'],'%Y-%m-%d')
#     result_data=today-data_in_shop
#     if result_data.days>30 and product['цена_единицы']*product['количество']>1000000:
#         print(f"Наименование: {product['наименование']}")
#         print(f"Количество: {product['количество']}")
#         print(f"Цена единицы: {product['цена_единицы']}")
#         print(f"Дата поступления: {product['дата_поступления']}")
#         print("-" * 30)

#TASK_4
# import json
# person = {
#     12345: ('Masha', 25),
#     67890: ('Kate', 30),
#     54321: ('Julia', 22),
#     98765: ('Nastya', 28),
#     11111: ('Ivan', 35)
# }
# with open('data.json', 'w') as json_file:
#     json.dump(person, json_file)
# print("Словарь сохранен в файл 'data.json'")

#TASK_5
# import json
# import csv
# with open('data.json', 'r') as json_file:
#     data_dict = json.load(json_file)
# csv_filename = 'data.csv'
# with open(csv_filename, 'w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=';')
#     csv_writer.writerow(['person_id', 'name', 'age'])
#     for person_id, (name, age) in data_dict.items():
#         csv_writer.writerow(['person ' + str(person_id), name, age])
# print(f"Данные записаны в файл {csv_filename}")

#TASK_6
# x = (1, 2, 5, 7)
# try:
#     x = x / 2
#     print(x)
# except TypeError as e:
#     print(f"Ошибка: {e}")

#TASK_7
# try:
#     my_list = [1, 2, 3, 4]
#     value = my_list[5]
#     print(f"Значение по индексу 5: {value}")
# except IndexError as e:
#     print(f"Ошибка: {e}")

#TASK_8
# try:
#     string_value = "Hello"
#     number_value = 22
#     result = string_value + number_value
#     print(f"Результат конкатенации: {result}")
# except TypeError as e:
#     print(f"Ошибка: {e}")

#TASK_9
# try:
#     file_1= "файл.txt"
#     with open(file_1, 'r') as file:
#         content = file.read()
#     print(f"Содержимое файла: {content}")
# except FileNotFoundError as e:
#     print(f"Ошибка: {e}")

#TASK_10
# try:
#     my_list = [1, 2, 3, 4, 5]
#     el_remove = int(input("Введите значение элемента для удаления: "))
#     my_list.remove(el_remove)
#     print(f"Список после удаления: {my_list}")
# except ValueError as e:
#     print(f"Ошибка: {e}")


