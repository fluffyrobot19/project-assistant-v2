from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)


@home_bp.route('/home')
def home():

    return render_template("base_home.html")


@home_bp.route('/my-profile')
def my_profile():
    return '<h1>this is user profile</h1>'


@home_bp.route('/reports')
def reports():
    return '<h1>this is reports</h1>'
