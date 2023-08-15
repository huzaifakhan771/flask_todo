from datetime import datetime

from config import db, ma


class Todos(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32))
    description = db.Column(db.String(120))
    done = db.Column(db.Boolean, default=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class TodosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Todos
        load_instance = True
        sqla_session = db.session


task_schema = TodosSchema()
todos_schema = TodosSchema(many=True)
