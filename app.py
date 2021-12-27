from dataclasses import dataclass
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:password$@localhost/flask_note_app"
db = SQLAlchemy(app)


@dataclass
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)

    def __init__(self, title, content):
        self.title = title
        self.content = content


@app.route("/add_note", methods=["POST"])
def add_note():
    title = "My programming note"
    content = "Computer programming........"
    note = Note(title, content)
    db.session.add(note)
    db.session.commit()
    return jsonify({"message": "Note Added"})


@app.route("/notes", methods=["GET"])
def fetch_notes():
    notes = Note.query.all()
    return jsonify(notes)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
