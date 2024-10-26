from sqlalchemy import ARRAY
from backend.extensions import db

class Budget(db.Model):
    __tablename__ = 'pa_budget'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    budget_type = db.Column(db.Text())
    budget_lines = db.Column(ARRAY(db.Integer))
    budget_lines_relation = db.relationship('Transaction', back_populates='budget')
    deadlines = db.Column(ARRAY(db.Date))

    def __init__(self, project_id, budget_type):
        self.project_id = project_id
        self.budget_type = budget_type
        self.transactions = []
        self.deadlines = []
