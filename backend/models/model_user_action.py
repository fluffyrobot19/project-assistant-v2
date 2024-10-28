import datetime

from backend.extensions import db

class UserAction(db.Model):
    __tablename__ = 'pa_user_actions'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Text())
    # how to get??
    record_type = db.Column(db.Text())
    record_id = db.Column(db.Integer)
    record_field = db.Column(db.Text())
    # polymorphic association
    __mapper_args__ = {
        'polymorphic_on': record_type,
        'polymorphic_identity': 'user_action'
    }
    value_previous = db.Column(db.Text())
    value_new = db.Column(db.Text())
    # many-to-one
    action_owner = db.Column(db.Integer, db.ForeignKey('pa_users.id'))
    action_owner_relation = db.Relationship('User', back_populates='history')
    # many-to-one
    action_approver = db.Column(db.Integer, db.ForeignKey('pa_users.id'))
    action_approver_relation = db.Relationship('User', back_populates='queue')
    action_approver_comment = db.Column(db.Text())
    timestamp = db.Column(db.DateTime, default=datetime.UTC, nullable=False)
