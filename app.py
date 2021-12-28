from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from constants import DATABASE_URI
from models.note import Note


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)


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
