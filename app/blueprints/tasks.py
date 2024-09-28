
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Task
from app.extensions import db
from app.forms import TaskForm

tasks_bp = Blueprint('tasks', __name__, template_folder='../templates')

@tasks_bp.route('/tasks', methods=['GET', 'POST'])
def manage_tasks():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, priority=form.priority.data, due_date=form.due_date.data)
        db.session.add(task)
        db.session.commit()
        flash('Task added successfully.')
        return redirect(url_for('tasks.manage_tasks'))
    
    tasks = Task.query.all()
    return render_template('tasks.html', form=form, tasks=tasks)

@tasks_bp.route('/tasks/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted successfully.')
    return redirect(url_for('tasks.manage_tasks'))
