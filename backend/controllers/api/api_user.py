from fastapi.encoders import jsonable_encoder
from flask import Blueprint, jsonify
from backend.models.models import User

user_api_bp = Blueprint('user', __name__)


@user_api_bp.route('/api/user/all')
def get_users():
    users = User.query.all()
    users_list = [user.to_dict() for user in users]
    return jsonify(users_list)


@user_api_bp.route('/api/user/<user_id>')
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return jsonable_encoder(user)
