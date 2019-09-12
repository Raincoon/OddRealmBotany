from application import db

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    mature_time = db.Column(db.Integer, nullable=False)
    is_tree = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, grow_time_hrs, is_tree=False):
        self.name = name
        self.mature_time = grow_time_hrs
        # defaults to False
        self.is_tree = is_tree