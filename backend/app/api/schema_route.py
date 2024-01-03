from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import db, Schema

schema_routes = Blueprint('schema', __name__)

# Get all
@schema_routes.route('/schema', methods=['GET'])
@login_required
def get_all_schemas():
    schemas = Schema.query.all()
    return jsonify({'schema': [schema.to_dict() for schema in schemas]})

# Get by ID
@schema_routes.route('/schema/<int:schema_id>', methods=['GET'])
@login_required
def get_schema_by_id(schema_id):
    schema = Schema.query.get(schema_id)
    if not schema:
        return jsonify({'error': 'Schema not found'}), 404

    return jsonify(schema.to_dict())

# Create
@schema_routes.route('/schema', methods=['POST'])
@login_required
def create_schema():
    data = request.get_json()

    new_schema = Schema(
        name=data['name'],
        user_id=data['user_id']
    )

    db.session.add(new_schema)
    db.session.commit()

    return jsonify(new_schema.to_dict()), 201



# Update
@schema_routes.route('/schema/<int:schema_id>', methods=['PUT'])
@login_required
def update_schema(schema_id):
    schema = Schema.query.get(schema_id)
    if not schema:
        return jsonify({'error': 'Schema not found'}), 404

    data = request.get_json()

    schema.name = data.get('name', schema.name)
    schema.user_id = data.get('user_id', schema.user_id)

    db.session.commit()

    return jsonify(schema.to_dict())

# Delete
@schema_routes.route('/schema/<int:schema_id>', methods=['DELETE'])
@login_required
def delete_schema(schema_id):
    schema = Schema.query.get(schema_id)
    if not schema:
        return jsonify({'error': 'Schema not found'}), 404

    db.session.delete(schema)
    db.session.commit()

    return jsonify({'message': 'Schema deleted'}), 200