from fastapi.encoders import jsonable_encoder
from flask import jsonify
from flask_login import UserMixin
from sqlalchemy import ARRAY, Enum
from sqlalchemy.orm import backref
from werkzeug.security import generate_password_hash, check_password_hash
from backend.extensions import db
from backend.models.association_tables import user_project_association
from backend.models.enums import AuthLevel, BudgetType, TransactionCode, Currency


class User(db.Model, UserMixin):
    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text())
    last_name = db.Column(db.Text())
    email = db.Column(db.Text(), unique=True)
    username = db.Column(db.Text(), unique=True)
    password = db.Column(db.Text())
    auth_level = db.Column(Enum(AuthLevel))
    # many-to-many
    project = db.relationship('Project', secondary=user_project_association, back_populates='user')

    def __init__(self, first_name, last_name, email, username, password, auth_level):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)
        self.auth_level = auth_level

    def is_password_correct(self, password_str):
        return check_password_hash(self.password, password_str)

    @staticmethod
    def get_users():
        users = User.query.all()
        users_list = [user.to_dict() for user in users]
        return jsonify(users_list)

    @staticmethod
    def get_user(user_id):
        user = User.query.filter_by(id=user_id).first()
        return jsonable_encoder(user)
