from flask import Blueprint, render_template
from flask_login import current_user

home_bp = Blueprint('home', __name__)


@home_bp.route('/home')
def index():
    return render_template("home.html", user=current_user.username)
