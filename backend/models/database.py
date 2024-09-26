import json
from sqlalchemy import text
from backend.extensions import db
from backend.models.enums import AuthLevel

# verify users: SELECT id, first_name, last_name, email, username, SUBSTRING(password FROM 1 FOR 6) AS short_password, auth_level FROM members;


def init_db(app):
    db.init_app(app)
    with app.app_context():
        clear_db(app)
        create_enums(app)
        db.create_all()
    print('Database created successfully')


def populate_db(app):
    from backend.models.model_user import User
    with app.app_context():
        with open('backend/models/test_users.json', 'r') as file:
            users = json.load(file)

            for user in users:
                new_user = User(
                    first_name=user['first_name'],
                    last_name=user['last_name'],
                    email=user['email'],
                    username=user['username'],
                    password=user['password'],
                    auth_level=AuthLevel.LOW
                )

                db.session.add(new_user)

            db.session.commit()
            print('Populated database')


def create_enums(app):
    with app.app_context():
        db.session.execute(text("CREATE TYPE AuthLevel AS ENUM ('HIGH', 'MID', 'LOW');"))
        db.session.execute(text("CREATE TYPE BudgetType AS ENUM ('actual', 'target');"))
        db.session.execute(text("CREATE TYPE TransactionCode AS ENUM ('A', 'B', 'C');"))
        db.session.execute(text("CREATE TYPE Currency AS ENUM ('HUF', 'EUR', 'USD');"))
        db.session.commit()


def clear_db(app):
    with app.app_context():
        db.session.execute(text("DROP TABLE IF EXISTS members CASCADE;"))
        db.session.execute(text("DROP TABLE IF EXISTS projects CASCADE;"))
        db.session.execute(text("DROP TABLE IF EXISTS budgets CASCADE;"))
        db.session.execute(text("DROP TABLE IF EXISTS reports CASCADE;"))
        db.session.execute(text("DROP TABLE IF EXISTS transactions CASCADE;"))
        db.session.execute(text("DROP TYPE AuthLevel CASCADE;"))
        db.session.execute(text("DROP TYPE BudgetType CASCADE;"))
        db.session.execute(text("DROP TYPE TransactionCode CASCADE;"))
        db.session.execute(text("DROP TYPE Currency CASCADE;"))
        db.session.commit()
