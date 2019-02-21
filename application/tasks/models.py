from application import db
from application.models import Base

from sqlalchemy.sql import text

tagtask = db.Table('tagtask',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('task_id', db.Integer, db.ForeignKey('task.id'), primary_key=True)
)

class Task(Base):
    __tablename__ = 'task'

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(1000))
    estimated_time = db.Column(db.Integer())
    used_time = db.Column(db.Integer())
    username = db.Column(db.String(144))

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    tags = db.relationship('Tag', secondary='tagtask', back_populates='tasks')

    def __init__(self, name, description, estimated_time):
        self.name = name
        self.description = description
        self.estimated_time = estimated_time

    @staticmethod
    def find_user(id):
        stmt = text("SELECT Account.name FROM Account WHERE (Account.id = :id);").params(id=id)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"name":row[0]})

        return response
