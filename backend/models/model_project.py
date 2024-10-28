from sqlalchemy import ARRAY
from sqlalchemy.orm import backref
from backend.extensions import db
from backend.models.association_tables import user_project_association

class Project(db.Model):
    __tablename__ = 'pa_projects'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Text())
    full_name = db.Column(db.Text(), unique=True)
    abbrev = db.Column(db.Text(), unique=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    # one-to-many AND same model different type
    budget_total_relation = db.relationship(
        'Budget',
        primaryjoin="and_(Budget.project_relation == Project.id, Budget.budget_type == 'total')",
        back_populates='project_total_relation')
    # one-to-many AND same model different type
    budget_expenditure_relation = db.Relationship(
        'Budget',
        primaryjoin="and_(Budget.project_expenditure_relation == Project.id, Budget.budget_type == 'expenditure')",
        back_populates='projects_expenditure_relation')
    # one-to-many
    report_relation = db.relationship('Report', back_populates='project_relation')
    # many-to-many
    users = db.Column(ARRAY(db.Integer))
    users_relation = db.relationship('User', secondary=user_project_association, back_populates='projects_relation')

    # one-to-many
    history = db.relationship(
        'UserAction',
        primaryjoin="and_(UserAction.record_id == Project.id, UserAction.record_type == 'project')",
        backref='project'
    )

    def __init__(self, full_name, abbrev, start_date, end_date):
        self.full_name = full_name
        self.abbrev = abbrev
        self.start_date = start_date
        self.end_date = end_date
