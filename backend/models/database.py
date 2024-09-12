import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()
db = SQLAlchemy()


def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("HOST")}:{os.getenv("DB_PORT")}/pa_db'
    db.init_app(app)
    with app.app_context():
        db.create_all()
        print('Database created successfully')

