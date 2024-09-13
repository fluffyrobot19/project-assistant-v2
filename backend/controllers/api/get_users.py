from flask import Blueprint, jsonify
from backend.models.models import User

users_api_bp = Blueprint('users', __name__)


@users_api_bp.route('/')
def get_users():
    users = User.query.all()
    users_list = [user.to_dict() for user in users]
    return jsonify(users_list)
