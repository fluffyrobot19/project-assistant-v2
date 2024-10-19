import os
from dotenv import load_dotenv
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager, login_manager
from flask_wtf import CSRFProtect
from backend.controllers.login import login_bp
from backend.controllers.home import home_bp
from backend.controllers.projects import projects_bp
from backend.controllers.reports import reports_bp
from backend.controllers.user_profile import user_profile_bp
from backend.models.database import init_db, populate_db

load_dotenv()
login_manager = LoginManager()


def create_server():
    app = Flask(__name__)
    app.register_blueprint(login_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(user_profile_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(reports_bp)
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://guest_user:guest_password@db:5432/pa_db'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@localhost:{os.getenv("DB_PORT")}/pa_db'
    app.config['SESSION_COOKIE_SAMESITE'] = "strict"
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SECRET_KEY'] = 'secret_key'

    create_extensions(app)

    return app


def create_extensions(app):
    # user session
    login_manager.init_app(app)

    # db
    init_db(app)
    populate_db(app)

    # form
    Bootstrap5(app)
    CSRFProtect(app)


@login_manager.user_loader
def load_user(user_id):
    from backend.models.model_user import User
    return User.query.get(int(user_id))
