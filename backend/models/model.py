from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .database.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.column(db.String(100))
    username = db.Column(db.String(50))

    def __repr__(self):
        return '<User %r>' % self.username

