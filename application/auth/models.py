from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):
    __tablename__ = 'account'
  
    name = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    tasks = db.relationship("Task", backref='account', lazy=True)

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
        return [self.role]

    def printpassword(self):
        return "*" * len(self.password)
        
    @staticmethod
    def find_users_with_no_tasks(susanna="kesken"):
        stmt = text("SELECT Account.id, Account.name FROM Account"
                     " LEFT JOIN Task ON Task.account_id = Account.id"
                     " WHERE (Task.used_time == 0)" # OR Task.usedtime = :tellervo)"
                     " GROUP BY Account.id"
                     " HAVING COUNT(Task.id) = 0").params(tellervo=susanna)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})
        return response

    @staticmethod
    def find_users_with_unstarted_tasks(used_time=0):
        stmt = text("SELECT Account.id, Account.name FROM Account "
                        "LEFT JOIN Task ON Task.account_id = Account.id "
                        "WHERE (Task.used_time = :used_time) "
                        "GROUP BY Account.id").params(used_time=used_time)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})
        return response

    @staticmethod
    def find_number_of_tasks_by_user_roles():
        stmt = text("SELECT Account.role, COUNT(*) FROM Account "
                        "INNER JOIN Task ON Task.account_id = Account.id "
                        "GROUP BY Account.role "
                        "ORDER BY Account.role DESC;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "count":row[1]})
        return response

    @staticmethod
    def unique_username(username=username):
        stmt = text("SELECT COUNT(*) FROM Account "
                        "WHERE (Account.username = :username) "
                        "GROUP BY Account.username").params(username=username)
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({"count":row[0]})
        return response