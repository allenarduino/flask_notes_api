from database import db
import json
from dataclasses import dataclass


@dataclass
class Note(db.Model):

    id: int
    title: str
    content: str

    __tablename__ = "note"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def serialize(self):
        return json.dumps(self, default=lambda o: o.__dict__)
