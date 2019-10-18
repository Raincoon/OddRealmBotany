from application import db
from application.models import Base
from application.tags.models import Tag

from sqlalchemy.sql import text

# helper/association table, fin.liitostaulu
helper = db.Table('plant_tag_helper',
    db.Column("plant_id", db.Integer, db.ForeignKey('plant.id')),
    db.Column("tag_id", db.Integer, db.ForeignKey('tag.id'))
)

class Plant(Base):

    name = db.Column(db.String(50), nullable=False)
    mature_time = db.Column(db.Integer, nullable=False)
    is_tree = db.Column(db.Boolean, nullable=False)

    # plant knows its creator and tags, not bidirectional
    owner_id = db.Column(db.Integer,
                         db.ForeignKey('account.id'), nullable=False)
    tags = db.relationship("Tag",
                            secondary=helper, lazy='subquery',
                            backref="plants")

    def __init__(self, name, grow_time_hrs, is_tree=False):
        self.name = name
        self.mature_time = grow_time_hrs
        self.is_tree = is_tree
    
    def is_owner(self, user_id):
        return user_id == self.owner_id

    @staticmethod
    def count_tags_on_plants(user_id):
        stmt = text("SELECT COUNT(Plant.id) FROM Plant "
                    "JOIN plant_tag_helper "
                    "ON Plant.id = plant_tag_helper.plant_id"
                    " WHERE Plant.owner_id = :id").params(id=user_id)
        result = db.engine.execute(stmt)
        
        # get the integer from result
        for row in result:
            response = row[0]
        return response