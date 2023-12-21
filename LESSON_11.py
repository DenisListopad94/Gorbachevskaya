#TASK_1
# def fib():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# fibonacci_generator = fib()
# for _ in range(10):
#     print(next(fibonacci_generator))

#TASK_2
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def simple(n):
#     current_number = 2
#     while current_number <= n:
#         if is_prime(current_number):
#             yield current_number
#         current_number += 1
#
# try:
#     n = int(input("Введите число n: "))
#     prime_generator = simple(n)
#     for prime in prime_generator:
#         print(prime)
#
# except ValueError:
#     print("Введите корректное число.")
# except StopIteration:
#     print("Произошло исключение StopIteration: все простые числа до n выведены.")

#TASK_3
# def is_perfect(number):
#     sum = 0
#     for i in range(1, number // 2 + 1):
#         if number % i == 0:
#             sum += i
#     return sum == number
# def perfect_numbers_generator(limit):
#     for num in range(2, limit + 1):
#         if is_perfect(num):
#             yield num
#
# limit = 1000000000
# perfect_gen = perfect_numbers_generator(limit)
# for perfect_num in perfect_gen:
#     print(perfect_num)

#TASK_7
# contacts = {}
# def add_contact(name, *phone_numbers):
#     if name in contacts:
#         contacts[name].extend(phone_numbers)
#     else:
#         contacts[name] = list(phone_numbers)
# def show_numbers(name):
#     if name in contacts:
#         if contacts[name]:
#             print(", ".join(map(str, contacts[name])))
#         else:
#             print("Не найдено")
#     else:
#         print("Не найдено")
#
# add_contact("Ben", "89001234050", "+70504321009")
# add_contact("Alice", "210-220")
# add_contact("Alice", "404-502", "894-005", "439-095")
# add_contact("Nick", "+16507811251")
# add_contact("Alex", "+4(908)273-22-42")
# add_contact("Robert", "51234047129", "92174043215")
# show_numbers("Alice")
# show_numbers("Ben")
# show_numbers("Alex")
# show_numbers("Nick")
# show_numbers("Robert")

#TASK_5
# class Server:
#     def __init__(self):
#         self.strings = []
#
#     def post(self, string):
#         self.strings.append(string)
#         return f"Added: {string}"
#
#     def get(self):
#         if self.strings:
#             return self.strings[-1]
#         else:
#             return "Nothing to retrieve"
#
#     def delete(self):
#         if self.strings:
#             deleted_string = self.strings.pop()
#             return f"Deleted: {deleted_string}"
#         else:
#             return "Nothing to delete"
#
#
# server = Server()
#
# commands = [
#     "POST 12",
#     "POST 15",
#     "POST 81",
#     "GET",
#     "DELETE",
#     "DELETE",
#     "POST Stack Overflow",
#     "POST Recursion",
#     "DELETE",
#     "GET",
# ]
#
# for command in commands:
#     parts = command.split()
#     if parts[0] == "POST":
#         string = " ".join(parts[1:])
#         print(server.post(string))
#     elif command == "GET":
#         print(server.get())
#     elif command == "DELETE":
#         print(server.delete())
#
# print(" ".join(server.strings))

#TASK_4
# def process_string(input_str):
#     start_index = input_str.find('{')
#     if start_index != -1:
#         end_index = input_str.find('}')
#         if end_index != -1:
#             output_str = input_str[:start_index] + input_str[end_index + 1:]
#         else:
#             output_str = input_str[:start_index]
#     else:
#         output_str = input_str
#
#     most_common_char = max(output_str, key=lambda x: output_str.count(x) if x != ' ' else 0)
#
#     return output_str, most_common_char
#
#
# input_string = "This is a {sample} string with some {random} groups of characters."
# result, most_common_character = process_string(input_string)
# print("Обработанная строка:", result)
# print("Наиболее часто встречающийся символ:", most_common_character)