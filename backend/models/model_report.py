from backend.extensions import db

class Report(db.Model):
    __tablename__ = 'pa_reports'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Text())
    # many-to-one
    project = db.Column(db.Integer, db.ForeignKey('pa_projects.id'))
    project_relation = db.relationship('Project', back_populates='report_relation')
    report_type = db.Column(db.Text())
    deadline = db.Column(db.Date)

    # one-to-many
    history_relation = db.relationship(
        'UserAction',
        primaryjoin="and_(UserAction.record_id == Report.id, UserAction.record_type == 'Report')",
        backref='report'
    )

    '''
    def __init__(self, project_id, report_type, deadline, status):
        self.project_id = project_id
        self.report_type = report_type
        self.deadline = deadline
        self.status = status
    '''