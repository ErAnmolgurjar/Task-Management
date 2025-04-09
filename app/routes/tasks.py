from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Task

task_bp = Blueprint('tasks', __name__)

# 🔸 Create Task
@task_bp.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    title = data.get('title')
    if not title:
        return jsonify({"msg": "Title is required"}), 400

    new_task = Task(
        title=title,
        description=data.get('description', ''),
        status=data.get('status', 'pending'),
        user_id=user_id
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"msg": "Task created", "task_id": new_task.id}), 201

# 🔸 Get All Tasks for Logged-in User
@task_bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    output = [{
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status
    } for task in tasks]
    return jsonify(output), 200

# 🔸 Update Task
@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])
@jwt_required()
def update_task(task_id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        return jsonify({"msg": "Task not found"}), 404

    data = request.get_json()
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.status = data.get('status', task.status)
    db.session.commit()

    return jsonify({"msg": "Task updated"}), 200

# 🔸 Delete Task
@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        return jsonify({"msg": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"msg": "Task deleted"}), 200
