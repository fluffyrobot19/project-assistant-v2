from flask import Blueprint
from backend.models.model import User

users_api_bp = Blueprint('users', __name__, url_prefix='/api/users')


@users_api_bp.route('/')
def get_users():
    users = User.query.all()
    return users
