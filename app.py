from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:password$@localhost/flask_note_app"
db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)

    def __init__(self, title, content):
        self.title = title
        self.content = content


note = Note("My Flask Note", "There are lot of apps powered by flask")
db.create_all()
db.session.commit()


@app.route("/notes", methods=["GET"])
def fetch_notes():
    notes = Note.query.all()
    my_notes = []
    for my_note in my_notes:
        my_notes.append(my_note.toDict())

    return jsonify(my_notes)


if __name__ == "__main__":
    app.run(debug=True)
