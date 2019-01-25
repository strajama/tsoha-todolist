from application import db

class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(1000))
    done = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('Account.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name
        self.done = 0
