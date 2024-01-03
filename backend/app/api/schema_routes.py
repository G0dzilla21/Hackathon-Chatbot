from app.models import Schema
from flask import Blueprint, jsonify
from flask_login import login_required

schema_routes = Blueprint('schema', __name__)
