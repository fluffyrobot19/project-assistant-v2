from enum import Enum
from backend.extensions import db
from backend.models.enums import TransactionCode, Currency


class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    budget_id = db.Column(db.Integer, db.ForeignKey('budgets.id'))
    budget = db.relationship('Budget', back_populates='transaction')
    code = db.Column(Enum(TransactionCode))
    description = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    amount_per_quantity = db.Column(db.Integer)
    original_amount = db.Column(db.Integer)
    original_currency = db.Column(Enum(Currency))
    target_currency = db.Column(Enum(Currency))
    target_amount = db.Column(db.Integer)

    def __init__(self, budget_id, code, description, quantity, amount_per_quantity, original_amount, original_currency, target_currency, target_amount):
        self.budget_id = budget_id
        self.code = code
        self.description = description
        self.quantity = quantity
        self.amount_per_quantity = amount_per_quantity
        self.original_amount = original_amount
        self.original_currency = original_currency
        self.target_currency = target_currency
        self.target_amount = target_amount
