from flask import Flask
from backend.controllers.login import login_bp
from backend.controllers.homepage import home_bp
from backend.controllers.api.get_users import users_api_bp
from backend.models.database.database import init_db


def create_server():
    app = Flask(__name__)

    # print(__name__)
    # backend

    # register blueprint: blueprint + url prefix
    app.register_blueprint(login_bp, url_prefix=login_bp.url_prefix)
    app.register_blueprint(home_bp, url_prefix=home_bp.url_prefix)

    # models
    app.register_blueprint(users_api_bp, url_prefix=users_api_bp.url_prefix)

    # init db
    init_db(app)

    return app
