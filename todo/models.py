from datetime import datetime

from config import db, ma
from sqlalchemy import Column, Integer, String
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(128), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


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
