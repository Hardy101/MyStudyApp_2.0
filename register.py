from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)


# class Users(db.Model):
#     id = db.Column(db.Integer, unique=True, primary_key=True)
#     user_id = db.Column(db.String(50), nullable=False)
#     user_name = db.Column(db.String(250), nullable=False)
#     user_email = db.Column(db.String(250), nullable=False)
#     user_password = db.Column(db.String(50), nullable=False)

class Book(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    desc = db.Column(db.String(250), nullable=True)
    date = db.Column(db.String(250), nullable=True)
    page_count = db.Column(db.Integer, nullable=True)


with app.app_context():
    db.create_all()
