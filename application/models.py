from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    entry = db.Column(db.String(1000))

    def __init__(self, title, entry):
        self.title = title
        self.entry = entry