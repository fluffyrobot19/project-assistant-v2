from flask import Blueprint

login_bp = Blueprint('login', __name__, url_prefix='/login')


@login_bp.route('/')
def index():
    return ('<h1>login page</h1>'
            '<div>Username:</div>'
            '<input></input>'
            '<div>Password:</div>'
            '<input></input>'
            '<br>'
            '<a href="/home">Enter</a>')
