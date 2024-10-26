import datetime

from backend.extensions import db

class UserAction(db.Model):
    __tablename__ = 'pa_user_action'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Text())
    record_type = db.Column(db.Text())
    record_id = db.Column(db.Integer)
    record_field = db.Column(db.Text())
    value_previous = db.Column(db.Text())
    value_new = db.Column(db.Text())
    action_owner = db.Column(db.Integer, db.ForeignKey('pa_user.id'))
    action_owner_relation = db.Relationship('User', back_populates="history")
    action_approver = db.Column(db.Integer, db.ForeignKey('pa_user.id'))
    action_approver_relation = db.Relationship('User', back_populates="queue")
    action_approver_comment = db.Column(db.Text())
    timestamp = db.Column(db.DateTime, default=datetime.UTC, nullable=False)
