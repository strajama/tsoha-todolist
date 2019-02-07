from application import db
from application.models import Base



class Tag(Base):
    __tablename__ = 'tag'

    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name


