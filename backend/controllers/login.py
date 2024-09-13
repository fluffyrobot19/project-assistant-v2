from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_user
from backend.models.forms.login_form import LoginForm
from backend.models.models import User

login_bp = Blueprint('login', __name__)


@login_bp.route('/', methods=['GET'])
def index():
    return render_template("base_login.html", index=True)


@login_bp.route('/login/', methods=['GET', 'POST'])
def login():
    # users = requests.get("http://localhost:5000/api/users").json()
    form = LoginForm()

    if form.validate_on_submit():
        username = form.data['username']
        password = form.data['password']
        user = User.query.filter_by(username=username).first()

        if user and user.is_password_correct(password):
            login_user(user)
            return redirect(url_for('home.home'))

    return render_template('login.html', form=form)


