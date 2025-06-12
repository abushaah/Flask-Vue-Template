from flask import Blueprint, jsonify
from app.models import Item

bp = Blueprint('items', __name__)

@bp.route('/items')
def get_items():
    return jsonify([{'id': i.id, 'name': i.name} for i in Item.query.all()])
