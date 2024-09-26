from backend.extensions import db

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
