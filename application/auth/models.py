from application import db
from application.models import Base

from sqlalchemy.sql import text
from sqlalchemy.types import Enum
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy import Enum

class User(Base):

    __tablename__ = 'account'
  
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    tasks = db.relationship("Task", backref='account', lazy=True)
    role = db.Column('role', db.Enum('admin', 'worker', name='role', create_type=False), nullable=False, default='admin')

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
        print('tulostetaan rooli')
        print(self.role)
        return [str(self.role)]

    @staticmethod
    def find_users_with_no_tasks(susanna="kesken"):
        stmt = text("SELECT Account.id, Account.name, Account.role FROM Account"
                     " LEFT JOIN Task ON Task.account_id = Account.id"
                     " WHERE (Task.usedtime IS null)" # OR Task.usedtime = :tellervo)"
                     " GROUP BY Account.id"
                     " HAVING COUNT(Task.id) = 0").params(tellervo=susanna)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "role":row[2]})

        return response

    @staticmethod
    def find_users_with_unfinished_tasks(usedtime=0):
        stmt = text("SELECT Account.id, Account.name, Account.role FROM Account "
                        "LEFT JOIN Task ON Task.account_id = Account.id "
                        "WHERE (Task.usedtime = :usedtime) "
                        "GROUP BY Account.id").params(usedtime=usedtime)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "role":row[2]})

        return response
