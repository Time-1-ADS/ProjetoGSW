from . import db

id = db.Column(db.Interger, primary_key=True)
email = db.Column(db.String(100), unique=True)
password = db.Column(db.String(100))
