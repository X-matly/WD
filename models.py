from database import db

from datetime import datetime


class event(db.Model):
    __tablename__ = 'nju'
    ID = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.String(50))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    significance = db.Column(db.Integer)
    complete = db.Column(db.Integer)
    note = db.Column(db.Text)
