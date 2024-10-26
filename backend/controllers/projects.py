from flask import Blueprint, render_template
from backend.models import Project

projects_bp = Blueprint('projects', __name__)


@projects_bp.route('/projects', methods=['GET'])
def index():
    projects = Project.query.all()
    print(projects)
    return render_template("projects.html", index=True, projects=projects)
