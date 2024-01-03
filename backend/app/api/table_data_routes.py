from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import db, TableData

table_data_routes = Blueprint('table_data', __name__)

# Get all
@table_data_routes.route('/')
@login_required
def get_all_table_data():
    table_data = TableData.query.all()
    return {'table_data': [td.to_dict() for td in table_data]}

# Get by Id
@table_data_routes.route('/<int:id>')
@login_required
def get_table_data_by_id(id):
    table_data = TableData.query.get(id)
    return table_data.to_dict()

# Create
@table_data_routes.route('/', methods = ['POST'])
@login_required
def create_table_data():
    data = request.get.json()
    
    new_table_data = TableData(
        name=data['name'],
        field_type=data['field_type'],
        nullable=data['nullable'],
        keys=data['keys'],
        default=data['default'],
        extra=data['extra'],
        schema_id=data['schema_id']
    )
    
    db.session.add(new_table_data)
    db.session.commit()

    return new_table_data.to_dict(), 201

# Update
@table_data_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_table_data(id):
    table_data = TableData.query.get(id)
    if not table_data:
        return jsonify(message='TableData not found'), 404

    data = request.get_json()

    table_data.name = data.get('name', table_data.name)
    table_data.field_type = data.get('field_type', table_data.field_type)
    table_data.nullable = data.get('nullable', table_data.nullable)
    table_data.keys = data.get('keys', table_data.keys)
    table_data.default = data.get('default', table_data.default)
    table_data.extra = data.get('extra', table_data.extra)
    table_data.schema_id = data.get('schema_id', table_data.schema_id)

    db.session.commit()

    return table_data.to_dict()

# Delete
@table_data_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_table_data(id):
    table_data = TableData.query.get(id)
    if not table_data:
        return jsonify(message='TableData not found'), 404

    db.session.delete(table_data)
    db.session.commit()

    return jsonify(message='TableData deleted'), 200