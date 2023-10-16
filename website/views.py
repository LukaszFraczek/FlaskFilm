from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import current_user
from .models import Movie, Opinion
from . import db

import json

views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
def home():
    return render_template("home.html", user=current_user)


@views.route("/movies", methods=["GET"])
def movies():
    return render_template("movies.html", user=current_user, movies=Movie.query.all())


@views.route("/movies/<movie_id>", methods=["GET", "POST"])
def movie_single(movie_id: int):
    if request.method == "POST":
        opinion = request.form.get("opinion_form")

        if len(opinion) < 1:
            flash("Your opinion is invalid, because it's too short!", category="error")
        else:
            new_opinion = Opinion(
                text=opinion,
                user_id=current_user.id,
                movie_id=movie_id
            )
            db.session.add(new_opinion)
            db.session.commit()
            flash("Review added!", category="success")

    movie = Movie.query.get(movie_id)

    if movie:
        return render_template("movie_single.html", user=current_user, movie=movie)

    return render_template("movie_not_found.html", user=current_user)


@views.route("/delete-opinion", methods=["POST"])
def delete_opinion():
    opinion = json.loads(request.data)
    opinion_id = opinion["opinion_id"]
    opinion_user_id = opinion["opinion_user_id"]
    opinion_db = Opinion.query.get(opinion_id)
    if opinion_db:
        if current_user.user_type == "admin" or current_user.id == opinion_user_id:
            db.session.delete(opinion_db)
            db.session.commit()

    return jsonify({'message': 'Sucessfuly Deleted.'})
