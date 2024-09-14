from flask import Blueprint, render_template

reports_bp = Blueprint('reports', __name__)


@reports_bp.route('/reports', methods=['GET'])
def index():
    return render_template("reports.html", index=True)
