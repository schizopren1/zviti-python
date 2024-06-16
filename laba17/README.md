Лабораторна робота №16: Advanced TODO List
___
Мета роботи:Task 1: 

___
Опис завдання:
```Python
Create Task Class
Create a Python class named Task with the following attributes:
title
description
due_date (use datetime.date )
Example of class usage:
Task 2: Add Method to Task Class
Add a method named is_due_today() to the Task class that checks if the task is due today and returns a boolean.
Example of class usage:
 
from datetime import date
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
from datetime import date
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today())
task.is_due_today()  # Expected output: True if today is the due
date
Task 3: Create Schedule Class
Create a class named Schedule that manages multiple tasks. It should have the following methods:
add_task(task: Task)
      remove_task(task_title: str)
     get_task(task_title: str) -> Task
Example of class usage:
  schedule = Schedule()
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task)
schedule.get_task("Buy groceries")  # Expected output: Task
object
Task 4: List Overdue Tasks
Add a method named list_overdue_tasks() to the Schedule class that returns a list of tasks that are overdue.
Example of class usage:
   from datetime import date, timedelta
schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today() - timedelta(days=1))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date.today() + timedelta(days=2))
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_overdue_tasks()  # Expected output: [task1]
Task 5: List Tasks Due Today
Add a method named list_tasks_due_today() to the Schedule class that returns a list of tasks that are due today.
Example of class usage:
   from datetime import date
schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today())

 task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date.today())
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_tasks_due_today()  # Expected output: [task1,
task2]
Task 6: Sort Tasks by Due Date
Add a method named sort_tasks_by_due_date() to the Schedule class that returns a list of tasks sorted by their due dates.
Example of class usage:
   from datetime import date, timedelta
schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today() + timedelta(days=2))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date.today() + timedelta(days=1))
schedule.add_task(task1)
schedule.add_task(task2)
schedule.sort_tasks_by_due_date()  # Expected output: [task2,
task1]
Task 7: Update Task
Add a method named update_task(task_title: str, **kwargs) to the Schedule class that updates the attributes of a task.
Example of class usage:
   schedule = Schedule()
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task)
schedule.update_task("Buy groceries", description="Milk, Bread,
Eggs, Cheese", due_date=date(2024, 5, 26))
schedule.get_task("Buy groceries")  # Expected output: Task
object with updated attributes

Task 8: Task Status
Add a status attribute to the class which can be 'Pending', 'In Progress', or
  'Completed'. Modify Task and Example of class usage:
to handle task status updates.
 task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Pending")
schedule = Schedule()
schedule.add_task(task)
task.status = "In Progress"
schedule.update_task("Buy groceries", status="Completed")
schedule.get_task("Buy groceries").status  # Expected output:
"Completed"
Task 9: Weekly Schedule
Create a method weekly_schedule(start_date: date) in the Schedule class that returns a list of tasks for the week starting from the provided date.
Example of class usage:
   from datetime import date, timedelta
schedule = Schedule()
task1 = Task(title="Task 1", description="First task",
due_date=date(2024, 5, 21))
task2 = Task(title="Task 2", description="Second task",
due_date=date(2024, 5, 23))
schedule.add_task(task1)
schedule.add_task(task2)
start_date = date(2024, 5, 20)
schedule.weekly_schedule(start_date)  # Expected output: [task1,
task2]
Task 10: Monthly Schedule
Create a method monthly_schedule(year: int, month: int) in the Schedule class that returns a list of tasks for the specified month.
  Example of class usage:
Task
 Schedule

 from datetime import date
schedule = Schedule()
task1 = Task(title="Task 1", description="First task",
due_date=date(2024, 5, 21))
task2 = Task(title="Task 2", description="Second task",
due_date=date(2024, 6, 1))
schedule.add_task(task1)
schedule.add_task(task2)
schedule.monthly_schedule(2024, 5)  # Expected output: [task1]
Task 11: Task Priority
Add a priority attribute to the Task class which can be 'Low', 'Medium', or 'High'. Modify Task and Schedule to handle task priority.
Example of class usage:
Task 12: List Tasks by Priority
Add a method list_tasks_by_priority(priority: str) to the Schedule class that returns a list of tasks with the specified priority.
Example of class usage:
    task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), priority="High")
schedule = Schedule()
schedule.add_task(task)
task.priority  # Expected output: "High"
   task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), priority="High")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), priority="Low")
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_tasks_by_priority("High")  # Expected output:
[task1]

Task 13: Save Schedule to File
Add a method save_to_file(filename: str) to the Schedule class that saves the schedule to a file.
Example of class usage:
Task 14: Load Schedule from File
Add a method load_from_file(filename: str) to the Schedule class that loads the schedule from a file.
   schedule = Schedule()
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task)
schedule.save_to_file("schedule.txt")
  Example of class usage:
Task 15: Task Notes
Add a notes attribute to the the task. Modify Task and
Example of class usage:
class that can store additional information about to handle task notes.
 schedule = Schedule()
schedule.load_from_file("schedule.txt")
 Task
  Schedule
 task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), notes="Use the discount
coupon")
schedule = Schedule()
schedule.add_task(task)
task.notes  # Expected output: "Use the discount coupon"
Task 16: List Tasks with Notes
Add a method list_tasks_with_notes() to the Schedule class that returns a list of tasks that have notes.
  
Example of class usage:
 task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), notes="Use the discount
coupon")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_tasks_with_notes()  # Expected output: [task1]
Task 17: Mark Task as Completed
Add a method mark_as_completed(task_title: str) to the Schedule class that marks the specified task as completed.
Example of class usage:
   task = Task(title="Buy groceries", description="Milk, Bread, Eggs
", due_date=date(2024, 5, 25))
schedule = Schedule()
schedule.add_task(task)
schedule.mark_as_completed("Buy groceries")
task.status  # Expected output: "Completed"
Task 18: List Completed Tasks
Add a method list_completed_tasks() to the Schedule class that returns a list of completed tasks.
Example of class usage:
   task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Completed")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), status="Pending")
schedule = Schedule()
schedule.add_task(task1)

 schedule.add_task(task2)
schedule.list_completed_tasks()  # Expected output: [task1]
Task 19: Find Task by Keyword
Add a method find_task_by_keyword(keyword: str) to the Schedule class that returns a list of tasks that contain the specified keyword in their title or description.
Example of class usage:
   task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.find_task_by_keyword("assignment")  # Expected output:
[task2]
Task 20: Task Deadline Notification
Add a method check_deadlines() to the Schedule class that returns a list of tasks that are due in the next 24 hours.
Example of class usage:
   from datetime import datetime, timedelta
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=datetime.now().date() + timedelta(days=1))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=datetime.now().date() + timedelta(days=2))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.check_deadlines()  # Expected output: [task1]
Task 21: List All Tasks

  Add a method list_all_tasks() to the Schedule class that returns a list of all tasks.
Example of class usage:
 task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_all_tasks()  # Expected output: [task1, task2]
Task 22: Task Duration
Add a duration attribute to the class which specifies the expected time to complete the task in hours. Modify and Schedule to handle task duration.
Example of class usage:
Task 23: List Tasks by Duration
Add a method
int) to the class that returns a list of tasks whose duration falls within
the specified range.
Example of class usage:
 Task
  Task
 task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), duration=2)
schedule = Schedule()
schedule.add_task(task)
task.duration  # Expected output: 2
 list_tasks_by_duration(min_duration: int, max_duration:
  Schedule
 task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), duration=2)
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), duration=4)
schedule = Schedule()
schedule.add_task(task1)

 schedule.add_task(task2)
schedule.list_tasks_by_duration(1, 3)  # Expected output: [task1]
Task 24: Task History
Add a method task_history() to the Schedule class that returns a history of tasks added, removed, and updated in the schedule.
Example of class usage:
   schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task1)
schedule.remove_task("Buy groceries")
schedule.task_history()  # Expected output: [("added", task1),
("removed", task1)]
Task 25: Clear Completed Tasks
Add a method clear_completed_tasks() to the Schedule class that removes all completed tasks from the schedule.
Example of class usage:
   task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Completed")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), status="Pending")
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.clear_completed_tasks()
schedule.list_all_tasks()  # Expected output: [task2]
Task 26: Task Recurrence
Add a recurrence attribute to the   class that specifies if the task is recurring (daily, weekly, monthly). Modify   and Schedule to handle task recurrence.
Task
 Example of class usage:
Task

 task = Task(title="Water plants", description="Water the plants
in the garden", due_date=date(2024, 5, 25), recurrence="weekly")
schedule = Schedule()
schedule.add_task(task)
task.recurrence  # Expected output: "weekly"
Task 27: List Recurring Tasks
Add a method list_recurring_tasks() to the Schedule class that returns a list of recurring tasks.
Example of class usage:
   task1 = Task(title="Water plants", description="Water the plants
in the garden", due_date=date(2024, 5, 25), recurrence="weekly")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_recurring_tasks()  # Expected output: [task1]
Task 28: Task Reminders
Add a method set_reminder(task_title: str, reminder_date: date) to the Schedule class that sets a reminder for a specific task.
Example of class usage:
   task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule = Schedule()
schedule.add_task(task)
schedule.set_reminder("Buy groceries", date(2024, 5, 24))
 Task 29: Task Completion Percentage
Add a method completion_percentage() to the Schedule class that returns the percentage of completed tasks.
  
Example of class usage:
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Completed")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), status="Pending")
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.completion_percentage()  # Expected output: 50.0
Task 30: Task Dependency
Add a dependencies attribute to the Task class that specifies other tasks that need to be completed before the task can start. Modify Task and Schedule to handle task dependencies.
Example of class usage:
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
task2 = Task(title="Prepare breakfast", description="Use
groceries to prepare breakfast", due_date=date(2024, 5, 26),
dependencies=[task1])
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
task2.dependencies  # Expected output: [task1]
```
___
Виконання роботи:
```Python
from datetime import date, datetime, timedelta

class Task:
    def __init__(self, title, description, due_date, status="Pending", priority="Medium", notes=None, duration=0, recurrence=None, dependencies=[]):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self.priority = priority
        self.notes = notes
        self.duration = duration
        self.recurrence = recurrence
        self.dependencies = dependencies

    def is_due_today(self):
        return self.due_date == date.today()

class Schedule:
    def __init__(self):
        self.tasks = []
        self.history = []

    def add_task(self, task):
        self.tasks.append(task)
        self.history.append(("added", task))

    def remove_task(self, task_title):
        task = self.get_task(task_title)
        if task:
            self.tasks.remove(task)
            self.history.append(("removed", task))

    def get_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                return task
        return None

    def list_overdue_tasks(self):
        return [task for task in self.tasks if task.due_date < date.today()]

    def list_tasks_due_today(self):
        return [task for task in self.tasks if task.is_due_today()]

    def sort_tasks_by_due_date(self):
        self.tasks.sort(key=lambda task: task.due_date)
        return self.tasks

    def update_task(self, task_title, **kwargs):
        task = self.get_task(task_title)
        if task:
            for attr, value in kwargs.items():
                setattr(task, attr, value)
            self.history.append(("updated", task))

    def weekly_schedule(self, start_date):
        end_date = start_date + timedelta(days=6)
        return [task for task in self.tasks if start_date <= task.due_date <= end_date]

    def monthly_schedule(self, year, month):
        month_start = date(year, month, 1)
        next_month = month + 1 if month < 12 else 1
        next_year = year + 1 if next_month == 1 else year
        month_end = date(next_year, next_month, 1) - timedelta(days=1)
        return [task for task in self.tasks if month_start <= task.due_date <= month_end]

    def list_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.title},{task.description},{task.due_date},{task.status},{task.priority},{task.notes},{task.duration},{task.recurrence},{','.join([d.title for d in task.dependencies])}\n")

    def load_from_file(self, filename):
        self.tasks = []
        with open(filename, "r") as file:
            for line in file:
                task_data = line.strip().split(",")
                title = task_data[0]
                description = task_data[1]
                due_date = datetime.strptime(task_data[2], "%Y-%m-%d").date()
                status = task_data[3]
                priority = task_data[4]
                notes = task_data[5] if task_data[5] else None
                duration = int(task_data[6]) if task_data[6] else 0
                recurrence = task_data[7] if task_data[7] else None
                dependencies = [self.get_task(d) for d in task_data[8].split(",")] if task_data[8] else []
                task = Task(title, description, due_date, status, priority, notes, duration, recurrence, dependencies)
                self.add_task(task)

    def list_tasks_with_notes(self):
        return [task for task in self.tasks if task.notes]

    def mark_as_completed(self, task_title):
        task = self.get_task(task_title)
        if task:
            task.status = "Completed"
            self.history.append(("updated", task))

    def list_completed_tasks(self):
        return [task for task in self.tasks if task.status == "Completed"]

    def find_task_by_keyword(self, keyword):
        return [task for task in self.tasks if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]

    def check_deadlines(self):
        return [task for task in self.tasks if (task.due_date - date.today()).days <= 1]

    def list_all_tasks(self):
        return self.tasks

    def list_tasks_by_duration(self, min_duration, max_duration):
        return [task for task in self.tasks if min_duration <= task.duration <= max_duration]

    def task_history(self):
        return self.history

    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if task.status != "Completed"]

    def list_recurring_tasks(self):
        return [task for task in self.tasks if task.recurrence]

    def set_reminder(self, task_title, reminder_date):
        task = self.get_task(task_title)
        if task:
            task.reminder_date = reminder_date

    def completion_percentage(self):
        completed_tasks = len(self.list_completed_tasks())
        total_tasks = len(self.tasks)
        if total_tasks == 0:
            return 0
        return (completed_tasks / total_tasks) * 100
```
___
Результати:
```Python
Task added: Buy groceries
All tasks: ['Buy groceries']
[<__main__.Task object at 0x103052cc0>]
Task added: Submit assignment
Task updated: Buy groceries
All tasks: ['Buy groceries', 'Submit assignment']
[<__main__.Task object at 0x103052cc0>, <__main__.Task object at 0x103052de0>]
Task marked as completed: Buy groceries
Completed tasks: ['Buy groceries']
[<__main__.Task object at 0x103052cc0>]
Task added: Water plants
Task history: [('added', 'Buy groceries'), ('added', 'Submit assignment'), ('updated', 'Buy groceries'), ('updated', 'Buy groceries'), ('added', 'Water plants')]
[('added', <__main__.Task object at 0x103052cc0>), ('added', <__main__.Task object at 0x103052de0>), ('updated', <__main__.Task object at 0x103052cc0>), ('updated', <__main__.Task object at 0x103052cc0>), ('added', <__main__.Task object at 0x103037b60>)]
Tasks with notes: []
[]
Tasks with priority Medium: ['Buy groceries', 'Submit assignment', 'Water plants']
[<__main__.Task object at 0x103052cc0>, <__main__.Task object at 0x103052de0>, <__main__.Task object at 0x103037b60>]
```
___
Висновки:З цього завдання я можу винести кілька уроків. По-перше, це основи ООП, такі як створення та використання класів, об'єктів, методів і атрибутів. Також важливим є навик роботи з датами, включаючи використання модулів datetime і timedelta для управління датами і часом. У процесі виконання завдання я розвиваю вміння управляти станом, відстежуючи зміни завдань і їхні статуси. Робота з файлами допомагає мені зрозуміти, як читати і записувати дані у файли, а також серіалізувати об'єкти. Крім того, реалізація методів для фільтрації та сортування завдань вчить мене ефективно керувати даними. Використання print для відладки та розуміння виконання програми підкреслює важливість прозорості коду. Ці навички допомагають мені покращити розуміння програмування та розвинути практичні вміння для вирішення реальних завдань.
___