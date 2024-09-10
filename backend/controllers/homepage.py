from flask import Blueprint, request

home_bp = Blueprint('home', __name__, url_prefix='/home')


@home_bp.route('/')
def home():
    return ('<h1>homepage</h1>'
            '<a href="my-profile">My profile</a><br>'
            '<a href="projects">Projects</a><br>'
            '<a href="reports">Reports</a><br>')


@home_bp.route('/my-profile')
def my_profile():
    return '<h1>this is user profile</h1>'


@home_bp.route('/projects')
def projects():
    return '<h1>this is projects</h1>'


@home_bp.route('/reports')
def reports():
    return '<h1>this is reports</h1>'
