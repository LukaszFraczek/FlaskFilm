from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime, date

from . import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    username = db.Column(db.String(50), unique=True)
    user_type = db.Column(db.String(50), default="user")
    opinions = db.relationship("Opinion", backref='opinion_poster', lazy=True)

    def __init__(self, email: str, username: str, password: str, user_type: str = "user"):
        self.email = email
        self.username = username
        self.password = password
        self.user_type = user_type


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    director = db.Column(db.String(200))
    writer = db.Column(db.String(200))
    genre = db.Column(db.String(200))
    release_date = db.Column(db.Date)
    summary = db.Column(db.String(5000))
    poster = db.Column(db.String(50))
    opinions = db.relationship("Opinion")

    def __init__(self, title: str, director: str, writer: str, genre: str, release_date: date, summary: str, poster: str = "placeholder.png"):
        self.title = title
        self.director = director
        self.writer = writer
        self. genre = genre
        self.release_date = release_date
        self.summary = summary
        self.poster = poster


class Opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(5000))
    post_date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))

    def __init__(self, text: str, user_id: int, movie_id: int, post_date: datetime = func.now()):
        self.text = text
        self.post_date = post_date
        self.user_id = user_id
        self.movie_id = movie_id
