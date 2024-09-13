from flask import Blueprint, render_template

projects_bp = Blueprint('projects', __name__)


@projects_bp.route('/projects', methods=['GET'])
def index():
    return render_template("base_login.html", index=True)
