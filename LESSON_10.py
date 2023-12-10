#TASK_1
# from datetime import datetime
# class Task:
#     def __init__(self,description:str,deadline:datetime):
#         self.description = description
#         self.deadline = deadline
#         self.status = False
#     def mark_as_done(self)->None:
#         '''Marks the task as done'''
#         self.status = True
#
# class Project:
#     def __init__(self,name:str,tasks:list)->None:
#         self.name = name
#         self.tasks=tasks
#     def add_task(self,task:Task)->None:
#         ''' Adds a task to the project'''
#         self.tasks.append(task)
#     def show_tasks(self)->None:
#         '''Displays the tasks in the project'''
#         print(f'Задачи в проекте {self.name}:')
#         for task in self.tasks:
#             status_str = "выполнена" if task.status else "не выполнена"
#             print(f'{task.description} (до {task.deadline}): {status_str}')
#
# class ProjectManager:
#     def __init__(self):
#         self.projects=[]
#     def create_proj(self, name:str, tasks:list=None)->None:
#         '''Creates a new project'''
#         project = Project(name, tasks if tasks else [])
#         self.projects.append(project)
#         return project
#
# manager=ProjectManager()
# progect_1=manager.create_proj('Проект №1')
# task_1=Task('Разработка А',datetime(2023,12,18))
# task_2=Task('Тестирование А',datetime(2023,12,25))
# task_3=Task('Релиз А',datetime(2023,12,30))
# progect_1.add_task(task_1)
# progect_1.add_task(task_2)
# progect_1.add_task(task_3)
# task_1.mark_as_done()
# progect_1.show_tasks()

#TASK_2
# class Passenger:
#     def __init__(self,name:str,surname:str):
#         self.name=name
#         self.surname = surname
# class Ticket:
#     def __init__(self, passanger:Passenger,route:str):
#         self.passanger = passanger
#         self.route = route
# class Flight:
#     def __init__(self, name:str, route:str):
#         self.name = name
#         self.route = route
#         self.tickets = []
#     def reserve_ticket(self,passanger:Passenger):
#         '''Reserves a ticket for the given passenger on the flight'''
#         ticket=Ticket(passanger,self.route)
#         self.tickets.append(ticket)
#         return ticket
#     def remove_ticket(self,ticket:Ticket)->None:
#         '''Removes a ticket from the list of reserved tickets on the flight'''
#         self.tickets.remove(ticket)
#
#     def show_tickets(self)->None:
#         '''Displays the list of reserved tickets on the flight'''
#         print(f'Зарезервированные билеты на рейсе {self.name}:')
#         for ticket in self.tickets:
#             print(f'{ticket.passanger.name} {ticket.passanger.surname} - {ticket.route}')
# class Airline:
#     def __init__(self, name:str):
#         self.name = name
#         self.flights = []
#
#     def create_flight(self, name:str, route:str)-> Flight:
#         '''Creates a new flight for the airline'''
#         flight = Flight(name, route)
#         self.flights.append(flight)
#         return flight
# airline=Airline('Pegasus')
# flight_1=Flight('AA01HY','Tbilisi - Abu Dhabi')
# flight_2=Flight('B76HUT','Batumi - Moscow')
# passenger_1=Passenger('Ivan','Butsko')
# passenger_2=Passenger('Yuliya','Harbacheuskaya')
# ticket_1=flight_1.reserve_ticket(passenger_1)
# ticket_2=flight_2.reserve_ticket(passenger_2)
# flight_1.show_tickets()
# flight_2.show_tickets()

#TASK_3 - Вы сказали, что разберем на занятии














