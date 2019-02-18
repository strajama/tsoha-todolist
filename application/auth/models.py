from application import db
from application.models import Base

from sqlalchemy.sql import text
from sqlalchemy.types import Enum

class User(Base):

    __tablename__ = 'account'
  
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    tasks = db.relationship("Task", backref='account', lazy=True)
    role = db.Column(db.Enum('admin', 'worker', name='roles'), nullable=False, default='admin')

    def __init__(self, name, username, password, role):
        self.name = name
        self.username = username
        self.password = password
        self.role = role
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return self.role

    @staticmethod
    def find_users_with_no_tasks(susanna="kesken"):
        stmt = text("SELECT Account.id, Account.name FROM Account"
                     " LEFT JOIN Task ON Task.account_id = Account.id"
                     " WHERE (Task.usedtime IS null)" # OR Task.usedtime = :tellervo)"
                     " GROUP BY Account.id"
                     " HAVING COUNT(Task.id) = 0").params(tellervo=susanna)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response

    @staticmethod
    def find_users_with_unfinished_tasks(usedtime=0):
        stmt = text("SELECT Account.id, Account.name FROM Account "
                        "LEFT JOIN Task ON Task.account_id = Account.id "
                        "WHERE (Task.usedtime = :usedtime) "
                        "GROUP BY Account.id").params(usedtime=usedtime)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response
