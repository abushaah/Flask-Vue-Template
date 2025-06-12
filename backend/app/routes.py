from flask import Blueprint, jsonify
from .models import Item

api = Blueprint('api', __name__)

@api.route('/items')
def get_items():
    return jsonify([{'id': item.id, 'name': item.name} for item in Item.query.all()])
