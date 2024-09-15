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


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.Text(), unique=True)
    abbrev = db.Column(db.Text(), unique=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    budget_id = db.relationship('Budget', backref=backref('project', uselist=False))
    report = db.relationship('Report', back_populates='project')
    history = db.Column(db.Text())
    user = db.relationship('User', secondary=user_project_association, back_populates='project')

    def __init__(self, full_name, abbrev, start_date, end_date, budget):
        self.full_name = full_name
        self.abbrev = abbrev
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget


class Budget(db.Model):
    __tablename__ = 'budgets'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    budget_type = db.Column(Enum(BudgetType))
    transaction = db.relationship('Transaction', back_populates='budget')
    deadlines = db.Column(ARRAY(db.Date))

    def __init__(self, project_id, budget_type):
        self.project_id = project_id
        self.budget_type = budget_type
        self.transactions = []
        self.deadlines = []


class Report(db.Model):
    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    project = db.relationship('Project', back_populates='report')
    report_type = db.Column(db.Text())
    deadline = db.Column(db.Date)
    status = db.Column(db.Text())

    def __init__(self, project_id, report_type, deadline, status):
        self.project_id = project_id
        self.report_type = report_type
        self.deadline = deadline
        self.status = status


class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    budget_id = db.Column(db.Integer, db.ForeignKey('budgets.id'))
    budget = db.relationship('Budget', back_populates='transaction')
    code = db.Column(Enum(TransactionCode))
    description = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    amount_per_quantity = db.Column(db.Integer)
    original_amount = db.Column(db.Integer)
    original_currency = db.Column(Enum(Currency))
    target_currency = db.Column(Enum(Currency))
    target_amount = db.Column(db.Integer)

    def __init__(self, budget_id, code, description, quantity, amount_per_quantity, original_amount, original_currency, target_currency, target_amount):
        self.budget_id = budget_id
        self.code = code
        self.description = description
        self.quantity = quantity
        self.amount_per_quantity = amount_per_quantity
        self.original_amount = original_amount
        self.original_currency = original_currency
        self.target_currency = target_currency
        self.target_amount = target_amount

