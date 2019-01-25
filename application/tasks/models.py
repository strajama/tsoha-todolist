from application import db

class Task(db.Model):
#    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(1000))
    done = db.Column(db.String(144))

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name):#, description, done):
        self.name = name
#        self.description = description
#        self.done = done
