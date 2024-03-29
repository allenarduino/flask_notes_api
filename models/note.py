from database import db
import json
import datetime
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
    time_created= db.Column(db.DateTime,default=datetime.datetime.now)
  

    def __init__(self, title, content):
        self.title = title
        self.content = content

       
