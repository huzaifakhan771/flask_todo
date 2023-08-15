from config import db
from flask import abort, make_response
from models import Todos, task_schema, todos_schema


def read_all():
    """
    fetch a list of all tasks
    """
    tasks = Todos.query.all()
    return todos_schema.dump(tasks)


def create(task):
    """
    create a new task
    """
    new_task = task_schema.load(task, session=db.session)
    db.session.add(new_task)
    db.session.commit()
    return task_schema.dump(new_task), 201


def read_one(id_):
    """
    fetch a single task based on its id
    :param id_:
    :return:
    """
    task = Todos.query.filter(Todos.id == id_).one_or_none()

    if task is not None:
        return task_schema.dump(task)
    abort(404, f"Task with id {id_} not found")


def update(id_, task):
    """
    update a task title, description, or status based on its id
    """
    existing_task = Todos.query.filter(Todos.id == id_).one_or_none()

    if existing_task:
        update_task = task_schema.load(task, session=db.session)
        existing_task.title = update_task.title
        existing_task.description = update_task.description
        existing_task.done = update_task.done
        db.session.merge(existing_task)
        db.session.commit()
        return task_schema.dump(existing_task), 201
    abort(404, f"Task with id {id_} not found")


def delete(id_):
    """
    delete a task based on its id
    :param id_:
    :return:
    """
    existing_task = Todos.query.filter(Todos.id == id_).one_or_none()

    if existing_task:
        db.session.delete(existing_task)
        db.session.commit()
        return make_response(f"{id_} successfully deleted", 200)
    abort(404, f"Task with id {id_} not found")
