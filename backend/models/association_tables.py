from backend.extensions import db

user_project_association = db.Table(
    'user_project_association',
    db.Column('user_id', db.Integer, db.ForeignKey('pa_user.id'), primary_key=True),
    db.Column('project_id', db.Integer, db.ForeignKey('pa_project.id'), primary_key=True)
)
