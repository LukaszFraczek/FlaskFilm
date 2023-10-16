from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password!", category="error")
        else:
            flash("No account with specified username!", category="error")
    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        query_username = User.query.filter_by(username=username).first()
        query_email = User.query.filter_by(email=email).first()

        errors = []
        if query_username:
            errors.append("Username already taken!")
        if query_email:
            errors.append("Email already in use!")
        if len(email) < 4:
            errors.append("Email must be longer than 3 characters")
        if len(username) < 2:
            errors.append("First name must be longer than 1 character")
        if password1 != password2:
            errors.append("Password fields must match each other")
        if len(password1) < 3:
            errors.append("Password must have at least 3 characters")

        if errors:
            for error in errors:
                flash(error, category="error")

        if not errors:
            new_user = User(
                email=email,
                username=username,
                password=generate_password_hash(password1, method="sha256")
            )
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember=True)
            flash("Account created!", category="success")
            return redirect(url_for("views.home"))

    return render_template("sign_up.html", user=current_user)


@auth.route("/settings", methods=["GET", "POST"])
@login_required
def profile():
    if request.method == "POST":
        action = request.form.get("submitButton")

        if action == "changeUsername":
            change_username()
        if action == "changeEmail":
            change_email()
        if action == "changePassword":
            if change_password():
                return redirect(url_for("auth.logout"))

    return render_template("settings.html", user=current_user)


def change_username() -> None:
    new_username = request.form.get("newUsername")
    password = request.form.get("password")

    query_new_username = User.query.filter_by(username=new_username).first()

    errors = []
    if query_new_username:
        errors.append("Username already taken!")
    if len(new_username) < 2:
        errors.append("First name must be longer than 1 character")
    if not check_password_hash(current_user.password, password):
        errors.append("Incorrect password!")

    if errors:
        for error in errors:
            flash(error, category="error")

    if not errors:
        current_user.username = new_username
        db.session.commit()
        flash("Username changed!", category="success")


def change_email() -> None:
    new_email = request.form.get("newEmail")
    password = request.form.get("password")

    query_new_email = User.query.filter_by(email=new_email).first()

    errors = []
    if query_new_email:
        errors.append("Email already in use!")
    if len(new_email) < 4:
        errors.append("Email must be longer than 3 characters")
    if not check_password_hash(current_user.password, password):
        errors.append("Incorrect password!")

    if errors:
        for error in errors:
            flash(error, category="error")

    if not errors:
        current_user.email = new_email
        db.session.commit()
        flash("Email changed!", category="success")


def change_password() -> bool:
    new_password1 = request.form.get("newPassword1")
    new_password2 = request.form.get("newPassword2")
    password = request.form.get("password")

    errors = []

    if not check_password_hash(current_user.password, password):
        errors.append("Incorrect password!")
    if new_password1 != new_password2:
        errors.append("Passwords must match each other")
    if len(new_password1) < 3:
        errors.append("Password must have at least 3 characters")

    if not errors:
        current_user.password = generate_password_hash(new_password1, method="sha256")
        db.session.commit()
        flash("Password changed!", category="success")
        return True

    for error in errors:
        flash(error, category="error")

    return False
