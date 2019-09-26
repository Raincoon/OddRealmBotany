from application import db

class Id(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)