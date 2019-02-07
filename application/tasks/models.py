from application import db
from application.models import Base

from sqlalchemy.sql import text

tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('task_id', db.Integer, db.ForeignKey('task.id'), primary_key=True)
)

class Task(Base):
    __tablename__ = 'task'

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(1000))
    done = db.Column(db.String(144))

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
        backref=db.backref('tasks', lazy=True))

    def __init__(self, name):#, description, done):
        self.name = name
#        self.description = description
#        self.done = done

    @staticmethod
    def find_user(id):
        print("kutsutaan find user")
        stmt = text("SELECT Account.name FROM Account WHERE (Account.id = 1);").params(id=id)
        res = db.engine.execute(stmt)
        print("printataan res", res)
        response = []
        for row in res:
            response.append({"name":row[0]})
        print("printataan response", response)

        return response