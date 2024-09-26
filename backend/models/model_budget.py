from sqlalchemy import ARRAY
from backend.extensions import db

class Budget(db.Model):
    __tablename__ = 'budgets'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    budget_type = db.Column(db.Text())
    transaction = db.relationship('Transaction', back_populates='budget')
    deadlines = db.Column(ARRAY(db.Date))

    def __init__(self, project_id, budget_type):
        self.project_id = project_id
        self.budget_type = budget_type
        self.transactions = []
        self.deadlines = []
