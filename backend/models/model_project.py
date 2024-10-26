from sqlalchemy import ARRAY
from sqlalchemy.orm import backref
from backend.extensions import db
from backend.models.association_tables import user_project_association

class Project(db.Model):
    __tablename__ = 'pa_project'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Text())
    full_name = db.Column(db.Text(), unique=True)
    abbrev = db.Column(db.Text(), unique=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    # budgets - make previous versions available
    budget_total = db.Column(ARRAY(db.Integer))
    budget_total_relation = db.relationship('Budget', backref=backref('pa_project', uselist=False))
    budget_expenditure = db.Column(ARRAY(db.Integer))
    budget_expenditure_relation = db.Relationship('Budget', backref=backref('pa_project', uselist=False))
    # reports
    reports = db.Column(ARRAY(db.Integer))
    report = db.relationship('Report', back_populates='project')
    # history records - all user actions related to project
    history = db.Column(ARRAY(db.Integer))
    # users
    users = db.Column(ARRAY(db.Integer))
    users_relation = db.relationship('User', secondary=user_project_association, back_populates='projects')

    def __init__(self, full_name, abbrev, start_date, end_date, budget):
        self.full_name = full_name
        self.abbrev = abbrev
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
