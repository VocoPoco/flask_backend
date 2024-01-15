import json
import datetime
from models import Task

def test_get_all_tasks(self):
    response = self.client.get('/task')
    self.assertEqual(response.status_code, 200)
    self.assertTrue(isinstance(json.loads(response.data), list))

def test_get_task_by_id(self):
    title = 'Test Task'
    description = 'This is a test task'
    due_date = datetime.date(2023, 12, 31)
    
    new_task = Task(title=title, description=description, due_date=due_date)
    
    response = self.client.get(f'/task/{new_task.id}')
    self.assertEqual(response.status_code, 200)
    
    response = self.client.get('/task/99999')
    self.assertEqual(response.status_code, 404)

def test_add_task(self):
    data = {'title': 'Test Task', 'description': 'This is a test task'}
    response = self.client.post('/task', json=data)
    self.assertEqual(response.status_code, 201)

    task = Task.query.filter_by(title='New Task').first()
    self.assertIsNotNone(task)