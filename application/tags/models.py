from application import db
from application.models import Base
from application.tasks.models import tagtask

from sqlalchemy.sql import text


class Tag(Base):
    __tablename__ = 'tag'

    name = db.Column(db.String(144), nullable=False)

    tasks = db.relationship('Task', secondary=tagtask, back_populates='tags')

    def __init__(self, name):
        self.name = name

    @staticmethod
    def find_tags_that_assigned_task():
        stmt=text("SELECT Tag.id AS id, Tag.name AS name FROM Tag "
                    "INNER JOIN Tagtask ON Tag.id=Tagtask.tag_id "
                    "INNER JOIN Task ON Tagtask.task_id=Task.id;")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            if {"id":row[0], "name":row[1]} not in response:
                response.append({"id":row[0], "name":row[1]})

        return response

    @staticmethod
    def find_most_used_tags():
        stmt=text("SELECT Tag.name, COUNT(*), SUM (Task.used_time) FROM Tag "
                    "INNER JOIN Tagtask ON Tagtask.tag_id = Tag.id "
                    "INNER JOIN Task ON Task.id = Tagtask.task_id "
                    "GROUP BY Tag.name;")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "count":row[1], "sum":row[2]})

        return response
