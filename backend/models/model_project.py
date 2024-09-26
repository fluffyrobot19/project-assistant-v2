from sqlalchemy.orm import backref
from backend.extensions import db
from backend.models.association_tables import user_project_association

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
    users = db.relationship('User', secondary=user_project_association, back_populates='projects')

    def __init__(self, full_name, abbrev, start_date, end_date, budget):
        self.full_name = full_name
        self.abbrev = abbrev
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
