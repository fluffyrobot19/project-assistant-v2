import os
from dotenv import load_dotenv
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect

from backend.controllers.login import login_bp
from backend.controllers.homepage import home_bp
from backend.controllers.api.get_users import users_api_bp
from backend.models.database import init_db, db
load_dotenv()


def create_server():
    app = Flask(__name__)

    app.register_blueprint(login_bp, url_prefix=login_bp.url_prefix)
    app.register_blueprint(home_bp, url_prefix=home_bp.url_prefix)
    app.register_blueprint(users_api_bp, url_prefix=users_api_bp.url_prefix)

    # init db
    init_db(app)

    # form
    app.secret_key = os.getenv("SECRET_KEY")
    Bootstrap5(app)
    CSRFProtect(app)

    return app
