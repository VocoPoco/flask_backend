from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from models.database import Database

db = Database().db


class Task(db.Model):
    def __init__(self):
        self.id = self.db.Column(self.db.Integer, primary_key=True)
        self.title = self.db.Column(self.db.String(120), unique=True, nullable=False)
        self.description = self.db.Column(self.db.String(500), nullable=True)
        self.due_date = self.db.Column(self.db.Date, default=None)
        self.created_at = db.Column(self.db.DateTime, default=datetime.utcnow)
        self.state = self.db.Column(
            self.db.Enum("TODO", "In Progress", "Finished"), default="TODO"
        )

    def __repr__(self):
        return f"{self.id}, {self.title}, {self.description}, {self.state}"
