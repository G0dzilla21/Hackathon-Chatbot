from .db import db, environment, SCHEMA

class TableData(db.Model):
    __tablename__ = 'table_data'

    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    field_type = db.Column(db.String(255), nullable=False)
    nullable = db.Column(db.Boolean, nullable=False)
    keys = db.Column(db.String(255))
    default = db.Column(db.String(255))
    extra = db.Column(db.String(255))
    schema_id = db.Column(db.Integer, db.ForeignKey('schemas.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'field_type': self.field_type,
            'nullable': self.nullable,
            'keys': self.keys,
            'default': self.default,
            'extra': self.extra,
            'schema_id': self.schema_id
        }