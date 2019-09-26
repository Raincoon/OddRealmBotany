from application import db
from application.models import Id

class Tag(Id):

    name = db.Column(db.String(50), nullable=False)

    # tag knows its creator, not bidirectional
    owner_id = db.Column(db.Integer,
                         db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
