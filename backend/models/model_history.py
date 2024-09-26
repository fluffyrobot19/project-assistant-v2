from backend.extensions import db

class History(db.Model):
    __tablename__ = 'history'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    user = db.Relationship('User', back_populates="history")
