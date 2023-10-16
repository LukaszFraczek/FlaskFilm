from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from hashlib import md5
from flask_login import LoginManager
from os import path


DB_PATH = "database.db"

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    encryptor = md5()

    app = Flask(__name__)
    app.config["SECRET_KEY"] = encryptor.digest()
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'

    db.init_app(app)
    migrate.init_app(app, db)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Movie, Opinion
    if not path.exists(f"instance/{DB_PATH}"):
        with app.app_context():
            db.create_all()
            print("Database created")

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
