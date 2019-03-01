from application import db
from application.models import Base
from application.tasks.models import tagtask

from sqlalchemy.sql import text


class Tag(Base):
    __tablename__ = 'tag'

    name = db.Column(db.String(30), nullable=False, unique=True)

    tasks = db.relationship('Task', secondary=tagtask, back_populates='tags')

    def __init__(self, name):
        self.name = name

    @staticmethod
    def find_used_tags():
        stmt=text("SELECT Tag.name, COUNT(*), SUM (Task.used_time) FROM Tag "
                    "INNER JOIN Tagtask ON Tagtask.tag_id = Tag.id "
                    "INNER JOIN Task ON Task.id = Tagtask.task_id "
                    "GROUP BY Tag.name "
                    "LIMIT (10);")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "count":row[1], "sum":row[2]})

        return response

    @staticmethod
    def unique_name(name=name):
        stmt = text("SELECT COUNT(*) FROM Tag "
                        "WHERE (Tag.name = :name) "
                        "GROUP BY Tag.name").params(name=name)
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({"count":row[0]})
        return response
