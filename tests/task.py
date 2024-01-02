from datetime import datetime
from models import Task


def test_create_task_with_extended_data(self):
    title = "Test Task"
    description = "This is a test task"
    due_date = datetime.date(2023, 12, 31)
    
    new_task = Task(title=title, description=description, due_date=due_date)
    
    self.assertEqual(new_task.title, title)
    self.assertEqual(new_task.description, description)
    self.assertEqual(new_task.due_date, due_date)
    self.assertEqual(new_task.state, 'TODO')
