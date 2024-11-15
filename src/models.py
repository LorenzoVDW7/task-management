from datetime import datetime
from utils import *
import uuid

class Task:
    def __init__(self, title: str, description: str, due_date: datetime, date_edited: datetime):
        self.task_id = uuid.uuid4()
        self.title = format_input(title)
        self.description = description
        self.status = "Pending"
        self.due_date = due_date
        self.date_edited = date_edited

    def __str__(self) -> str:
        return (f"ID: {self.task_id}, title: {self.title},\nDescription: {self.description}, status: {self.status},"
                f" date: {self.due_date}, date_edited: {self.date_edited}")

    def mark_completed(self) -> None:
        self.status = "Completed"
        self.date_edited = datetime.now()

    def mark_in_progress(self) -> None:
        self.status = "In progress"
        self.date_edited = datetime.now()

    def update_title(self, new_title) -> None:
        self.title = format_input(new_title)

    def update_due_date(self, new_due_date) -> None:
        self.due_date = new_due_date

    def update_date_edited(self, new_date_edited) -> None:
        self.date_edited = new_date_edited

class TaskManager:
    def __init__(self):
        self.task_list_in_progress = {}
        self.task_list_complete = {}
        self.task_list_pending = {}

    def create_task(self, task: Task) -> str:
        if not self.task_list_pending.get(task.task_id):
            self.task_list_pending[task.title] = task
            return f"Task {task.title} has been created."
        return f"Task {task.title} already exists."



