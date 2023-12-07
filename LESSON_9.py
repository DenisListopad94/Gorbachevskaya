#TASK_1
# class SummMax():
#     def __init__(self,a:int,b:int):
#         self.a=a
#         self.b = b
#     def display(self)->None:
#         '''Displays arguments a and b on the screen'''
#         print(f'Число а {self.a} и Число b {self.b}:')
#     def summ(self):
#         '''Finds the sum of a and b'''
#         return self.a+self.b
#     def max_el(self):
#         '''Finds the maximum of a and b'''
#         return max(self.a,self.b)
#
# num=SummMax(6,7)
# num.display()
# print(f'Summa: {num.summ()}')
# print(f'Maximum: {num.max_el()}')

#TASK_2
# class Decimal_counter():
#     def __init__(self,max_value=100,min_value=0,start_value=0):
#         self.max_value=max_value
#         self.min_value=min_value
#         self.start_value=start_value
#         self.value=start_value
#     def current_value(self)->int:
#         return self.value
#     def increase(self)->None:
#         """Increases the counter value by 1 if the maximum value is not reached"""
#         if self.value <self.max_value:
#             self.value+=1
#         else:
#             print("Достигнуто максимальное значение.")
#     def decrease(self)->None:
#         """Reduces the counter value by 1 if the minimum value is not reached"""
#         if self.value > self.min_value:
#             self.value-=1
#         else:
#             print("Достигнуто минимальное значение.")
# counter = Decimal_counter()
# print("Текущее значение:", counter.current_value())
# counter.increase()
# print("Увеличено значение:", counter.current_value())
# counter.decrease()
# print("Уменьшено значение:", counter.current_value())
# counter_custom = Decimal_counter(max_value=10, min_value=-10, start_value=5)
# print("Текущее значение:", counter_custom.current_value())
# counter_custom.increase()
# print("Увеличено значение:", counter_custom.current_value())
# counter_custom.decrease()
# print("Уменьшено значение:", counter_custom.current_value())



#TASK_3
# class Product():
#     def __init__(self,name:str,price:float):
#         self.name=name
#         self.price=price
# class Shop():
#     def __init__(self):
#         self.products=[]
#     def find(self,name:str)->None:
#         '''Searches  for a product in the list'''
#         for product in self.products:
#             if product.name==name:
#                 print(f'Продукт {name} есть в магазине')
#                 return
#         print(f'Продукт {name} не найден')
#
#     def add_prod(self,product:Product)->None:
#         '''Adds a product to the store'''
#         if product not in self.products:
#             self.products.append(product)
#             print(f'Продукт {product.name} добавлен в магазин')
#         else:
#             print(f'Продукт {product.name} уже есть в магазине')
#
#     def delete_prod(self,name:str)->None:
#         '''Removes a product from the store'''
#         for product in self.products:
#             if product.name == name:
#                 self.products.remove(product)
#                 print(f'Продукт {product.name} удален из магазина')
#                 return
#         print(f'Продукт {product.name} не найден')
#     def display_prod(self)->None:
#         '''Displays products on the screen'''
#         print('Список продуктов в магазине:')
#         for product in self.products:
#             print(product.name)
#
# shop=Shop()
# #Добавление продуктов
# product_1=Product('Сыр',8.6)
# product_2=Product('Хлеб',1.8)
# product_3=Product('Молоко',2.9)
# shop.add_prod(product_1)
# shop.add_prod(product_2)
# shop.add_prod(product_3)
# #Поиск продуктов
# shop.find('Пиво')
# shop.find('Хлеб')
# #Удаление продуктов
# shop.delete_prod("Молоко")
# #Вывод продуктов на экран
# shop.display_prod()

#TASK_4
# class MoneyBox():
#     def __init__(self,capacity:int):
#         self.capacity =capacity
#         self.money=0
#     def can_add_money(self,money:int)->bool:
#         '''Checks if it is possible to add coins to the MoneyBox'''
#         return self.money+money<= self.capacity
#     def add(self,money:int)->int:
#         '''Adds coins to the MoneyBox'''
#         if self.can_add_money(money):
#             self.money+=money
#             print(f'Добавлено {money} монет. В копилке теперь {self.money} монет')
#         else:
#             print(f'Нельзя добавить {money} монет.В копилке нет места')
#     def display_money(self):
#         '''Displays the number of coins in the MoneyBox'''
#         print(f'В копилке сейчас {self.money} монет')
# moneybox=MoneyBox(capacity=25)
# print(f'Вметимость копилки {moneybox.capacity} монет')
# print(f'Сейчас в копилке {moneybox.money} монет')
# #Добавляем монеты в копилку
# moneybox.add(7)
# moneybox.add(18)
# moneybox.add(1)
# moneybox.display_money()

#TASK_5
# class Product:
#     def __init__(self,name:str,price:float,quantity:int)->None:
#         self.name=name
#         self.price=price
#         self.quantity=quantity
# class Shop:
#     def __init__(self)->None:
#         self.products=[]
#     def add_prod(self,product:Product)->None:
#         '''Adds products to the store'''
#         self.products.append(product)
#         print(f'Продукт {product.name} добавлен в магазин. Стоимость {product.price} руб. Количество {product.quantity} шт.')
#     def find_prod(self,name:str,quantity:int)->None:
#         '''Looking for an item in the store'''
#         for prod in self.products:
#             if prod.name==name and prod.quantity>=quantity:
#                 print(f'Продукт {name} есть в наличии. K оплате {quantity*prod.price} рублей')
#                 prod.quantity -= quantity
#                 return
#         print(f"Товар {name} отсутствует в наличии. Товаровед делает запрос на склад")
# shop=Shop()
# product_1=Product('Тушь',22.6,2)
# product_2=Product('Пудра',32.1,10)
# product_3=Product('Консилер',25.2,7)
# product_4=Product('Хайлайтер',65.8,1)
# product_5=Product('Бронзер',15.2,5)
# product_6=Product('ВВ-крем',76.2,3)
# shop.add_prod(product_1)
# shop.add_prod(product_2)
# shop.add_prod(product_3)
# shop.add_prod(product_4)
# shop.add_prod(product_5)
# shop.add_prod(product_6)
# shop.find_prod('Бронзер',2)


















