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
            response.append({"id":row[0], "name":row[1]})

        return response
