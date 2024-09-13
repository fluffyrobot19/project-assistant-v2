import json
from backend.extensions import db


def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
    print('Database created successfully')


def populate_db(app):
    from backend.models.models import User
    with app.app_context():
        db.session.query(User).delete()
        with open('backend/models/test_users.json', 'r') as file:
            users = json.load(file)

            index = 1
            for user in users:
                new_user = User(
                    id=index,
                    first_name=user['first_name'],
                    last_name=user['last_name'],
                    email=user['email'],
                    username=user['username'],
                    password=user['password']
                )

                db.session.add(new_user)
                index = index + 1

            db.session.commit()
            print('Populated database')
