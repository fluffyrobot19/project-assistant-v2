from fastapi.encoders import jsonable_encoder
from flask import jsonify
from flask_login import UserMixin
from sqlalchemy import ARRAY
from werkzeug.security import generate_password_hash, check_password_hash
from backend.extensions import db
from backend.models.association_tables import user_project_association

class User(db.Model, UserMixin):
    __tablename__ = 'pa_users'

    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Text())
    first_name = db.Column(db.Text())
    last_name = db.Column(db.Text())
    email = db.Column(db.Text(), unique=True)
    username = db.Column(db.Text())
    password = db.Column(db.Text())
    auth_level = db.Column(db.Text())
    projects = db.Column(ARRAY(db.Integer))
    projects_relation = db.relationship('Project', secondary=user_project_association, back_populates='users_relation')
    history = db.Column(ARRAY(db.Integer,db.ForeignKey('pa_user_action.id')))
    history_relation = db.Relationship('UserAction', back_populates='action_owner')
    queue = db.Column(ARRAY(db.Integer, db.ForeignKey('pa_user_action.id')))
    queue_relation = db.Relationship('UserAction', back_populates='action_approver')

    def __init__(self, activity, first_name, last_name, email, username, password, auth_level):
        self.active = activity
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
