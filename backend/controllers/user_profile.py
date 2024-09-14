from flask import Blueprint, render_template

user_profile_bp = Blueprint('user_profile', __name__)


@user_profile_bp.route('/my-profile', methods=['GET'])
def index():
    return render_template("user_profile.html", index=True)
