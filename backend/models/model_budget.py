from sqlalchemy import ARRAY
from backend.extensions import db

class Budget(db.Model):
    __tablename__ = 'pa_budgets'

    id = db.Column(db.Integer, primary_key=True)
    # many-to-one
    project_relation = db.Column(db.Integer, db.ForeignKey('pa_projects.id'))
    project_total_relation = db.relationship('Project', back_populates='budget_total_relation')
    project_expenditure_relation = db.relationship('Project', back_populates='budget_expenditure_relation')
    budget_type = db.Column(db.Text())
    # one-to-many
    budget_lines = db.Column(ARRAY(db.Integer))
    budget_lines_relation = db.relationship('Transaction', back_populates='budget')

    # one-to-many
    history = db.relationship(
        'UserAction',
        primaryjoin="and_(UserAction.record_id == Budget.id, UserAction.record_type == 'budget')",
        backref='budget'
    )

    '''
    def __init__(self, project_id, budget_type):
        self.project_id = project_id
        self.budget_type = budget_type
        self.transactions = []
        self.deadlines = []
    '''