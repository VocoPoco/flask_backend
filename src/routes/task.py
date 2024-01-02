from flask import Blueprint, jsonify, request
from models import Task, db 

task_view = Blueprint('task_routes', __name__)

@task_view.route('/task', methods=['GET'])
def get_all_tasks():
    tasks = Task.query.all()
    return jsonify([task.serialize() for task in tasks])

@task_view.route('/task/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    task = Task.query.get(task_id)
    if task:
        return jsonify(task.serialize())
    else:
        return jsonify({'error': 'Task not found'}), 404

@task_view.route('/task', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(title=data['title'], description=data['description'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.serialize()), 201
