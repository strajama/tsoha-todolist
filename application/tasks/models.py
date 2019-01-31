from application import db
from application.models import Base

class Task(Base):
    __tablename__ = 'task'

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(1000))
    done = db.Column(db.String(144))

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name):#, description, done):
        self.name = name
#        self.description = description
#        self.done = done
