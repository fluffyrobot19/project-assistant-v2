import json
from sqlalchemy import text
from backend.extensions import db

# verify users: SELECT id, first_name, last_name, email, username, SUBSTRING(password FROM 1 FOR 6) AS short_password, auth_level FROM members;


def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.execute(text('ALTER SEQUENCE members_id_seq RESTART WITH 1;'))
        db.session.commit()
    print('Database created successfully')


def populate_db(app):
    from backend.models.model_user import User
    with app.app_context():
        with open('backend/models/test_users.json', 'r') as file:
            users = json.load(file)

            for user in users:
                new_user = User(
                    active=user['active'],
                    first_name=user['first_name'],
                    last_name=user['last_name'],
                    email=user['email'],
                    username=user['username'],
                    password=user['password'],
                    auth_level='LOW'
                )

                db.session.add(new_user)

            db.session.commit()
            print('Populated database')
