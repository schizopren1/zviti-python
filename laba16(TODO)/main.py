
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
        print(f"Task added: {task.title}")

    def remove_task(self, task_title):
        task = self.get_task(task_title)
        if task:
            self.tasks.remove(task)
            self.history.append(("removed", task))
            print(f"Task removed: {task.title}")
        else:
            print(f"Task not found: {task_title}")

    def get_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                return task
        print(f"Task not found: {task_title}")
        return None

    def list_overdue_tasks(self):
        overdue_tasks = [task for task in self.tasks if task.due_date < date.today()]
        print(f"Overdue tasks: {[task.title for task in overdue_tasks]}")
        return overdue_tasks

    def list_tasks_due_today(self):
        tasks_due_today = [task for task in self.tasks if task.is_due_today()]
        print(f"Tasks due today: {[task.title for task in tasks_due_today]}")
        return tasks_due_today

    def sort_tasks_by_due_date(self):
        self.tasks.sort(key=lambda task: task.due_date)
        print(f"Tasks sorted by due date: {[task.title for task in self.tasks]}")
        return self.tasks

    def update_task(self, task_title, **kwargs):
        task = self.get_task(task_title)
        if task:
            for attr, value in kwargs.items():
                setattr(task, attr, value)
            self.history.append(("updated", task))
            print(f"Task updated: {task.title}")
        else:
            print(f"Task not found: {task_title}")

    def weekly_schedule(self, start_date):
        end_date = start_date + timedelta(days=6)
        weekly_tasks = [task for task in self.tasks if start_date <= task.due_date <= end_date]
        print(f"Weekly schedule from {start_date} to {end_date}: {[task.title for task in weekly_tasks]}")
        return weekly_tasks

    def monthly_schedule(self, year, month):
        month_start = date(year, month, 1)
        next_month = month + 1 if month < 12 else 1
        next_year = year + 1 if next_month == 1 else year
        month_end = date(next_year, next_month, 1) - timedelta(days=1)
        monthly_tasks = [task for task in self.tasks if month_start <= task.due_date <= month_end]
        print(f"Monthly schedule for {year}-{month}: {[task.title for task in monthly_tasks]}")
        return monthly_tasks

    def list_tasks_by_priority(self, priority):
        tasks_by_priority = [task for task in self.tasks if task.priority == priority]
        print(f"Tasks with priority {priority}: {[task.title for task in tasks_by_priority]}")
        return tasks_by_priority

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.title},{task.description},{task.due_date},{task.status},{task.priority},{task.notes},{task.duration},{task.recurrence},{','.join([d.title for d in task.dependencies])}\n")
        print(f"Tasks saved to {filename}")

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
        print(f"Tasks loaded from {filename}")

    def list_tasks_with_notes(self):
        tasks_with_notes = [task for task in self.tasks if task.notes]
        print(f"Tasks with notes: {[task.title for task in tasks_with_notes]}")
        return tasks_with_notes

    def mark_as_completed(self, task_title):
        task = self.get_task(task_title)
        if task:
            task.status = "Completed"
            self.history.append(("updated", task))
            print(f"Task marked as completed: {task.title}")
        else:
            print(f"Task not found: {task_title}")

    def list_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if task.status == "Completed"]
        print(f"Completed tasks: {[task.title for task in completed_tasks]}")
        return completed_tasks

    def find_task_by_keyword(self, keyword):
        tasks_with_keyword = [task for task in self.tasks if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]
        print(f"Tasks with keyword '{keyword}': {[task.title for task in tasks_with_keyword]}")
        return tasks_with_keyword

    def check_deadlines(self):
        deadlines = [task for task in self.tasks if (task.due_date - date.today()).days <= 1]
        print(f"Tasks with upcoming deadlines: {[task.title for task in deadlines]}")
        return deadlines

    def list_all_tasks(self):
        print(f"All tasks: {[task.title for task in self.tasks]}")
        return self.tasks

    def list_tasks_by_duration(self, min_duration, max_duration):
        tasks_by_duration = [task for task in self.tasks if min_duration <= task.duration <= max_duration]
        print(f"Tasks with duration between {min_duration} and {max_duration} minutes: {[task.title for task in tasks_by_duration]}")
        return tasks_by_duration

    def task_history(self):
        print(f"Task history: {[(action, task.title) for action, task in self.history]}")
        return self.history

    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if task.status != "Completed"]
        print("Completed tasks cleared")

    def list_recurring_tasks(self):
        recurring_tasks = [task for task in self.tasks if task.recurrence]
        print(f"Recurring tasks: {[task.title for task in recurring_tasks]}")
        return recurring_tasks

    def set_reminder(self, task_title, reminder_date):
        task = self.get_task(task_title)
        if task:
            task.reminder_date = reminder_date
            print(f"Reminder set for task '{task.title}' on {reminder_date}")
        else:
            print(f"Task not found: {task_title}")

    def completion_percentage(self):
        completed_tasks = len(self.list_completed_tasks())
        total_tasks = len(self.tasks)
        if total_tasks == 0:
            print("No tasks available.")
            return 0
        percentage = (completed_tasks / total_tasks) * 100
        print(f"Completion percentage: {percentage:.2f}%")
        return percentage

# Пример использования:
schedule = Schedule()

# Добавление задач
task1 = Task(title='Buy groceries', description='Milk, Bread, Eggs', due_date=datetime(2024, 6, 5).date())
schedule.add_task(task1)

# Вывод всех задач
all_tasks = schedule.list_all_tasks()
print(all_tasks)

# Добавление еще одной задачи
task2 = Task(title='Submit assignment', description='Math assignment', due_date=datetime(2024, 6, 8).date())
schedule.add_task(task2)

# Обновление задачи
schedule.update_task('Buy groceries', description='Milk, Bread, Eggs, Cheese', due_date=datetime(2024, 5, 26).date(), status='Completed')

# Список всех задач
all_tasks = schedule.list_all_tasks()
print(all_tasks)

# Завершение задачи
schedule.mark_as_completed('Buy groceries')

# Список завершенных задач
completed_tasks = schedule.list_completed_tasks()
print(completed_tasks)

# Добавление задачи с заметками
task3 = Task(title='Water plants', description='Water the plants in the garden', due_date=datetime(2024, 5, 25).date(), duration=2)
schedule.add_task(task3)

# История задач
history = schedule.task_history()
print(history)

# Вывод задач с заметками
tasks_with_notes = schedule.list_tasks_with_notes()
print(tasks_with_notes)

# Список всех задач по приоритету
tasks_by_priority = schedule.list_tasks_by_priority('Medium')
print(tasks_by_priority)

# Установка напоминания
schedule.set