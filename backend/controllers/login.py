from flask import Blueprint, redirect, render_template

from backend.models.forms.login_form import LoginForm
import requests

login_bp = Blueprint('login', __name__, url_prefix='/')


@login_bp.route('/', methods=['GET', 'POST'])
def index():
    users = requests.get("http://localhost:5000/api/users").json()
    form = LoginForm()

    if form.validate_on_submit():
        form_data = form.data
        username = form_data['username']
        password = form_data['password']

        for user in users:
            print(user['username'])

            if username == user['username'] and password == user['password']:
                redirect("http://localhost:5000/home")
            else:
                print('invalid login')

    return render_template("login.html", form=form)


